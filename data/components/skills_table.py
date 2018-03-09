from itertools import cycle

import pygame as pg

from .. import prepare
from ..components.labels import Label, Button, ButtonGroup
from ..components.feats_table import FEATS
from ..components.info_tables import (SKILL_ABIL_MAP, RACIAL_SKILL_BONUSES,
            ABIL_MODS, SKILL_POINTS_PER_LEVEL, CLASS_SKILLS, SYNERGIES, COLORS,
            ABIL_COLORS)


class SkillsTable(object):
    def __init__(self, topleft, race, char_class, level, abilities_table):
        print "Race: {}".format(race)
        ability_scores = {name: slot.score
                    for name, slot in abilities_table.slots.items()}
        points = self.get_skill_points(ability_scores, race, char_class, level)
        self.class_skills = CLASS_SKILLS[char_class]
        self.unassigned_points = points
        self.assigned_points = 0
        self.max_ranks = level + 3
        self.headers = self.make_headers(topleft)
        self.slots = self.make_slots(topleft, ability_scores, race)
        self.distribute_default_skills()
        self.buttons = self.make_rank_buttons()

    def make_headers(self, topleft):
        names = ["Skill", "Total", "Abil Mod",
                    "Ranks {}/{}".format(self.assigned_points,(self.unassigned_points+self.assigned_points)), "Misc."]
        offsets = [0, 370, 445, 530, 610] #[0, 250, 330, 430, 530]
        
        left, top = topleft
        headers = pg.sprite.Group()
        for name, offset in zip(names, offsets):
            if offset == offsets[3]:
                self.ranks_header = Label(name, {"midtop": (left + offset, top)}, headers, font_size=16)
            else:
                Label(name, {"midtop": (left + offset, top)}, headers, font_size=16)
        return headers

    def make_slots(self, topleft, ability_scores, race):
        self.bg_rects = []
        colors = cycle([pg.Color("gray10"), pg.Color("gray5")])
        space = 23
        left, top = topleft[0], topleft[1] + space
        slots = {}
        for skill_name in sorted(SKILL_ABIL_MAP.keys()):
            misc_mods = []
            ability = SKILL_ABIL_MAP[skill_name]
            abil_mod = ABIL_MODS[ability_scores[ability]]

            if skill_name in self.class_skills:
                cross_class = False
            else:
                cross_class = True
            if race in RACIAL_SKILL_BONUSES:
                if skill_name in RACIAL_SKILL_BONUSES[race]:
                    misc_mods.append(
                                ("Race", RACIAL_SKILL_BONUSES[race][skill_name]))
            slot = SkillSlot((left, top), skill_name, abil_mod,
                        cross_class, misc_mods)
            slots[skill_name] = slot
            self.bg_rects.append((pg.Rect(left, top + 4, 760, space), next(colors)))
            top += space
        return slots
        
    def add_rank(self, slot):
        print "unassigned: {}".format(self.unassigned_points)
        print "assigned: {}".format(self.assigned_points)
        
        if self.unassigned_points > 0:
            if slot.ranks < self.max_ranks:
                slot.ranks += 1
                self.unassigned_points -= 1
                self.assigned_points += 1
                
    def remove_rank(self, slot):
        print "Here"
        if slot.ranks > 0:
            self.unassigned_points += 1
            self.assigned_points -= 1
            slot.ranks -= 1
        print self.unassigned_points
            
    def make_rank_buttons(self):
        buttons = ButtonGroup()
        img = prepare.GFX["tinyarrow-up"]
        button_size = img.get_size()
        flipped = pg.transform.flip(img, False, True)
        for slot in self.slots.values():
            cx = slot.ranks_label.rect.right + 10
            y= slot.ranks_label.rect.centery + 1
            Button({"midbottom": (cx, y)}, buttons, idle_image=img,
                        call=self.add_rank, args=slot, button_size=button_size)
            Button({"midtop": (cx, y)}, buttons, idle_image=flipped,
                        call=self.remove_rank, args=slot, button_size=button_size)
        return buttons

    def distribute_default_skills(self):
        for skill in self.class_skills:
            ranks = self.slots[skill].ranks
            to_assign = min(self.unassigned_points, self.max_ranks - ranks)
            self.unassigned_points -= to_assign
            self.assigned_points += to_assign
            self.slots[skill].ranks += to_assign

    def get_synergy_bonuses(self):
        bonuses = {}
        for slot in self.slots.values():
            if slot.ranks > 4:
                if slot.name in SYNERGIES:
                    for skill in SYNERGIES[slot.name]:
                        if skill in bonuses:
                            bonuses[skill].append((slot.name, 2))
                        else:
                            bonuses[skill] = [(slot.name, 2)]
        return bonuses

    def get_feat_bonuses(self, feats_table):
        bonuses = {}
        for s in feats_table.selectors:
            if s.value != "Unselected":
                b = FEATS[s.value][1]
                if b is not None:
                    if "skills" in b:
                        for name, num in b["skills"]:
                            if name in bonuses:
                                bonuses[name] += num
                            else:
                                bonuses[name] = num
        return bonuses
                
    def update_abilities(self, ability_scores, race, char_class, level):
        #self.ability_scores = ability_scores
        for slot in self.slots.values():
            relative = SKILL_ABIL_MAP[slot.name]
            slot.abil_mod = ABIL_MODS[ability_scores[relative]]
        points = self.get_skill_points(ability_scores, race, char_class, level)
        current_points = self.unassigned_points + self.assigned_points
        if current_points != points:
            if points > self.unassigned_points + self.assigned_points:
                self.unassigned_points += points - current_points
            else:
                to_remove = current_points - points
                if to_remove <= self.unassigned_points:
                    self.unassigned -= to_remove
                else:
                    to_remove -= self.unassigned_points
                    self.unassigned_points = 0                    
                    removing = True
                    while removing:
                        for skill in CLASS_SKILLS[char_class]:
                            slot = self.slots[skill]
                            if not to_remove:
                                removing = False
                                break
                            if slot.ranks > 0:
                                slot.ranks -= 1
                                self.assigned_points -= 1
                                to_remove -= 1
                            
            #self.assigned_points = 0
            #self.distribute_default_skills()
    
    def get_skill_points(self, ability_scores, race, char_class, level):
        points_per_level = SKILL_POINTS_PER_LEVEL[char_class]
        #print race
        if race == "Human":
            points_per_level += 1
        points_per_level += ABIL_MODS[ability_scores["Int"]]
        points = points_per_level * 4
        points += points_per_level * (level - 1)
        return points

    def get_event(self, event):
        self.buttons.get_event(event)
        
    def update(self, scaled_mouse, ability_scores, race, char_class, level, feats_table):
        self.buttons.update(scaled_mouse)
        self.update_abilities(ability_scores, race, char_class, level)
        syn_bonuses = self.get_synergy_bonuses()
        feat_bonuses = self.get_feat_bonuses(feats_table)
        for slot in self.slots.values():
            if slot.name in syn_bonuses:
                slot.synergy_bonuses = syn_bonuses[slot.name]
            if slot.name in feat_bonuses:
                slot.feat_bonuses = feat_bonuses[slot.name]
            else:
                slot.feat_bonuses = 0            
        for s in self.slots.values():
            s.update()
        text = "Ranks {}/{}".format(self.assigned_points,
                    (self.unassigned_points+self.assigned_points))
        self.ranks_header.set_text(text)
        
    def draw(self, surface):
        for rect, color in self.bg_rects:
            pg.draw.rect(surface, color, rect)
        self.headers.draw(surface)
        for slot in self.slots.values():
            slot.draw(surface)
        self.buttons.draw(surface)


