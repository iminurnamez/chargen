ABIL_MODS = {x: (x // 2) - 5 for x in range(3, 45)}


ARMOR_NAMES = [
        "None", "Padded", "Leather", "Studded leather", "Chain shirt", "Hide",
        "Scale mail",  "Chainmail", "Breastplate", "Splint mail",
        "Banded mail","Half-plate", "Full plate"]


ARMOR = {
       #             Type  Bonus, Max Dex, Check Penalty, Spell Failure, Weight, Price
        "None": ("Light", 0, 20, 0, 0, 0, 0),         
        "Padded": ("Light", 1, 8, 0, 5, 10, 5),
        "Leather": ("Light", 2, 6, 0, 10, 15, 10),
        "Studded leather": ("Light", 3, 5, -1, 15, 20, 25),
        "Chain shirt": ("Light", 4, 4, -2, 20, 25, 100),
        "Hide": ("Medium", 3, 4, -3, 20, 25, 15),
        "Scale mail": ("Medium", 4, 3, -4, 25, 30, 50),
        "Chainmail": ("Medium", 5, 2, -5, 30, 40, 150),
        "Breastplate": ("Medium", 5, 3, -4, 25, 30, 200),
        "Splint mail": ("Heavy", 6, 0, -7, 40, 45, 200),
        "Banded mail": ("Heavy", 6, 1, -6, 35, 35, 250),
        "Half-plate": ("Heavy", 7, 0, -7, 40, 50, 600),
        "Full plate": ("Heavy", 8, 1, -6, 35, 50, 1500)
        }


BASE_ATTACK = {
    "Barbarian": [1,2,3,4,5,(6,1),(7,2),(8,3),(9,4),(10,5),(11,6,1),(12,7,2),(13,8,3),(14,9,4),(15,10,5),(16,11,6,1),(17,12,7,2),(18,13,8,3),(19,14,9,4),(20,15,10,5)],
    "Bard": [0,1,2,3,3,4,5,(6,1),(6,1),(7,2),(8,3),(9,4),(9,4),(10,5),(11,6,1),(12,7,2),(12,7,2),(13,8,3),(14,9,4),(15,10,5)],
    "Cleric": [0,1,2,3,3,4,5,(6,1),(6,1),(7,2),(8,3),(9,4),(9,4),(10,5),(11,6,1),(12,7,2),(12,7,2),(13,8,3),(14,9,4),(15,10,5)],
    "Druid": [0,1,2,3,3,4,5,(6,1),(6,1),(7,2),(8,3),(9,4),(9,4),(10,5),(11,6,1),(12,7,2),(12,7,2),(13,8,3),(14,9,4),(15,10,5)],
    "Fighter": [1,2,3,4,5,(6,1),(7,2),(8,3),(9,4),(10,5),(11,6,1),(12,7,2),(13,8,3),(14,9,4),(15,10,5),(16,11,6,1),(17,12,7,2),(18,13,8,3),(19,14,9,4),(20,15,10,5)],
    "Monk": [0,1,2,3,3,4,5,(6,1),(6,1),(7,2),(8,3),(9,4),(9,4),(10,5),(11,6,1),(12,7,2),(12,7,2),(13,8,3),(14,9,4),(15,10,5)],
    "Paladin": [1,2,3,4,5,(6,1),(7,2),(8,3),(9,4),(10,5),(11,6,1),(12,7,2),(13,8,3),(14,9,4),(15,10,5),(16,11,6,1),(17,12,7,2),(18,13,8,3),(19,14,9,4),(20,15,10,5)],
    "Ranger": [1,2,3,4,5,(6,1),(7,2),(8,3),(9,4),(10,5),(11,6,1),(12,7,2),(13,8,3),(14,9,4),(15,10,5),(16,11,6,1),(17,12,7,2),(18,13,8,3),(19,14,9,4),(20,15,10,5)],
    "Rogue": [0,1,2,3,3,4,5,(6,1),(6,1),(7,2),(8,3),(9,4),(9,4),(10,5),(11,6,1),(12,7,2),(12,7,2),(13,8,3),(14,9,4),(15,10,5)],
    "Sorcerer": [0,1,1,2,2,3,3,4,4,5,5,(6,1),(6,1),(7,2),(7,2),(8,3),(8,3),(9,4),(9,4),(10,5)],
    "Wizard": [0,1,1,2,2,3,3,4,4,5,5,(6,1),(6,1),(7,2),(7,2),(8,3),(8,3),(9,4),(9,4),(10,5)]
    }


CLASSES = ["Fighter","Ranger","Barbarian","Monk","Paladin","Wizard",
            "Sorcerer","Cleric","Druid","Rogue","Bard"]

CLASS_SKILLS = {
    "Fighter": ["Jump", "Ride", "Climb",  "Swim", "Intimidate",
                "Craft", "Handle Animal"],
    "Ranger": ["Hide",  "Move Silently", "Spot", "Listen", "Survival", "Search",
                "Ride", "Climb", "Jump", "Handle Animal", "Swim", "Use Rope",
                "Knowledge(nature)", "Knowledge(dungeoneering)",
                "Knowledge(geography)", "Concentration", "Craft",
                "Heal", "Profession"],
    "Barbarian": ["Jump", "Climb", "Listen", "Intimidate", "Survival",
                "Handle Animal",  "Ride", "Swim", "Craft"],
    "Paladin": ["Concentration", "Knowledge(religion)", "Diplomacy", "Ride",
                "Sense Motive", "Handle Animal", "Heal",
                "Knowledge(nobility)", "Craft", "Profession"],
    "Wizard": ["Spellcraft", "Concentration", "Decipher Script",
                "Knowledge(arcana)", "Knowledge(local)",
                "Knowledge(the planes)", "Knowledge(dungeoneering)",
                "Knowledge(geography)",
                "Knowledge(egineering)",
                "Knowledge(religion)", "Knowledge(nobility)",
                "Knowledge(nature)", "Craft", "Profession"],
    "Sorcerer": ["Spellcraft", "Concentration", "Bluff",  "Knowledge(arcana)",
                "Craft", "Profession"],
    "Cleric": ["Heal", "Spellcraft", "Concentration", "Knowledge(religion)",
                "Knowledge(the planes)", "Diplomacy", "Knowledge(arcana)",
                "Knowledge(history)", "Craft", "Profession"],
    "Druid": ["Spellcraft", "Concentration", "Listen", "Spot", "Heal",
                "Survival", "Knowledge(nature)", "Diplomacy", "Handle Animal",
                "Ride", "Swim", "Craft", "Profession"],
    "Monk": [ "Tumble", "Escape Artist", "Move Silently", "Balance", "Climb",
                "Jump", "Listen", "Spot", "Hide", "Sense Motive", "Swim",
                "Concentration", "Diplomacy", "Knowledge(religion)",
                "Knowledge(arcana)", "Perform", "Craft", "Profession"],
    "Rogue": ["Hide", "Move Silently", "Open Lock", "Climb", "Search",
                "Listen", "Disable Device",  "Spot", "Use Rope", "Jump",
                "Gather Information", "Appraise", "Balance", "Bluff",
                "Decipher Script", "Diplomacy", "Disguise", "Escape Artist",
                "Tumble", "Sleight of Hand", "Forgery", "Intimidate",
                "Knowledge(local)", "Perform", "Profession", "Sense Motive",
                "Swim", "Use Magic Device"],
    "Bard": ["Perform", "Gather Information", "Knowledge(local)", "Diplomacy",
                "Sense Motive", "Sleight of Hand", "Search", "Hide",
                "Move Silently", "Appraise", "Balance", "Bluff", "Climb",
                "Concentration", "Decipher Script",
                "Knowledge(nobility)", "Disguise", "Escape Artist",
                "Jump", "Listen", "Knowledge(arcana)",
                "Knowledge(dungeoneering)", "Knowledge(geography)",
                 "Knowledge(egineering)",
                 "Knowledge(religion)","Knowledge(nature)",
                 "Speak Language", "Spellcraft", "Swim", "Tumble",
                 "Use Magic Device", "Craft", "Profession"]
    }

    
COLORS = {
    "CYAN": (81, 163, 157),
    "BLUE": (6, 66, 92),
    "PURPLE": (129, 67, 116),
    "RED": (183, 105, 92),
    "YELLOW": (205, 187, 121),
   "WHITE": (242, 242, 242),
   "GREEN": (121, 205, 145)
   }

   
ABIL_COLORS = {
    "Str": COLORS["RED"],
    "Dex": COLORS["PURPLE"],
    "Con": COLORS["BLUE"],
    "Int": COLORS["CYAN"],
    "Wis": COLORS["GREEN"],
    "Cha": COLORS["YELLOW"]
    }
    
    
HIT_DICE_BY_CLASS = {
        "Fighter": 10,
        "Ranger": 8,
        "Barbarian": 4,
        "Monk": 8,
        "Paladin": 10,
        "Wizard": 4,
        "Sorcerer": 4,
        "Cleric": 8,
        "Druid": 8,
        "Rogue": 6,
        "Bard": 6}


LEVEL_XP = {}
total = 0
for x in range(1, 21):
    LEVEL_XP[x] = total
    total += x * 1000
            
        
RACES = ["Human", "Dwarf", "Elf", "Gnome", "Halfling", "Half-Orc", "Half-Elf"]


RACE_INFO = {
        #              size, speed, 
        "Human": ("Medium", 30),
        "Dwarf": ("Medium", 20),
        "Elf": ("Medium", 30),
        "Gnome": ("Small", 20),
        "Halfling": ("Small", 20),
        "Half-Orc": ("Medium", 30),
        "Half-Elf": ("Medium", 30)
        }
        

RACIAL_ABIL_MODS = {
    "Elf": {"Dex": 2, "Con": -2},
    "Dwarf": {"Con": 2, "Cha": -2},
    "Gnome": {"Con": 2, "Str": -2},
    "Halfling": {"Dex": 2, "Str": -2},
    "Half-Orc": {"Str": 2, "Int": -2, "Cha": -2}}

    
RACIAL_SKILL_BONUSES = {
    "Elf": {"Listen": 2, "Search": 2, "Spot": 2},
    "Gnome": {"Listen": 2, "Craft(alchemy)": 2},
    "Halfling": {"Hide": 4, "Climb": 2, "Jump": 2, "Move Silently": 2, "Listen": 2},
    "Half-Elf": {"Listen": 1, "Search": 1, "Spot": 1, "Diplomacy": 2, "Gather Information": 2}
    }
    

SKILL_POINTS_PER_LEVEL = {
        "Fighter": 2,
        "Ranger": 6,
        "Barbarian": 4,
        "Monk": 4,
        "Paladin": 2,
        "Wizard": 2,
        "Sorcerer": 2,
        "Cleric": 2,
        "Druid": 4,
        "Rogue": 8,
        "Bard": 6}
    
    
SAVING_THROWS = {
    # num of d4s, all but monk multiply result by 10
    "Fighter": [(2, 0, 0), (3, 0, 0), (3, 1, 1), (4, 1, 1), (4, 1, 1), (5, 2, 2), (5, 2, 2), (6, 2, 2), (6, 3, 3), (7, 3, 3), (7, 3, 3), (8, 4, 4), (8, 4, 4), (9, 4, 4), (9, 5, 5), (10, 5, 5), (10, 5, 5), (11, 6, 6), (11, 6, 6), (12, 6, 6)],
    "Ranger": [(2, 2, 0), (3, 3, 0), (3, 3, 1), (4, 4, 1), (4, 4, 1), (5, 5, 2), (5, 5, 2), (6, 6, 2), (6, 6, 3), (7, 7, 3), (7, 7, 3), (8, 8, 4), (8, 8, 4), (9, 9, 4), (9, 9, 5), (10, 10, 5), (10, 10, 5), (11, 11, 6), (11, 11, 6), (12, 12, 6)],
    "Barbarian": [(2, 0, 0), (3, 0, 0), (3, 1, 1), (4, 1, 1), (4, 1, 1), (5, 2, 2), (5, 2, 2), (6, 2, 2), (6, 3, 3), (7, 3, 3), (7, 3, 3), (8, 4, 4), (8, 4, 4), (9, 4, 4), (9, 5, 5), (10, 5, 5), (10, 5, 5), (11, 6, 6), (11, 6, 6), (12, 6, 6)],
    "Monk": [(2, 2, 2), (3, 3, 3), (3, 3, 3), (4, 4, 4), (4, 4, 4), (5, 5, 5), (5, 5, 5), (6, 6, 6), (6, 6, 6), (7, 7, 7), (7, 7, 7), (8, 8, 8), (8, 8, 8), (9, 9, 9), (9, 9, 9), (10, 10, 10), (10, 10, 10), (11, 11, 11), (11, 11, 11), (12, 12, 12)],
    "Paladin": [(2, 0, 0), (3, 0, 0), (3, 1, 1), (4, 1, 1), (4, 1, 1), (5, 2, 2), (5, 2, 2), (6, 2, 2), (6, 3, 3), (7, 3, 3), (7, 3, 3), (8, 4, 4), (8, 4, 4), (9, 4, 4), (9, 5, 5), (10, 5, 5), (10, 5, 5), (11, 6, 6), (11, 6, 6), (12, 6, 6)],
    "Wizard": [(0, 0, 2), (0, 0, 3), (1, 1, 3), (1, 1, 4), (1, 1, 4), (2, 2, 5), (2, 2, 5), (2, 2, 6), (3, 3, 6), (3, 3, 7), (3, 3, 7), (4, 4, 8), (4, 4, 8), (4, 4, 9), (5, 5, 9), (5, 5, 10), (5, 5, 10), (6, 6, 11), (6, 6, 11), (6, 6, 12)],
    "Sorcerer": [(0, 0, 2), (0, 0, 3), (1, 1, 3), (1, 1, 4), (1, 1, 4), (2, 2, 5), (2, 2, 5), (2, 2, 6), (3, 3, 6), (3, 3, 7), (3, 3, 7), (4, 4, 8), (4, 4, 8), (4, 4, 9), (5, 5, 9), (5, 5, 10), (5, 5, 10), (6, 6, 11), (6, 6, 11), (6, 6, 12)],
    "Cleric": [(2, 0, 2), (3, 0, 3), (3, 1, 3), (4, 1, 4), (4, 1, 4), (5, 2, 5), (5, 2, 5), (6, 2, 6), (6, 3, 6), (7, 3, 7), (7, 3, 7), (8, 4, 8), (8, 4, 8), (9, 4, 9), (9, 5, 9), (10, 5, 10), (10, 5, 10), (11, 6, 11), (11, 6, 11), (12, 6, 12)],
    "Druid":  [(2, 0, 2), (3, 0, 3), (3, 1, 3), (4, 1, 4), (4, 1, 4), (5, 2, 5), (5, 2, 5), (6, 2, 6), (6, 3, 6), (7, 3, 7), (7, 3, 7), (8, 4, 8), (8, 4, 8), (9, 4, 9), (9, 5, 9), (10, 5, 10), (10, 5, 10), (11, 6, 11), (11, 6, 11), (12, 6, 12)],
    "Rogue": [(0, 2, 0), (0, 3, 0), (1, 3, 1), (1, 4, 1), (1, 4, 1), (2, 5, 2), (2, 5, 2), (2, 6, 2), (3, 6, 3), (3, 7, 3), (3, 7, 3), (4, 8, 4), (4, 8, 4), (4, 9, 4), (5, 9, 5), (5, 10, 5), (5, 10, 5), (6, 11, 6), (6, 11, 6), (6, 12, 6)],
    "Bard": [(0, 2, 2), (0, 3, 3), (1, 3, 3), (1, 4, 4), (1, 4, 4), (2, 5, 5), (2, 5, 5), (2, 6, 6), (3, 6, 6), (3, 7, 7), (3, 7, 7), (4, 8, 8), (4, 8, 8), (4, 9, 9), (5, 9, 9), (5, 10, 10), (5, 10, 10), (6, 11, 11), (6, 11, 11), (6, 12, 12)]
    }    
    
    
SKILL_ABIL_MAP = {
        "Appraise": "Int",
        "Balance": "Dex",
        "Bluff": "Cha",
        "Climb": "Str",
        "Concentration": "Con",
        "Craft": "Int",
        "Decipher Script": "Int",
        "Diplomacy":  "Cha",
        "Disable Device": "Int",
        "Disguise": "Cha",
        "Escape Artist": "Dex",
        "Forgery": "Int",
        "Gather Information": "Cha",
        "Handle Animal": "Cha",
        "Heal": "Wis",
        "Hide": "Dex",
        "Intimidate": "Cha",
        "Jump": "Str",
        "Knowledge(arcana)": "Int",
        "Knowledge(dungeoneering)": "Int",
        "Knowledge(egineering)": "Int",
        "Knowledge(geography)": "Int",
        "Knowledge(history)": "Int",
        "Knowledge(local)": "Int",
        "Knowledge(nature)": "Int",
        "Knowledge(nobility)": "Int",
        "Knowledge(the planes)": "Int",
        "Knowledge(religion)": "Int",
        "Listen": "Wis",
        "Move Silently": "Dex",
        "Open Lock": "Dex",
        "Perform": "Cha",
        "Profession": "Wis",
        "Ride": "Dex",
        "Search": "Int",
        "Sense Motive": "Wis",
        "Sleight of Hand": "Dex",
        "Speak Language": "Int",
        "Spellcraft": "Int",
        "Spot": "Wis",
        "Survival": "Wis",
        "Swim": "Str",
        "Tumble": "Dex",
        "Use Magic Device": "Cha",
        "Use Rope": "Dex"
        }


SHIELD_NAMES = [
        "None", "Buckler", "Light wooden", "Light steel", "Heavy wooden",
        "Heavy steel", "Tower"]

SHIELDS = {
        #            Type  Bonus, Max Dex, Check Penalty, Spell Failure, Weight, Price
        "None": ("Light", 0, 20, 0, 0, 0, 0),
        "Buckler": ("Light", 1,  20, -1, 5, 5, 15),
        "Light wooden": ("Light", 1, 20, -1, 5, 5, 3),
        "Light steel": ("Light", 1, 20, -1, 5, 6, 9),
        "Heavy wooden": ("Heavy", 2, 20, -2, 15, 10, 7),
        "Heavy steel": ("Heavy", 2, 20, -2, 15, 15, 20),
        "Tower": ("Heavy", 4, 2, -10, 50, 45, 30)
        }
       
       
STARTING_GOLD_DICE = {
    # num of d4s, all but monk multiply result by 10
    "Fighter": 6,
    "Ranger": 6,
    "Barbarian": 4,
    "Monk": 5,
    "Paladin": 6,
    "Wizard": 3,
    "Sorcerer": 3,
    "Cleric": 5,
    "Druid": 2,
    "Rogue": 5,
    "Bard": 4
    }
       
        
SYNERGIES = {
    "Bluff": ["Diplomacy", "Disguise", "Intimidate", "Sleight of Hand"],
    "Handle Animal": ["Ride"],
    "Jump": ["Tumble"],
    "Knowledge(arcana)": ["Spellcraft"],
    "Knowledge(local)": ["Gather Information"],
    "Knowledge(nobility)": ["Diplomacy"],
    "Sense Motive": ["Diplomacy"],
    "Survival": ["Knowledge(nature)"],
    "Tumble": ["Balance", "Jump"]
    }
    
        
WEAPON_NAMES = ["Unarmed", "Dagger","Light mace","Heavy mace","Short sword",
        "Rapier","Scimitar","Long Sword","Greatsword","Quarterstaff",
        "Short Spear","Spear","Longspear","Battleaxe","Greataxe","Greatclub",
        "Sling","Light crossbow","Heavy crossbow","Shortbow","Longbow"]

WEAPONS = {
    #               Type     S  M   Crit   Wt   Price 
    "Unarmed": ("Melee", "1d2", "1d3", "x2", 0, 0), 
    "Dagger": ("Melee", "1d3", "1d4", "19-20/x2", 1, 2),
    "Light mace": ("Melee", "1d4", "1d6", "x2", 4, 5),
    "Heavy mace": ("Melee", "1d6", "1d8", "x2", 8, 12),
    "Short sword": ("Melee", "1d4", "1d6", "19-20/x2", 2, 10),
    "Long Sword": ("Melee", "1d6", "1d8", "19-20/x2", 4, 15),
    "Rapier": ("Melee", "1d4", "1d6", "18-20/x2", 2, 20),
    "Scimitar": ("Melee", "1d4", "1d6", "18-20/x2", 4, 15),
    "Quarterstaff": ("Melee", "1d4", "1d6", "x2", 4, 0),
    "Short Spear": ("Melee", "1d4", "1d6", "x2", 3, 1),
    "Spear": ("Melee", "1d6", "1d8", "x3", 6, 2),
    "Longspear": ("Melee", "1d6", "1d8", "x3", 9, 5),
    "Battleaxe": ("Melee", "1d6", "1d8", "x3", 6, 10),
    "Greataxe": ("Melee", "1d10", "1d12", "x3", 12, 20),
    "Greatclub": ("Melee", "1d8", "1d10", "x2", 8, 5),
    "Greatsword": ("Melee", "1d10", "2d6", "19-20/x2", 8, 50),
    "Sling": ("Ranged", "1d3", "1d4", "x2", 0, 0),
    "Light crossbow": ("Ranged", "1d6", "1d8", "19-20/x2", 4, 35),
    "Heavy crossbow": ("Ranged", "1d8", "1d10", "19-20/x2", 8, 50),
    "Shortbow": ("Ranged", "1d4", "1d6", "x3", 2, 30),
    "Longbow": ("Ranged", "1d6", "1d8", "x3", 3, 75)
    }
    
    
    



