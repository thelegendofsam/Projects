#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sam-S
#
# Created:     24/03/2021
# Copyright:   (c) Sam-S 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


import random

def magic_8():
    input(print("What is your question? Must be yes or no"))
    random_number=random.randint(0,8)
    if random_number == 0:
        print("Yes- definatly")
    elif random_number == 1:
        print("It is decidedly so.")
    elif random_number == 2:
        print("Without a doubt.")
    elif random_number == 3:
        print("Reply hazy, try again.")
    elif random_number == 4:
        print("Ask again later.")
    elif random_number == 5:
        print("Better not tell you now.")
    elif random_number == 6:
        print("My sources say no.")
    elif random_number == 7:
        print("Outlook not so good.")
    elif random_number == 8:
        print("Very doubtful.")

magic_8()