#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sam-S
#
# Created:     23/03/2021
# Copyright:   (c) Sam-S 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import random

def roll_dice():
    answer=input(print("roll dice?"))
    if answer == "yes":
        print(random.randint(1,6))
    else:
        print("done")
        return
    roll_dice()

roll_dice()




