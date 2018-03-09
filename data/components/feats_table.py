from collections import OrderedDict, deque

import pygame as pg

from ..components.labels import Label
from ..components.info_tables import BASE_ATTACK
from ..components.ui_elements import Selector
#handle individually
#    Armor Proficiency
#    Improved Critical
#    Improved intiative
#    Improved Grapple
#    Skills bonuses
#    Save bonuses
#react to changes


FEATS = OrderedDict([
        ("Unselected", [None,
                    None,
                    ""]),
        ("Acrobatic", [None, 
                    {"skills": [("Jump", 2), ("Tumble", 2)]},
                    "Jump +2, Tumble +2"]),
        ("Agile", [None, 
                    {"skills": [("Balance", 2), ("Escape Artist", 2)]},
                    "Balance +2, Escape Artist +2"]),
        ("Alertness", [None, 
                    {"skills": [("Listen", 2), ("Spot", 2)]},
                    "Listen +2, Spot +2"]),
        ("Animal Affinity", [None, 
                    {"skills": [("Handle Animal", 2), ("Ride", 2)]},
                    "Handle Animal +2, Ride +2"]),
        ("Armor Proficiency (light)", [None,
                    None,
                    "No armor check penalty on attack rolls"]),
        ("Armor Proficiency (medium)", [{"feats":["Armor Proficiency (light)"]},
                    None,
                    "No armor check penalty on attack rolls"]),
        ("Armor Proficiency (heavy)", [{"feats":["Armor Proficiency (light)", "Armor Proficiency (medium)"]},
                    None,
                    "No armor check penalty on attack rolls"]),
        ("Athletic", [None,
                    {"skills": [("Climb", 2), ("Swim", 2)]},
                    "Climb +2, Swim +2"]),
        ("Augment Summoning", [{"feats":["Spell Focus (conjuration)"]},
                    None,
                    "Summoned creatures gain +4 Str, +4 Con"]),
        ("Blind-Fight", [None,
                    None,
                    "Reroll miss chance for concealment"]),
        ("Combat Casting", [None,
                    None,
                    "+4 Concentration for defensive casting"]),
        ("Combat Expertise", [{"abilities": [("Int", 13)]},
                    None,
                    "Trade attack bonus for AC (max 5)"]),
        ("Improved Disarm", [{"feats":["Combat Expertise"], "abilities": [("Int", 13)]},
                    None,
                    "+4 to disarm attempts, no attacks of opportunity"]),
        ("Improved Feint", [{"feats":["Combat Expertise"], "abilities": [("Int", 13)]},
                    None,
                    "Feint in combat as a move action"]),
        ("Improved Trip", [{"feats":["Combat Expertise"], "abilities": [("Int", 13)]},
                    None,
                    "+4 to trip attempts, no attacks of opportunity"]),
        ("Whirlwind Attack", [{"feats":["Combat Expertise", "Dodge", "Mobility", "Spring Attack"],   "abilities": [("Int", 13), ("Dex", 13)], "base attack": 4},
                    None,
                    "One melee attack against each opponent in reach"]),
        ("Combat Reflexes", [None,
                    None,
                    "Additional attacks of opportunity"]),
        ("Deceitful", [None,
                    {"skills": [("Disguise", 2), ("Forgery", 2)]},
                    "Disguise +2, Forgery +2"]),
        ("Deft Hands", [None,
                    {"skills": [("Sleight of Hand", 2), ("Use Rope", 2)]},
                    "Sleight of Hand +2, Use Rope +2"]),
        ("Diligent", [None,
                    {"skills": [("Appraise", 2), ("Decipher Script", 2)]},
                    "Appraise +2, Decipher Script +2"]),
        ("Dodge", [{"abilities": [("Dex", 13)]},
                    None,
                    "+1 AC vs selected target"]),
        ("Mobility", [{"feats":["Dodge"], "abilities": [("Dex", 13)]},
                    None,
                    "+4 AC vs some attacks of opportunity"]),
        ("Spring Attack", [{"feats":["Dodge", "Mobility"], "abilities": [("Dex", 13)], "base attack":  4},
                    None,
                    "Move before and after melee attack"]),
        ("Endurance", [None,
                    None,
                    "+4 checks and save vs non-lethal damage"]),
        ("Die Hard", [{"feats":["Endurance"]},
                    None,
                    "Remain conscious at -1 to -9 hp"]),
        ("Eschew Materials", [None,
                    None,
                    "Cast spells without material components"]),
        ("Exotic Weapon Proficiency", [{"base attack": 1},
                    None,
                    "No penalty on attacks with specific exotic weapon"]),
        ("Extra Turning", [{"class level": [("Cleric", 1), ("Paladin", 4)]},
                    None,
                    "Turn/rebuke 4 more times per day"]),
        ("Great Fortitude", [None,
                    {"saves": [("Fort", 2)]},
                    "+2 to Fortitude saves"]),
        ("Improved Counterspell", [None,
                    None,
                    "Counterspell with any spell of same school"]),
        ("Improved Critical", [{"base attack": 8},
                    None,
                    "Double threat range of weapon"]),
        ("Improved Initiative", [None,
                    {"initiative": 4},
                    "+4 bonus to Initiative"]),
        ("Improved Turning", [{"class level": [("Cleric", 1), ("Paladin", 4)]},
                    None,
                    "+1 to Turning checks"]),
        ("Improved Unarmed Strike", [None,
                    None,
                    "Considered armed when unarmed"]),
        ("Improved Grapple", [{"feats":["Improved Unarmed Strike"], "abilities": [("Dex", 13)]}, 
                    {"grapple": 4},
                    "+4 grapple, no attacks of opportunity"]),
        ("Deflect Arrows", [{"feats":["Improved Unarmed Strike"],  "abilities": [("Dex", 13)]},
                    None,
                    "Deflect one ranged attack per round"]),
        ("Snatch Arrows", [{"feats":["Improved Unarmed Strike", "Deflect Arrows"], "abilities": [("Dex", 15)]},
                    None,
                    "Catch a deflected range attack"]),
        ("Stunning Fist", [{"feats":["Improved Unarmed Strike"],  "abilities": [("Dex", 13), ("Wis", 13)], "base attack": 8},
                    None,
                    "Stun opponent with unarmed strike"]),
        ("Investigator", [None,
                    {"skills": [("Gather Information", 2), ("Search", 2)]},
                    "Gather Information +2, Search +2"]),
        ("Iron Will", [None,
                    {"saves": [("Will", 2)]},
                    "+2 Will saves"]),
        ("Leadership", [{"class level": [("Any", 6)]},
                    None,
                    "Attract cohorts and followers"]),
        ("Lightning Reflexes", [None,
                    {"saves": [("Ref", 2)]},
                    "+2 Reflex saves"]),
        ("Magical Aptitude", [None,
                    {"skills": [("Spellcraft", 2), ("Use Magic Device", 2)]},
                    "Spellcraft +2, Use Magic Device +2"]),
        ("Martial Weapon Proficiency", [None,
                    None,
                    "No penalty on attacks with martial specific martial weapon"]),
        ("Mounted Combat", [{"ranks": [("Ride", 1)]},
                    None,
                    "Negate hits on mount with Ride check"]),
        ("Mounted Archery", [{"feats":["Mounted Combat"], "ranks": [("Ride", 1)]}, 
                    None,
                    "Half penalty for mounted ranged attacks"]),
        ("Ride-By Attack", [{"feats":["Mounted Combat"], "ranks": [("Ride", 1)]},
                    None,
                    "Move before and after a mounted charge"]),
        ("Spirited Charge", [{"feats":["Mounted Combat", "Ride-By Attack"], "ranks": [("Ride", 1)]}, 
                    None,
                    "Double damge for mounted charges"]),
        ("Trample", [{"feats":["Mounted Combat"], "ranks": [("Ride", 1)]}, 
                    None,
                    "Target cannot avoid mounted overrun"]),
        ("Natural Spell", [{"abilities": [("Wis", 13)], "class level": [("Druid", 5)]},
                    None,
                    "Cast spells while in wild shape"]),            
        ("Negotiator", [None,
                    {"skills": [("Diplomacy", 2), ("Sense Motive", 2)]},
                    "Diplomacy +2, Sense Motive +2"]),
        ("Nimble Fingers", [None,
                    {"skills": [("Disable Device", 2), ("Open Lock", 2)]},
                    "Disable Device +2, Open Lock +2"]),
        ("Persuasive", [None,
                    {"skills": [("Bluff", 2), ("Intimidate", 2)]},
                    "Bluff +2, Intimidate +2"]),
        ("Point Blank Shot", [None,
                    None,
                    "+1 attack and damage for ranged attacks w/in 30"]),
        ("Far Shot", [{"feats":["Point Blank Shot"]},
                    None,
                    "Increase range increment 50% or 100%"]),
        ("Precise Shot", [{"feats":["Point Blank Shot"]},
                    None,
                    "'No -4 penalty firing into melee"]),
        ("Improved Precise Shot", [{"feats":["Point Blank Shot", "Precise Shot"], "abilities": [("Dex", 19)], "base attack": 11}, 
                    None,
                    "Ignore less than total cover/concealment"]),
        ("Rapid Shot", [{"feats":["Point Blank Shot"], "abilities": [("Dex", 13)]},
                    None,
                    "One extra ranged attack  each round"]),
        ("Manyshot", [{"feats":["Point Blank Shot", "Rapid Shot"], "base attack": 6},
                    None,
                    "Shoot two or more arrows simultaneously"]),
        ("Shot on the Run", [{"feats":["Point Blank Shot", "Dodge", "Mobility"], "abilities": [("Dex", 13)], "base attack": 4},
                    None,
                    "Move before and after ranged attack"]),
        ("Power Attack", [{"abilities": [("Str", 13)]},
                    None,
                    "Trade attack bonus for damage (up to base attack)"]),
        ("Cleave", [{"feats":["Power Attack"], "abilities": [("Str", 13)]}, 
                    None,
                    "Extra melee attack after dropping target"]),
        ("Great Cleave", [{"feats":["Power Attack", "Cleave"], "abilities": [("Str", 13)], "base attack": 4},
                    None,
                    "No limit to cleave attacks per round"]),
        ("Improved Bull Rush", [{"feats":["Power Attack"], "abilities": [("Str", 13)]}, 
                    None,
                    "+4 bull rush, no attacks of opportunity"]),
        ("Improved Overrun", [{"feats":["Power Attack"], "abilities": [("Str", 13)]}, 
                    None,
                    "+4 overrrun, no attacks of opportunity"]),
        ("Improved Sunder", [{"feats":["Power Attack"], "abilities": [("Str", 13)]}, 
                    None,
                    "+4 sunder, no attacks of opportunity"]),
        ("Quick Draw", [{"base attack": 1},
                    None,
                    "Draw weapon as free action"]),
        ("Rapid Reload", [None,
                    None,
                    "Reload crossbows more quickly"]),
        ("Run", [None,
                    None,
                    "Run at 5x normal speed, +4 Jump w/running start"]),
        ("Self-Sufficient", [None,
                    {"skills": [("Heal", 2), ("Survival", 2)]},
                    "Heal +2, Survival +2"]),
        ("Shield Proficiency", [None,
                    None,
                    "No armor check penalty on attacks"]),
        ("Improved Shield Bash", [{"feats": ["Shield Proficiency"]},
                    None,
                    "Retain shield bonus to AC when bashing"]),
        ("Tower Shield Proficiency", [{"feats": ["Shield Proficiency"]},
                    None,
                    "No armor check penalty on attack rolls"]),
        ("Simple Weapon Proficiency", [None,
                    None,
                    "No -4 penalty on attacks with simple weapons"]),
        ("Skill Focus", [None,
                    None,
                    "+3 bonus to selected skill"]),
        ("Spell Focus", [None,
                    None,
                    "+1 DC spells of specific school"]),
        ("Greater Spell Focus", [{"feats": ["Spell Focus"]},
                    None,
                    "+1 DC spells of specific school"]),
        ("Spell Mastery", [{"class level": [("Wizard", 1)]},
                    None,
                    "Can prepare some spells without a spellbook"]),
        ("Spell Penetration", [None,
                    None,
                    "+2 CL vs spell resistance"]),
        ("Greater Spell Penetration", [{"feats":["Spell Penetration"]},
                    None,
                    "+2 CL vs spell resistance"]),
        ("Stealthy", [None,
                    {"skills": [("Hide", 2), ("Move Silently", 2)]},
                    "Hide +2, Move Silently +2"]),
        ("Toughness", [None,
                    {"hit points": 3},
                    "+3 hit points"]),
        ("Track", [None,
                    None,
                    "Use Survival skill to track"]),
        ("Two-Weapon Fighting", [{"abilities": [("Dex", 15)]},
                    None,
                    "Reduce two-weapon fighting penalties"]),
        ("Two-Weapon Defense", [{"feats": ["Two-Weapon Fighting"], "abilities": [("Dex", 15)]},
                    None,
                    "Offhand weapon grants +1 shield bonus to AC"]),
        ("Improved Two-Weapon Fighting", [{"feats": ["Two-Weapon Fighting"],  "abilities": [("Dex", 17)], "base attack": 6},
                    None,
                    "Gain second offhand attack"]),
        ("Greater Two-Weapon Fighting", [{"feats": ["Two-Weapon Fighting", "Improved Two-Weapon Fighting"], "abilities": [("Dex", 19)], "base attack": 11},
                    None,
                    "Gain third offhand attack"]),
        ("Weapon Finesse", [{"base attack": 1},
                    None,
                    "Use Dex mod. on attacks with light weapons"]),
        ("Weapon Focus", [{"base attack": 1},
                    None,
                    "+1 attack with selected weapon"]),
        ("Weapon Specialization", [{"feats": ["Weapon Focus"], "class level": [("Fighter", 4)]},
                    None,
                    "+2 damage with selected weapon"]),
        ("Greater Weapon Focus", [{"feats": ["Weapon Focus"], "class level": [("Fighter", 8)]},
                    None,
                    "+1 attack with selected weapon"]),
        ("Greater Weapon Specialization", [{"feats": ["Weapon Specialization", "Greater Weapon Focus"], "class level": [("Fighter", 12)]},
                    None,
                    "+2 damage with selected weapon"]),
        ("Brew Potion", [{"class level": [("Wizard", 3), ("Cleric", 3), ("Druid", 3), ("Bard", 3), ("Ranger", 6)]},
                    None,
                    "Create magic potions"]),
        ("Craft Magic Arms and Armor", [{"class level": [("Wizard", 5), ("Cleric", 5), ("Druid", 5), ("Bard", 5), ("Ranger", 10)]},
                    None,
                    "Create magic arms, armor and shields"]),
        ("Craft Rod", [{"class level": [("Wizard", 9), ("Cleric", 9), ("Druid", 9), ("Bard", 9), ("Ranger", 18)]},
                    None,
                    "Create magic rods"]),
        ("Craft Staff", [{"class level": [("Wizard", 12), ("Cleric", 12), ("Druid", 12), ("Bard", 12), ("Ranger", 24)]},
                    None,
                    "Create magic staffs"]),
        ("Craft Wand", [{"class level": [("Wizard", 5), ("Cleric", 5), ("Druid", 5), ("Bard", 5), ("Ranger", 10)]},
                    None,
                    "Create magic wands"]),
        ("Craft Wondrous Item", [{"class level": [("Wizard", 3), ("Cleric", 3), ("Druid", 3), ("Bard", 3), ("Ranger", 6)]},
                    None,
                    "Create magic wondrous items"]),
        ("Forge Ring", [{"class level": [("Wizard", 12), ("Cleric", 12), ("Druid", 12), ("Bard", 12), ("Ranger", 24)]},
                    None,
                    "Create magic rings"]),
        ("Scribe Scroll", [{"class level": [("Wizard", 1), ("Cleric", 1), ("Druid", 1), ("Bard", 1), ("Ranger", 4)]},
                    None,
                    "Create magic scrolls"]),
        ("Empower Spell", [None,
                    None,
                    "Increase spell's variable, numeric effects 50%"]),
        ("Enlarge Spell", [None,
                    None,
                    "Double spell's range"]),
        ("Extend Spell", [None,
                    None,
                    "Double spell's duration"]),
        ("Heighten Spell", [None,
                    None,
                    "Cast spells as higher level"]),
        ("Maximize Spell", [None,
                    None,
                    "Maximize spell's variable, numeric effects"]),
        ("Quicken Spell", [None,
                    None,
                    "Cast spells as free action"]),
        ("Silent Spell", [None,
                    None,
                    "Cast spells without verbal components"]),
        ("Still Spell", [None,
                    None,
                    "Cast spells without somatic components"]),
        ("Widen Spell", [None,
                    None,
                    "Double spell's area"])
        ])     

