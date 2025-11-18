#ATBASH cypher
from re import match


def atbashEncrypter(message):
    newMessage = ""
    aplha = "abcdefghijklmnopqrstuvwxyz"
    revAlpha = "zyxwvutsrqponmlkjihgfedcba"
    for letter in message:
        if letter.isalpha():
            index = aplha.index(letter)
            newMessage += revAlpha[index]
        else:
            continue;
    return newMessage;


wrongChoice = True

while wrongChoice:
    whichCy = input("Would you like to encyript(1) or decrypt(2) : ").lower()
    if whichCy == 1:
        wrongChoice = False
    elif whichCy == 2:
        wrongChoice = False
    print("Please enter 1 to encrypt a message or 2 to decrypt a message")

if whichCy == 1:
    encyptionType = int(input("Would you like to encrypt with atbash(1) "))
    match encyptionType:
        # When user enters one then the code incrypts their message using atbash
        case 1: 
            message = input("What message would you like to incrypt? : ").lower()
            print(atbashEncrypter(message))

elif whichCy == 2:
    decyptionType = int(input("Would you like to decrypt with atbash(1) "))
    match decyptionType:
        case 1:
            print()

