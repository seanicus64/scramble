#!/usr/bin/env python3
import random
string = input("Put in your sentence, HS.  I'm too lazy to handle punctuation tho\n")
if not string:
    string = "The Industrial Revolution and its consequences have been a disaster for the human race . They have greatly increased the Iffe - expectancy of those of us who live in ' advanced ' countries , but they have destabilized society , have made life unfulfilling , have subjected human beings to indignities , have led to widespread psychological suffering ( in the Third World to physical suffering as well ) and have inflicted severe damage on the natural world . The continued development of technology will worsen the situation . It will certainly subject human being to greater indignities and inflict greater damage on the natural world , it will probably lead to greater social disruption and psychological suffering , and it may lead to increased physical suffering even in advanced countries".lower()
new = ""
split = string.split()
for word in split:
    word_list = list(word)
    if len(word) > 3:
        first = word_list.pop(0)
        last = word_list.pop()
        random.shuffle(word_list)
        new += " {}{}{}".format(first, "".join(word_list), last)
    else:
        new += " " + word
print(new)