WEAPON_SPECIFIC_FEATS = [
            "Exotic Weapon Proficiency", "Martial Weapon Proficiency", "Weapon Focus",
            "Weapon Specialization", "Greater Weapon Focus",
            "Greater Weapon Specialization", "Improved Critical"]

SCHOOL_SPECIFIC_FEATS = [
            "Spell Focus", "Grater Spell Focus"]

SKILL_SPECIFIC_FEATS = [
            "Skill Focus"]
            
WiZARD_BONUS_FEATS = ["Unselected", "Spell Mastery", "Brew Potion",
            "Craft Magic Arms and Armor", "Craft Rod", "Craft Staff",
            "Craft Wand", "Craft Wondrous Item", "Forge Ring", 
            "Scribe Scroll", "Empower Spell", "Enlarge Spell",
            "Extend Spell", "Heighten Spell", "Maximize Spell",
            "Quicken Spell", "Silent Spell", "Still Spell", "Widen Spell"]
            
FIGHTER_BONUS_FEATS = ["Unselected",
            "Blind-Fight","Combat Expertise","Improved Disarm","Improved Feint",
            "Improved Trip","Whirlwind Attack","Combat Reflexes","Dodge",
            "Mobility", "Spring Attack", "Exotic Weapon Proficiency",
            "Improved Critical", "Improved Initiative","Improved Unarmed Strike",
            "Improved Grapple","Deflect Arrows","Snatch Arrows","Stunning Fist",
            "Mounted Combat","Mounted Archery","Ride-By Attack","Spirited Charge",
            "Trample","Point Blank Shot","Far Shot","Precise Shot",
            "Improved Precise Shot","Rapid Shot","Manyshot","Shot on the Run",
            "Power Attack","Cleave","Great Cleave","Improved Bull Rush",
            "Improved Overrun","Improved Sunder","Quick Draw","Rapid Reload",
            "Improved Shield Bash","Two-Weapon Fighting","Two-Weapon Defense",
            "Improved Two-Weapon Fighting","Greater Two-Weapon Fighting",
            "Weapon Finesse","Weapon Focus","Weapon Specialization",
            "Greater Weapon Focus","Greater Weapon Specialization"]

            
