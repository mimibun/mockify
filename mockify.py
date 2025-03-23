from random import randint
import argparse

parser = argparse.ArgumentParser(description="a tool to mockify text")
parser.add_argument("sentence", metavar="<sentence>", type=str, help="sentence to mockify")
args = parser.parse_args()

def mockifyParse(sentence):
    s = ""
    space = " "

    for letter in sentence:
        if letter.isalpha() == True:
            rng = randint(0, 1)
            if rng == 1:
                letter = letter.upper()
            else:
                letter = letter.lower()
        elif letter == space:
            space += letter
        s += letter

    return s


output = mockifyParse(args.sentence)
print(output)