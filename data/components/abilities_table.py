from random import randint, shuffle

import pygame as pg

from .. import prepare
from ..components.labels import Label
from ..components.info_tables import ABIL_MODS, ABIL_COLORS, RACIAL_ABIL_MODS


class Die(pg.sprite.Sprite):
    images = {x:
                pg.transform.scale(prepare.GFX["dieWhite{}".format(x)], (24, 24))
                for x in range(1, 7)}

    def __init__(self, topleft, value, *groups):
        super(Die, self).__init__(*groups)
        self.value = value
        self.image = self.images[self.value]
        self.rect = self.image.get_rect(topleft=topleft)


class DiceGroup(object):
    def __init__(self, topleft, *groups):
        self.dice = pg.sprite.Group()

        rolls = [randint(1, 6) for x in range(4)]
        dropped = sorted(rolls, reverse=True)[:-1]
        shuffle(dropped)
        img_width, img_height = 24, 24
        space = 3
        for i, score in enumerate(dropped):
            Die((i * (img_width + space), 0), score, self.dice)
        left, top = topleft
        self.rect = pg.Rect(left, top, (3 * img_width) + (2 * space), img_height)
        self.image = pg.Surface(self.rect.size)
        self.dice.draw(self.image)

    def tally(self):
        return sum((die.value for die in self.dice))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

     
class AbilitySlot(object):
    def __init__(self, name, topleft):
        self.name = name
        self.topleft = topleft
        self.labels = pg.sprite.Group()
        self.dice = DiceGroup(self.topleft)
        self.score = self.dice.tally()
        self.abil_mod = ABIL_MODS[self.score]
        left, cy = self.dice.rect.right, self.dice.rect.centery
        
        self.name_label = Label("{}".format(name),
                    {"midleft": (left + 6, cy)}, self.labels, font_size=20,
                    font_path=prepare.FONTS["weblysleekuisb"], text_color=ABIL_COLORS[name])
        self.score_label = Label("{}".format(self.score),
                    {"midright": (left + 83, cy)}, self.labels, font_size=16)
        self.abil_mod_label = Label("{}".format(self.abil_mod),
                    {"midright": (left + 145, cy)}, self.labels, font_size=16)
        self.racial_mods_label = Label("", {"midleft": (left + 172, cy)}, self.labels, font_size=12)
        
    def update(self, race):
        self.score = self.dice.tally()
        text = ""
        if race in RACIAL_ABIL_MODS:
            if self.name in RACIAL_ABIL_MODS[race]:
                mod = RACIAL_ABIL_MODS[race][self.name]
                self.score += mod
                text = "{:+} Race".format(mod)
        self.racial_mods_label.set_text(text)
        self.score_label.set_text("{}".format(self.score))
        self.abil_mod = ABIL_MODS[self.score]
        self.abil_mod_label.set_text("{:+}".format(self.abil_mod))

    def draw(self, surface):
        self.labels.draw(surface)
        self.dice.draw(surface)


class AbilitiesTable(object):
    def __init__(self, topleft):
        self.slots = {}
        names = ["Str", "Dex", "Con", "Int",
                    "Wis", "Cha"]
        self.labels = pg.sprite.Group()
        left, top = topleft
        Label("Abilities", {"midtop": (left + 60, top)}, self.labels,
                    font_size=24)
        Label("Score", {"midtop": (left + 160, top + 8)}, self.labels,
                    font_size=16)
        Label("Mod.", {"midtop": (left + 223, top + 8)}, self.labels,
                    font_size=16)
        top += 40
        for name in names:
            self.slots[name] = AbilitySlot(name, (left, top))
            top += 40
        self.grabbed = None
        self.all_dice_rect = self.slots["Str"].dice.rect.unionall(
                    [slot.dice.rect for slot in self.slots.values()])

    def swap_dice(self, grabbed_slot, dest_slot):
        grabbed_dice = grabbed_slot.dice
        grabbed_slot.dice = dest_slot.dice
        dest_slot.dice = grabbed_dice
        dest_slot.dice.rect.topleft = dest_slot.topleft
        grabbed_slot.dice.rect.topleft = grabbed_slot.topleft
        self.grabbed = None

    def get_event(self, event, scale):
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = int(event.pos[0] * scale[0]), int(event.pos[1] * scale[1])
            for slot in self.slots.values():
                rect = slot.dice.rect
                if rect.collidepoint((x, y)):
                    self.grabbed = slot
                    self.grab_offset = x - rect.left, y - rect.top

        elif event.type == pg.MOUSEBUTTONUP:
            if self.grabbed is None:
                return
            for slot in self.slots.values():
                if slot is not self.grabbed and slot.dice.rect.collidepoint(event.pos):
                    self.swap_dice(self.grabbed, slot)
                    break
            else:
                self.grabbed.dice.rect.topleft = self.grabbed.topleft
            self.grabbed = None

    def update(self, scaled_mouse, race):
        if self.grabbed:
            mx, my = scaled_mouse
            x, y = self.grab_offset
            self.grabbed.dice.rect.top = my - y
            self.grabbed.dice.rect.clamp_ip(self.all_dice_rect)
        for slot in self.slots.values():
            slot.update(race)

    def draw(self, surface):
        self.labels.draw(surface)
        for slot in self.slots.values():
            slot.draw(surface)
        if self.grabbed:
            self.grabbed.draw(surface)

