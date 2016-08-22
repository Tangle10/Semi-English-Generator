import random

RAND = random.randrange(0,99999999)

words = []

english_dict = {
    0: "a",
    1: "ae",
    2: "ai",
    3: "au",
    4: "b",
    5: "c",
    6: "ch",
    7: "d",
    8: "e",
    9: "ea",
    10: "ee",
    11: "eg",
    12: "f",
    13: "g",
    14: "h",
    15: "i",
    16: "ie",
    17: "io",
    18: "j",
    19: "je",
    20: "jo",
    21: "k",
    22: "l",
    23: "m",
    24: "n",
    25: "o",
    26: "oo",
    27: "p",
    28: "q",
    29: "qu",
    30: "qu",
    31: "r",
    32: "re",
    33: "ri",
    34: "ro",
    35: "ru",
    36: "s",
    37: "sh",
    38: "ss",
    39: "t",
    40: "te",
    41: "ti",
    42: "u",
    43: "ue",
    44: "ug",
    45: "v",
    46: "ve",
    47: "w",
    48: "wi",
    49: "wh",
    50: "ex",
    51: "x",
    52: "y",
    53: "ya",
    54: "ye",
    55: "yo",
    56: "yu",
    57: "z", 
    58: "'nt",
    59: "'s",
}

# this function grabs syllables from the dictionary and strings them together.
words = [''.join([random.choice(english_dict) for _ in range(random.randint(2,8))]) for _ in range(1000)]
# this part creates an output
with open("TrillionNames" + str(RAND) + ".txt", "w") as text_file:
    text_file.write(str(words))