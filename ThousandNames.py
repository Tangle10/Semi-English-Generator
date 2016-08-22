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

word = 0
wordcount = 0
word0 = 0
word1 = 0
word2 = 0
word3 = 0
word4 = 0
word5 = 0
word6 = 0
word7 = 0
word8 = 0
word9 = 0
word10 = 0
while wordcount < 1000:
    sylc = random.randrange(2,8)
    syl1 = english_dict[random.randrange(0,59)]
    syl2 = english_dict[random.randrange(0,59)]
    syl3 = english_dict[random.randrange(0,59)]
    syl4 = english_dict[random.randrange(0,59)]
    syl5 = english_dict[random.randrange(0,59)]
    syl6 = english_dict[random.randrange(0,59)]
    syl7 = english_dict[random.randrange(0,59)]
    syl8 = english_dict[random.randrange(0,59)]
    if sylc == 1: word = str(syl1) + str(syl2)
    elif sylc == 2: word = str(syl1) + str(syl2)
    elif sylc == 3: word = str(syl1) + str(syl2) + str(syl3)
    elif sylc == 4: word = str(syl1) + str(syl2) + str(syl3) + str(syl4)
    elif sylc == 5: word = str(syl1) + str(syl2) + str(syl3) + str(syl4) + str(syl5)
    elif sylc == 6: word = str(syl1) + str(syl2) + str(syl3) + str(syl4) + str(syl5) + str(syl6)
    elif sylc == 7: word = str(syl1) + str(syl2) + str(syl3) + str(syl4) + str(syl5) + str(syl6) + str(syl7)
    elif sylc == 8: word = str(syl1) + str(syl2) + str(syl3) + str(syl4) + str(syl5) + str(syl7) + str(syl8)
    #attempt to create "word0", "word1", etc.
    print str(word)
    words.append(word)
    wordcount = wordcount + 1
with open("TrillionNames" + str(RAND) + ".txt", "w") as text_file:
    text_file.write(str(words))