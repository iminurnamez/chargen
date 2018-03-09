import pygame as pg

from .. import tools, prepare
from ..components.character_generator import CharacterGenerator #FillableForm, CHARACTER_SHEET


class Gameplay(tools._State):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.generator = CharacterGenerator()
        
    def startup(self, persistent):
        self.persist = persistent
        
    def get_event(self,event, scale):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                self.quit = True
        self.generator.get_event(event, scale)
        
    def update(self, dt, scale):
        self.generator.update(dt, scale)

    def draw(self, surface):
        surface.fill(pg.Color("gray5"))
        self.generator.draw(surface)
        