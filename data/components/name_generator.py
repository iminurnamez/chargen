from random import choice, randint


FEMALE_NAMES = ["Daisy", "Violet", "Lobelia", "Esmerelda", "Holly", "Amelia",
                 "Dulcina", "Elvina", "Juniper", "Gwendolyn", "Azalea",
                 "Adelaide", "Caldonia", "Cordelia", "Glendora", "Filomena",
                 "Louvenia", "Gretel", "Myrtle", "Clementine", "Prunella",
                 "Blossom", "Lily", "Iris", "Jasmine", "Petunia", "Poppy", "Fern",
                 "Ivy", "Flora", "Contessa", "Ambrosia", "Guinivere",
                 "Saffron", "Veronica", "Fiona", "Arianna", "Abigail",
                 "Geneva", "Phoebe", "Robin", "Octavia", "Rowena",
                 "Ramona", "Althea", "Evangeline", "Emmaline", "Elspeth",
                 "Hester", "Eleonora", "Ethel", "Claribel", "Maribel",
                 "Hortensia", "Gilda", "Claudia", "Beatrix"]
                 
MALE_NAMES = ["Cornelius", "Alowicius", "Maximillian", "Ebenezer", "Quentin",
              "Demetrius", "Cedric", "Seamus", "Thaddeus", "Basil", "Aelfric",
              "Chadwick", "Hershell", "Finnegan", "Mortimer", "Percival",
              "Archibald", "Hansel", "Hiram", "Kale",
              "Reed", "Clovis", "Vernon", "Humphrey", "Chester", "Fergus",
              "Crispin", "Atticus", "Grover", "Stanton", "Thornton", 
              "Walden", "Llewellyn", "Montgomery", "Octavius",
              "Wilbur", "Alfredo", "Nelson", "Silas", "Jasper", "Edmund", 
              "Elwood", "Bertram", "Thurman", "Haywood", "Seymour",
              "Wellington", "Roderick", "Cyril", "Elmer", "Herbert", "Rufus"]


PREFIXES = {
        1: ["Gr", "G", "Gl", "Fr", "F", "Fl", "T", "Tr", "V", "Vr", "Vl", "B",
            "Br", "Bl", "P", "Pr", "Pl"],
        2: ["Mar", "Mal", "Mer", "Mel", "Dar", "Del", "Der", "Car", "Cal",
            "Cer", "Cel", "Var", "Ver", "Bar", "Ber", "Par", "Per", "St"]
        }    
    #        ["Al", "Ar", "An",
    #"Er",
    #"Kel",
    #"Cor",
    #"Gar",
    #"Lon",
    #"Kev",
    #"Nard",
    #"Gard",
    #"]
    
    
    
MIDDLES = {
        1: ["im", "if", "il", "ik", "om", "on", "of", "ol", "ok", "um", "uf",
            "ul", "am", "af", "al", "ak", "an", "em", "en", "ef", "el", "ek"],
        2: ["il", "in", "lin", "til", "in", "id"] 
        }
        #"a", "o", "e", "el"]

SUFFIXES = {
        1: ["lar", "lin", "lane", "hane", "rane", "rin", "ris", "rit", "nis",
            "nin", "bin", "lib", "bil", "blit", "blif", "nib", "tar", "blin"],
        2: ["ius", "ian", "tis", "tus", "dius"]
        }
TITLES = [
        "Impenetrable", "Wise", "Strong", "Foolish", "Nimble", "Powerful",
        "Kind", "Great", "Swift", "Silent", "Weak", "Wild", "Wealthy", "Elder", "Fist", "Blade"]
    
def build_name():
    num = 2
    pre = choice(PREFIXES[num])
    pre += choice(MIDDLES[num])
    pre += choice(SUFFIXES[num])
    return pre
    
def generate_name():
    if not randint(0, 2):
        if not randint(0, 1):
            name = choice(MALE_NAMES)
        else:
            name = choice(FEMALE_NAMES)
    else:
        name = build_name()
    if not randint(0, 5):
        name += " the {}".format(choice(TITLES))
    return name        