class SkillSlot(object):
    def __init__(self, topleft, name, abil_mod, cross_class, misc_mods):
        self.abil_mod = abil_mod
        self.ranks = 0
        self.feat_bonuses = 0
        self.name = name
        self.cross_class = cross_class
        self.misc_mods = misc_mods
        self.feat_mods = []
        style = {"text_color": COLORS["WHITE"], "font_size": 20}
        self.labels = pg.sprite.Group()
        left, top = topleft
        offsets = [375, 450, 530, 610]
        Label(name, {"topleft": topleft}, self.labels, text_color=ABIL_COLORS[SKILL_ABIL_MAP[name]], font_size=24)
        self.total_label = Label("{:+}".format(self.get_total()), {"topright": (left + offsets[0], top)}, self.labels, **style)
        self.abil_mod_label = Label("{:+}".format(self.abil_mod), {"topright": (left + offsets[1], top)}, self.labels, **style)
        self.ranks_label = Label("{}".format(self.ranks), {"topright": (left + offsets[2], top)}, self.labels, **style)
        text = ", ".join(("+{} {}".format(m[1], m[0]) for m in self.misc_mods))
        self.misc_label = Label(text, {"topleft": (left + offsets[3], top)}, self.labels, **style)
        

    def get_total(self):
        total = self.ranks + self.abil_mod
        mods = self.misc_mods[:]
        mods.append(("Feats", self.feat_bonuses))
        for name, val in mods:
            total += val
        return total

    def update(self):
        self.total = self.get_total()
        self.total_label.set_text("{:+}".format(self.total))
        self.abil_mod_label.set_text("{:+}".format(self.abil_mod))
        ranks = "{}".format(self.ranks) if self.ranks else "-"
        self.ranks_label.set_text(ranks)
        mods = self.misc_mods[:]
        if self.feat_bonuses:
            mods.append(("Feat", self.feat_bonuses))
        text = ", ".join(("+{} {}".format(m[1], m[0]) for m in mods))
        self.misc_label.set_text(text)

    def draw(self, surface):
        self.labels.draw(surface)