class FeatsTable(object):
    def __init__(self, race, char_class, level, ability_scores):   
        base_attack = BASE_ATTACK[char_class][level - 1]    
        self.make_selectors(race, char_class, level, ability_scores, base_attack)
            
    def  make_selectors(self, race, char_class, level, ability_scores, base_attack):
        num_feats = 1 + (level // 3)
        bonus_feats = 0
        vert_space = 25
        if race == "Human":
            num_feats += 1
        left, top = 80, 560
        width = 160
        horiz_offset = 30
        bonus_feats = 0
        self.selectors = []
        if char_class == "Fighter":
            bonus_feats = 1 + (level // 2)
        elif char_class == "Wizard":
            bonus_feats = level // 5
        for b in range(bonus_feats):
            if char_class == "Fighter":
                feats = [x for x in FIGHTER_BONUS_FEATS
                            if self.validate_feat(x, race, char_class, level, ability_scores, base_attack)]
            elif char_class == "Wizard":
                feats = [x for x in WIZARD_BONUS_FEATS
                            if self.validate_feat(x, race, char_class, level, ability_scores, base_attack)]
            self.selectors.append(Selector("", (left, top), width, horiz_offset, feats))
            top += vert_space
        
        for x in range(num_feats):
            feat_names = [x for x in FEATS
                        if self.validate_feat(x, race, char_class, level, ability_scores, base_attack)]
            self.selectors.append(Selector("", (left, top), width, horiz_offset, feat_names))
            top += vert_space

    def validate_feat(self, feat_name, race, char_class, level, ability_scores, base_attack):
        current_feats = [selector.value for selector in self.selectors]
        if feat_name == "Unselected":
            return True
        prereqs = FEATS[feat_name][0]
        valid = True
        if prereqs is not None:
            if "feats" in prereqs:
                for f in prereqs["feats"]:
                    if f not in current_feats:
                        return False
            if "abilities" in prereqs:
                for abil, score in prereqs["abilities"]:
                    if ability_scores[abil] < score:
                        return False
            if "class level" in prereqs:
                valid_class = False
                for character_class, level_num in prereqs["class level"]:
                    if char_class == character_class and level >= level_num:
                        valid_class = True
                if not valid_class:
                    return False
            if "base attack" in prereqs:
                if base_attack < prereqs["base attack"]:
                    return False
        return True
        
    def get_event(self, event):
        for selector in self.selectors:
            selector.get_event(event)
        
    def update(self, scaled_mouse, race, char_class, level, ability_scores, base_attack):
        self.labels = pg.sprite.Group()
        
        for selector in self.selectors:
            val = selector.value
            other_feats = [s.value for s in self.selectors if s is not selector] 
            valid = [x for x in FEATS if self.validate_feat(x, race, char_class, level, ability_scores, base_attack)]
            if val not in valid:
                val = "Unselected"
            valid_feats = []
            for v in valid:
                if FEATS[v][0] is not None:
                    if "feats" in FEATS[v][0]:
                        if val in FEATS[v][0]["feats"]:
                            if val not in other_feats:
                                continue
                valid_feats.append(v)
                    
            
            selector.values = deque(valid_feats)
            selector.value = selector.values[0]
            #print "val: {}".format(val)
            #print "value: {}".format(selector.value)
            #print "values: {}".format(selector.values)
            if val not in selector.values:
                val = "Unselected"
                selector.value = selector.values[0]
            while selector.value != val:
                selector.values.rotate(-1)
                selector.value = selector.values[0]
            selector.update(scaled_mouse)
            text = FEATS[selector.value][2]
            rect = selector.name_label.rect
            Label(text, {"midleft": (rect.centerx + 180, rect.centery)}, self.labels)
            
    def draw(self, surface):
        for s in self.selectors:
            s.draw(surface)
        self.labels.draw(surface)
            
            