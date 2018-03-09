from random import randint

import pygame as pg

from .. import prepare
from ..components.labels import Label, Textbox, Button, ButtonGroup
from ..components.ui_elements import Selector, Incrementor, FillableForm
from ..components.abilities_table import AbilitiesTable
from ..components.skills_table import SkillsTable
from ..components.feats_table import FeatsTable, FEATS
from ..components.saves_table import SavesTable
from ..components.name_generator import generate_name
from ..components.info_tables import (RACES, CLASSES, HIT_DICE_BY_CLASS,
            ABIL_MODS, BASE_ATTACK, ARMOR, ARMOR_NAMES, SHIELDS, SHIELD_NAMES,
            LEVEL_XP, STARTING_GOLD_DICE, RACE_INFO, WEAPONS, WEAPON_NAMES, COLORS, SAVING_THROWS)


CHARACTER_SHEET = { #OrderedDict([
        "Name": generate_name()}


class CharacterGenerator(object):
    def __init__(self):
        self.namebox = Textbox({"topleft": (0, 20)}, **{"fill_color": "gray10", "outline_color": "gray15", "box_size": (300, 30)})
        self.random_name()
        self.labels = pg.sprite.Group()
        self.namebox_title = Label("Character Name", {"midtop": (150, -4)}, self.labels, font_size=18)
        self.abilities_table_topleft = (0, 200)
        self.abilities_table = AbilitiesTable(self.abilities_table_topleft)
        self.selectors = self.make_selectors()
        self.incrementors = self.make_incrementors()
        self.skills_table_topleft = (1155, 10)

        race, char_class, level = (self.selectors["Race"].value,
                    self.selectors["Class"].value,
                    self.incrementors["Level"].value)
        self.skills_table = SkillsTable(self.skills_table_topleft, race,
                    char_class, level, self.abilities_table)
        ability_scores = {name: slot.score
                    for name, slot in self.abilities_table.slots.items()}            
        self.feats_table = FeatsTable(race, char_class, level, ability_scores)         
        self.saves_table = SavesTable((860, 0))
        
        self.previous = {"Race": race, "Class": char_class, "Level": level}
        self.buttons = ButtonGroup()
        Button({"midtop": (130, 480)}, self.buttons, text="Reroll",
                    fill_color="gray20", font_size=16, button_size=(120, 18),
                    call=self.reroll)
        Button({"midtop": (150, 60)}, self.buttons, text="Random Name",
                    fill_color="gray20", font_size=16, call=self.random_name,
                    button_size=(120, 18))
        self.hp_roll = self.generate_hp_roll(char_class, level)
        self.starting_gold = self.generate_starting_gold(char_class, level)
        self.derivative_labels = self.make_derivative_labels()
        cxs = [540, 630, 730]
        top = 215
        Label("Weapon", {"midtop": (400, top)}, self.labels, font_size=16,
                    text_color=COLORS["WHITE"])
        Label("Attack", {"midtop": (cxs[0], top)}, self.labels, font_size=16,
                    text_color=COLORS["WHITE"])
        Label("Damage", {"midtop": (cxs[1], top)}, self.labels, font_size=16,
                    text_color=COLORS["WHITE"])
        Label("Critical", {"midtop": (cxs[2], top)}, self.labels, font_size=16,
                    text_color=COLORS["WHITE"])

    def random_name(self, *args):
        self.namebox.buffer = generate_name()
        self.namebox.buffer_index = len(self.namebox.buffer)

    def reroll(self, *args):
        self.abilities_table = AbilitiesTable(self.abilities_table_topleft)
        self.skills_table = SkillsTable(self.skills_table_topleft,
                    self.selectors["Race"].value,
                    self.selectors["Class"].value,
                    self.incrementors["Level"].value,
                    self.abilities_table)

    def make_selectors(self):
        selectors = {
            "Race": Selector("Race", (5, 100), 80, 180, RACES),
            "Class": Selector("Class", (5, 130), 80, 180, CLASSES),
            "Armor": Selector("Armor", (320, 80), 100, 160, ARMOR_NAMES),
            "Shield": Selector("Shield", (580, 80), 100, 160, SHIELD_NAMES),
            "Weapon 1": Selector("", (350, 260), 100, 50, WEAPON_NAMES),
            "Weapon 2": Selector("", (350, 290), 100, 50, WEAPON_NAMES),
            "Weapon 3": Selector("", (350, 320), 100, 50, WEAPON_NAMES),
            "Weapon 4": Selector("", (350, 350), 100, 50, WEAPON_NAMES),
            "Weapon 5": Selector("", (350, 380), 100, 50, WEAPON_NAMES),
            "Weapon 6": Selector("", (350, 410), 100, 50, WEAPON_NAMES),
            "Weapon 7": Selector("", (350, 440), 100, 50, WEAPON_NAMES),
            "Weapon 8": Selector("", (350, 470), 100, 50, WEAPON_NAMES),
            }
        return selectors

    def make_incrementors(self):
        incrementors = {
            "Level": Incrementor("Level", (5, 160), 80, 180, 1, 1, 20)
            }
        return incrementors

    def get_event(self, event, scale):
        self.buttons.get_event(event)
        self.namebox.get_event(event)
        for selector in self.selectors.values():
            selector.get_event(event)
        for incrementor in self.incrementors.values():
            incrementor.get_event(event)
        self.abilities_table.get_event(event, scale)
        self.skills_table.get_event(event)
        self.feats_table.get_event(event)

    def make_derivative_labels(self):
        labels = {}
        info = [
                #("Armor Bonus",

                ("Armor Class", (320, 100)),
                ("Flat-footed", (425, 100)),
                ("Touch AC", (530, 100)),
                ("Check Penalty", (610, 100)),
                ("Spell Failure", (720, 100)),
                
                ("Base Attack", (390, 150)),
                ("Base Melee", (500, 150)),
                ("Base Ranged", (610, 150)),
                ("Grapple", (720, 150)),
                
                ("Hit Points", (315, 5)),
                ("Initiative", (400, 5)),
                ("Size", (495, 5)),
                ("Speed", (555, 5)),
                ("Experience", (645, 5)),
                ("Gold", (765, 5))
                ]
        for name, topleft in info:
            title = Label("{}".format(name), {"topleft": topleft}, self.labels, font_size=16)
            val_label = Label("", {"midtop": title.rect.midbottom}, self.labels)
            labels[name] = val_label
        
        Label("Feats", {"midtop": (100, 510)}, self.labels, font_size=20)
        cxs = [540, 630, 730]
        for x in range(1, 9):
            weapon_name = "Weapon {}".format(x)
            selector = self.selectors[weapon_name]
            val_label = selector.value_label
            for stat, cx in zip(["attack", "damage", "critical"], cxs):
                stat_name = "{} {}".format(weapon_name, stat)
                stat_label = Label("", {"center": (cx, val_label.rect.centery)}, self.labels)
                labels[stat_name] = stat_label        
        return labels

    def update(self, dt, scale):
        mx, my =  pg.mouse.get_pos()
        scaled = int(mx * scale[0]), int(my * scale[1])

        race = self.selectors["Race"].value
        char_class = self.selectors["Class"].value
        level = self.incrementors["Level"].value

        self.buttons.update(scaled)
        self.namebox.update(dt)
        for selector in self.selectors.values():
            selector.update(scaled)
        for incrementor in self.incrementors.values():
            incrementor.update(scaled)
        self.update_values()
        ability_scores = {name: slot.score
                    for name, slot in self.abilities_table.slots.items()}
        self.skills_table.update(scaled, ability_scores, race, char_class, level, self.feats_table)
        self.abilities_table.update(scaled, race)
        ba = BASE_ATTACK[char_class][level - 1]
        try:
            base_attack = ba[0]
        except TypeError:
            base_attack = ba
        self.feats_table.update(scaled, race, char_class, level, ability_scores, base_attack)
        self.saves_table.update(race, char_class, level, ability_scores, self.feats_table)
        
    def generate_hp_roll(self, char_class, level):
        hit_die = HIT_DICE_BY_CLASS[char_class]
        hp_roll = hit_die + sum(
                    (randint(1, hit_die) for _ in range(level - 1)))
        return hp_roll

    def update_derivatives(self,race, char_class, level):
        d = self.derivative_labels
        size, speed = RACE_INFO[race]
        dex = ABIL_MODS[self.abilities_table.slots["Dex"].score]
        str = ABIL_MODS[self.abilities_table.slots["Str"].score]
        con = ABIL_MODS[self.abilities_table.slots["Con"].score]
        wis = ABIL_MODS[self.abilities_table.slots["Wis"].score]
        bonus_hp = con * level
        hp = self.hp_roll + bonus_hp
        initiative = dex # + FEATS
        armor = ARMOR[self.selectors["Armor"].value]
        shield = SHIELDS[self.selectors["Shield"].value]
        armor_bonus = armor[1]
        size_bonus = 1 if size == "Small" else 0
        adj_dex = min(dex, min(armor[2], shield[2]))
        spell_failure = armor[4] + shield[4]
        penalty = armor[3] + shield[3]
        ac = 10 + adj_dex + armor_bonus + size_bonus
        ffac = 10 + armor_bonus + size_bonus
        touch = 10 + adj_dex + size_bonus
        gold = self.starting_gold - self.get_expenses(armor, shield)
        xp = LEVEL_XP[level]
        d["Armor Class"].set_text("{}".format(ac))
        d["Flat-footed"].set_text("{}".format(ffac))
        d["Touch AC"].set_text("{}".format(touch))
        d["Check Penalty"].set_text("{:+}".format(penalty))
        d["Spell Failure"].set_text("{}%".format(spell_failure))
        d["Hit Points"].set_text("{}".format(hp))
        d["Initiative"].set_text("{:+}".format(initiative))
        d["Size"].set_text("{}".format(size))
        d["Speed"].set_text("{}".format(speed))
        d["Experience"].set_text("{:,}".format(xp))
        d["Gold"].set_text("{}".format(gold))

        
        
        
        
        
        base_attacks = BASE_ATTACK[char_class][level - 1]
        try:
            ba_string = "/".join(("{:+}".format(attack) for attack in base_attacks))
        except TypeError:
            ba_string = "{:+}".format(base_attacks)
            base_attacks = [base_attacks]
        base_melee = "/".join(("{:+}".format(att + str) for att in base_attacks))
        base_ranged = "/".join(("{:+}".format(att + dex) for att in base_attacks))
        size_mod = -4 if size == "Small" else 0
        grapple = base_attacks[0] + str + size_mod
        d["Base Attack"].set_text("{}".format(ba_string))
        d["Base Melee"].set_text("{}".format(base_melee))
        d["Base Ranged"].set_text("{}".format(base_ranged))
        d["Grapple"].set_text("{}".format(grapple))

        for x in range(1, 5):
            n = "Weapon {}".format(x)
            weapon_name = self.selectors[n].value
            weapon = WEAPONS[weapon_name]
            weap_type, sm_dmg, med_dmg, crit = weapon[:4]
            damage = sm_dmg if size == "Small" else med_dmg
            if weap_type == "Melee":
                att = "/".join(("{:+}".format(att + str) for att in base_attacks))
                if str != 0:
                    damage += "+{}".format(str)
            else:
               att = "/".join(("{:+}".format(att + dex) for att in base_attacks))
            #CHECK FOR WEAPON FEATS

            d["{} attack".format(n)].set_text(att)
            d["{} damage".format(n)].set_text(damage)
            try:
                d["{} critical".format(n)].set_text(crit)
            except:
                print crit
                
    def get_expenses(self, armor, shield): #, weapons):
        total = 0
        total += armor[6]
        total += shield[6]
        #for weapon in weapons:
        #    weapon[]
        return total

    def generate_starting_gold(self, char_class, level):
        num_dice = STARTING_GOLD_DICE[char_class]
        total = sum((randint(1, 4) for _ in range(num_dice)))
        if char_class != "Monk":
            total *= 10
        return total

    def update_values(self):
        char_class = self.selectors["Class"].value
        race = self.selectors["Race"].value
        level = self.incrementors["Level"].value
        self.update_derivatives(race, char_class, level)


        changed = {
                    "Class": self.previous["Class"] != char_class,
                    "Race": self.previous["Race"] != race,
                    "Level": self.previous["Level"] != level}
        if any(changed.values()):
            self.skills_table = SkillsTable(self.skills_table_topleft, race, char_class, level, self.abilities_table)
            self.hp_roll = self.generate_hp_roll(char_class, level)
            ability_scores = {name: slot.score
                    for name, slot in self.abilities_table.slots.items()}
            self.feats_table = FeatsTable(race, char_class, level, ability_scores)
        if changed["Class"]:
            self.starting_gold = self.generate_starting_gold(char_class, level)

        self.previous = {
            "Race": race,
            "Class": char_class,
            "Level": level}

    def draw(self, surface):
        self.labels.draw(surface)
        self.namebox.draw(surface)
        self.abilities_table.draw(surface)
        self.feats_table.draw(surface)
        for selector in self.selectors.values():
            selector.draw(surface)
        for incrementor in self.incrementors.values():
            incrementor.draw(surface)
        self.skills_table.draw(surface)
        self.saves_table.draw(surface)
        self.buttons.draw(surface)
