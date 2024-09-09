# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:49:09 2024
@author: segal
"""
# dice roll game in py
import random
# use unicode 
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ │ └ ┘
# To build dice:
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
# next dictionary for dice art:
DieArt = {
    1: ( "┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    2: ( "┌─────────┐",
         "│  ●      │",
         "│         │",
         "│      ●  │",
         "└─────────┘"),
    3: ( "┌─────────┐",
         "│  ●      │",
         "│    ●    │",
         "│      ●  │",
         "└─────────┘"),
    4: ( "┌─────────┐",
         "│  ●    ● │",
         "│         │",
         "│  ●    ● │",
         "└─────────┘"),
    5: ( "┌─────────┐",
         "│  ●    ● │",
         "│     ●   │",
         "│  ●    ● │",
         "└─────────┘"),
    6: ( "┌─────────┐",
         "│  ●    ● │",
         "│  ●    ● │",
         "│  ●    ● │",
         "└─────────┘")  
}

# next a list of dice:
dies = []
AllCnt = 0
NumberDie = int(input("How many dice?: "))

for die in range(NumberDie):

    dies.append(random.randint(1, 6))
# to see num of die
#print(dice)
# next see a total:
    
# and display the dice art:

#for die in range(NumberDie):
#    for line in DieArt.get(dies[die]):
#        print(line)

# but to see each die on 1 line:
for line in range(5):
    for die in dies:
        print(DieArt.get(die)[line], end=" ")
    print()
    
for die in dies:
    AllCnt += die
print(f"total: {AllCnt}")
