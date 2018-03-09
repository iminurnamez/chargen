from collections import deque

import pygame as pg

from .. import prepare
from ..components.labels import Label, Button, ButtonGroup, Textbox


class Selector(object):
    def __init__(self, name, midleft, width, horiz_offset, values):
        self.values = deque(values)
        self.value = self.values[0]
        img = prepare.GFX["arrow-left"]
        left, cy = midleft
        cx = left + horiz_offset
        self.buttons = ButtonGroup()
        self.name_label = Label(name, {"midleft": midleft}, font_size=24)
        Button({"midright": (cx - (width//2), cy)}, self.buttons, call=self.rotate,
                    args=1, idle_image=img, button_size=img.get_size())
        Button({"midleft": (cx + (width//2), cy)}, self.buttons, call=self.rotate,
                    args=-1, idle_image=pg.transform.flip(img, True, False),
                    button_size=img.get_size())
        
        self.value_label = Label("{}".format(self.value), {"center": (cx, cy)})

    def rotate(self, direction):
        self.values.rotate(direction)
        self.value = self.values[0]
        self.value_label.set_text("{}".format(self.value))

    def get_event(self, event):
        self.buttons.get_event(event)

    def update(self, mouse_pos):
        self.buttons.update(mouse_pos)
        text = "{}".format(self.value)
        if self.value_label.text != text:
            self.value_label.set_text(text)

    def draw(self, surface):
        self.buttons.draw(surface)
        self.name_label.draw(surface)
        self.value_label.draw(surface)

    
class Incrementor(object):
    def __init__(self, name, midleft, width, horiz_offset, value, min_value, max_value):
        self.name = name
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.name_label = Label(name, {"midleft": midleft}, font_size=24)
        left, cy = midleft
        cx = left + horiz_offset
        self.value_label = Label("{}".format(self.value), {"center": (cx, cy)})
        self.buttons = ButtonGroup()
        img = prepare.GFX["arrow-left"]
        Button({"midright": (cx - (width//2), cy)}, self.buttons, call=self.increment,
                    args=-1, idle_image=img, button_size=img.get_size())
        Button({"midleft": (cx + (width//2), cy)}, self.buttons, call=self.increment,
                    args=1, idle_image=pg.transform.flip(img, True, False),
                    button_size=img.get_size())

    def increment(self, amount):
        self.value += amount
        if self.value < self.min_value:
            self.value = self.min_value
        elif self.value > self.max_value:
            self.value = self.max_value
        self.value_label.set_text("{}".format(self.value))

    def get_event(self, event):
        self.buttons.get_event(event)

    def update(self, mouse_pos):
        self.buttons.update(mouse_pos)

    def draw(self, surface):
        self.buttons.draw(surface)
        self.name_label.draw(surface)
        self.value_label.draw(surface)
        
        
class FillableForm(object):
    def __init__(self, topleft, vert_space, fields_dict, **kwargs):
        self.labels = pg.sprite.Group()
        fields = []
        self.fields_by_name = {}
        left, top = topleft
        for name in fields_dict:
            val = fields_dict[name]
            label = Label(name, {"topleft": (left, top)}, self.labels)
            box_left = label.rect.right + 10
            box = Textbox({"topleft": (box_left, top)}, **kwargs)
            box.buffer = "{}".format(val)
            box.buffer_index = len(box.buffer)
            box.active = False
            box.update(0)
            fields.append(box)
            self.fields_by_name[name] = box
            top += vert_space
        self.fields = deque(fields)
        self.active_field = self.fields[0]
        self.active_field.active = True

    def get_event(self, event):
        self.active_field.get_event(event)
        if event.type == pg.KEYUP:
            if event.key == pg.K_TAB:
                if pg.key.get_pressed()[pg.K_LSHIFT]:
                    direction = 1
                else:
                    direction = -1
                self.fields.rotate(direction)
                self.active_field.active = False
                self.active_field.cursor_active = False
                self.active_field.update(0)
                self.active_field = self.fields[0]
                self.active_field.active = True

    def update(self, dt):
        self.active_field.update(dt)

    def draw(self, surface):
        self.labels.draw(surface)
        for field in self.fields:
            field.draw(surface)
        