import pygame as pg

from ..components.labels import Label
from ..components.info_tables import SAVING_THROWS, ABIL_MODS
from ..components.feats_table import FEATS


class SavesTable(object):
    def __init__(self, topleft):
        self.labels = pg.sprite.Group()
        labels = {}
        left, top = topleft
        top1, top2, top3 = top + 40, top + 70, top + 100
        right1, right2, right3, right4 = left + 65, left + 125, left + 185, left + 245
        
        Label("Fort", {"midleft": (left + 5, top1)}, self.labels, font_size=16)
        Label("Ref", {"midleft": (left + 5, top2)}, self.labels, font_size=16)
        Label("Will", {"midleft": (left + 5, top3)}, self.labels, font_size=16)
        Label("Saving Throws", {"midtop": (left + 100, top)}, self.labels, font_size=18)
        Label("Total", {"midtop": (right1, top1 - 20)}, self.labels)
        Label("Base Save", {"midtop": (right2, top1 - 20)}, self.labels)
        Label("Abil Mod", {"midtop": (right3, top1 - 20)}, self.labels)
        
        labels["Fort"] = Label("", {"midright": (right1, top1)}, self.labels)
        labels["base Fort"] = Label("",  {"midright": (right2, top1)}, self.labels)
        labels["Fort abil"] = Label("",  {"midright": (right3, top1)}, self.labels)
        labels["Fort mods"] = Label("",  {"midright": (right4, top1)}, self.labels)
        
        labels["Ref"] = Label("", {"midright": (right1, top2)}, self.labels)
        labels["base Ref"] = Label("", {"midright": (right2, top2)}, self.labels)
        labels["Ref abil"] = Label("", {"midright": (right3, top2)}, self.labels)
        labels["Ref mods"] = Label("", {"midright": (right4, top2)}, self.labels)

        labels["Will"] = Label("",  {"midright": (right1, top3)}, self.labels)
        labels["base Will"] = Label("", {"midright": (right2, top3)}, self.labels)
        labels["Will abil"] = Label("", {"midright": (right3, top3)}, self.labels)
        labels["Will mods"] = Label("", {"midright": (right4, top3)}, self.labels)
        self.derivative_labels = labels
        
    def update(self, race, char_class, level, ability_scores, feats_table):
        d = self.derivative_labels
        dex = ABIL_MODS[ability_scores["Dex"]]
        con = ABIL_MODS[ability_scores["Con"]]
        wis = ABIL_MODS[ability_scores["Wis"]]
        fort, ref, will = SAVING_THROWS[char_class][level]
        d["base Fort"].set_text("{:+}".format(fort))
        d["base Ref"].set_text("{:+}".format(ref))
        d["base Will"].set_text("{:+}".format(will))
        if race == "Halfling":
            fort += 1
            ref += 1
            will += 1
        fort += con
        ref += dex
        will += wis
        feat_mods = {"Fort": 0, "Ref": 0, "Will": 0}
        for s in feats_table.selectors:
            bonuses = FEATS[s.value][1]
            if bonuses is not None and "saves" in bonuses:
                for save_name, val in bonuses["saves"]:
                    feat_mods[save_name] += val
        fort += feat_mods["Fort"]                                
        ref += feat_mods["Ref"]                                
        will += feat_mods["Will"]                                
                    
        d["Fort"].set_text("{:+}".format(fort))
        d["Fort abil"].set_text("{:+}".format(con))
        fort_text = "+{} Feats".format(feat_mods["Fort"]) if feat_mods["Fort"] else ""
        d["Fort mods"].set_text(fort_text)
        d["Ref"].set_text("{:+}".format(ref))
        d["Ref abil"].set_text("{:+}".format(dex))
        ref_text = "+{} Feats".format(feat_mods["Ref"]) if feat_mods["Ref"] else ""
        d["Ref mods"].set_text(ref_text)
        d["Will"].set_text("{:+}".format(will))
        d["Will abil"].set_text("{:+}".format(wis))
        will_text = "+{} Feats".format(feat_mods["Will"]) if feat_mods["Will"] else ""
        d["Will mods"].set_text(will_text)
        
    def draw(self, surface):
        self.labels.draw(surface)
        