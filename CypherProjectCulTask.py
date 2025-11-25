#ATBASH cypher
from re import match
from itertools import cycle
import string

def cesarianOrMonoEncryption(cesarian = bool,twoAlphabets = ""):
    if cesarian:
        newMessage = "" 
        upOrDown = int(input("Would you like to shift up(1) or down(2): "))     
        shifts = int(input("How many letter places are you shifting? : "))     
        match upOrDown:
            case 1:
                #If user is inefficient and enters a number more than 26 than minus 26 from the number to avoid error
                    if shifts > 26:
                        shifts -= 26
                    for letter in message:
                        if letter.isalpha():
                            #when user wants to go up start with second alphabet by adding 26
                            index = twoAlphabets.index(letter) + 26
                            #to go up minus index by number of shifts user wants up
                            newMessage += twoAlphabets[index - shifts] 
                        else:
                            # if char is not a letter than continue aka don't touch chars that are not letters
                            continue;
                        #printing of new message to user
            case 2:
                #If user is inefficient and enters a number more than 26 than minus 26 from the number to avoid error
                    if shifts > 26:
                        shifts -= 26
                    for letter in message:
                        if letter.isalpha():
                            #when user wants to go down start with first alphabet
                            index = twoAlphabets.index(letter)
                            #to go up add index by number of shifts user wants down
                            newMessage += twoAlphabets[index + shifts] 
                    else:
                        # if char is not a letter than continue aka don't touch chars that are not letters
                        newMessage += letter
                        #printing of new message to user
        print(newMessage)
    elif not(cesarian):
        newMessage = "" 
        upOrDown = int(input("Would you like to shift up(1) or down(2): "))     
        shifts = int(input("How many letter places are you shifting? : "))     
        match upOrDown:
            case 1:
                #If user is inefficient and enters a number more than 26 than minus 26 from the number to avoid error
                    if shifts > 26:
                        shifts -= 26
                    for letter in message:
                        if letter.isalpha():
                            #when user wants to go up start with second alphabet by adding 26
                            index = twoAlphabets.index(letter) + 26
                            #to go up minus index by number of shifts user wants up
                            newMessage += twoAlphabets[index - shifts] 
                        else:
                            # if char is not a letter than continue aka don't touch chars that are not letters
                            newMessage += letter
                        #printing of new message to user
            case 2:
                #If user is inefficient and enters a number more than 26 than minus 26 from the number to avoid error
                    if shifts > 26:
                        shifts -= 26
                    for letter in message:
                        if letter.isalpha():
                            #when user wants to go down start with first alphabet
                            index = twoAlphabets.index(letter)
                            #to go up add index by number of shifts user wants down
                            newMessage += twoAlphabets[index + shifts] 
                    else:
                        # if char is not a letter than continue aka don't touch chars that are not letters
                        newMessage += letter
                        #printing of new message to user
        print(newMessage)

def vigenreCypher(message):
            newMessage = ""
            twoAlphabets = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" 
            keyword = input("What is your keyword? : ").lower()
            upOrDown = int(input("Would you like to shift up(1) or down(2): "))
            shifts = []
            #determining how the index of each letter in keyword fom the alphabet
            for letter in keyword:
                shifts.append(twoAlphabets.index(letter))

            #for letter in message:
                #shifts += shifts
            for i in range(5):
                shifts += shifts

            match upOrDown:
                case 1:
                    count = 0
                    for letter in message:
                        if letter.isalpha():
                            #when user wants to go up start with second alphabet by adding 26
                            index = twoAlphabets.index(letter) + 26
                            #to go up minus index by number of shifts user wants up
                            newMessage += twoAlphabets[index - shifts[count]] 
                            count += 1
                        else:
                            # if char is not a letter than continue aka don't touch chars that are not letters
                            newMessage += letter
                            count += 1
                    #printing of new message to user
                    print(newMessage)
                case 2:
                    count = 0
                    for letter in message:
                        if letter.isalpha():
                            #when user wants to go down start with first alphabet
                            index = twoAlphabets.index(letter)
                            #to go up add index by number of shifts user wants down
                            newMessage += twoAlphabets[index + shifts[count]] 
                            count+=1
                        else:
                            # if char is not a letter than continue aka don't touch chars that are not letters
                            newMessage += letter
                            count+=1
                    #printing of new message to user
                    print(newMessage)


def beconianCypher():
    newMessage = ""
    beconianList= ""
    lenOfbeconianList = 0
    encodedLeters = ""
    beconianLetters = {"aaaaa":["A"],"aaaab":["B"],"aaaba":["C"],"aaabb":["D"],"aabaa":["E"],
                   "aabab":["F"],"aabba":["G"],"aabbb":["H"],"abaaa":["I"],"abaab":["J"],
                   "ababa":["K"],"ababb":["L"],"abbaa":["M"],"abbab":["N"],"abbba":["O"],
                   "abbbb":["P"],"baaaa":["Q"],"baaab":["R"],"baaba":["S"],"baabb":["T"],
                   "babaa":["U"],"babab":["V"],"babba":["W"],"babbb":["X"],"bbaaa":["Y"],
                   "bbaab":["Z"]}

    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                encodedLeters += "b"
            elif letter.islower():
                encodedLeters += "a"
        else:
            continue;
    print(encodedLeters)

    lenOfbeconianList = len(encodedLeters)// 5

    # add letter to index
# if length of item in list is 5 go to next index
     
    for beconianLetter in lenOfbeconianList:
        for letter in encodedLeters:
            if not(len(beconianList[letter]) == 5):
                beconianLetter += letter
            elif len(lenOfbeconianList[letter]) == 5:
                break;
    
        
    print()

            
    




wrongChoice = True

while wrongChoice:
    whichCy = int(input("Would you like to encrypt(1) or decrypt(2) : "))
    if whichCy == 1:
        wrongChoice = False
    elif whichCy == 2:
        wrongChoice = False
    else:
        print("Please enter 1 to encrypt a message or 2 to decrypt a message")

if whichCy == 1:
    encryptionType = int(input("Would you like to encrypt with atbash(1), Mono(2), Caesarean(3), Vigenere(4) or Baconian(5) :"))
    if encryptionType == 5:
        print("Ignore all usual capitalization rules. For your message A's are is lowercase letters and B's are upper case.")
        print("Spell out all numbers")
        message = input("What message would you like to encrypt? : ")
    else:
        message = input("What message would you like to encrypt? : ").lower()

    match encryptionType:
        # When user enters one then the code encrypts their message using atbash
        case 1: 
            newMessage = ""
            aplha = "abcdefghijklmnopqrstuvwxyz"
            revAlpha = "zyxwvutsrqponmlkjihgfedcba"
            for letter in message:
                if letter.isalpha():
                    index = aplha.index(letter)
                    newMessage += revAlpha[index]
                else:
                    newMessage += letter
                    continue;
            print(newMessage)
        #Mono
        case 2:
            invalidAlphabet = True
            
            # loop through the user input until a valid alphabet is entered
            # assume it is invalid at start
            while invalidAlphabet:

                checkedLetters = "" 
                alphabetlengthIsInvalid = False
                hasInvalidCharacter = False

                userAlpha = input("Please enter your own alphabet:").lower()        
                
                # the alphabet must contain all 26 letters if not program throws error to user
                if not(len(userAlpha) == 26 ):

                    print("Alphabet has to contain all 26 letters of the english alphabet, no more or less. Please try again.")
                    alphabetlengthIsInvalid = True

                else:
                    #Checking to see if user alphabet is valid
                    for letter in userAlpha:
                        #no numbers, special characters or spaces
                        if letter.isnumeric() or not(letter.isalnum()) or letter.isspace():
                            print("Alphabets have no numbers, special characters or spaces. Please try again")
                            hasInvalidCharacter = True
                            break

                        #has to have one of each letter aka no duplicates
                        if not(checkedLetters.find(letter) == -1):
                            print("Alphabets have no repeating chars")
                            hasInvalidCharacter = True
                            break

                        else:
                            # if char in loop not in string add char
                            checkedLetters += letter

                          
                if hasInvalidCharacter or alphabetlengthIsInvalid:
                    invalidAlphabet = True
                else:
                    invalidAlphabet = False
                        
            # here the checkedLetters will have always the valid input
            # call function to encrypt
            cesarianOrMonoEncryption(False, userAlpha + userAlpha)
        case 3:
            cesarianOrMonoEncryption(True, "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
        case 4:
            vigenreCypher(message)
        case 5:
            beconianCypher()
            



elif whichCy == 2:
    decryptionType = int(input("Would you like to decrypt by atbash(1), Mono(2), Cesarian(3), Vingenre(4) :"))
    message = input("What message would you like to decrypt? : ").lower()
    match decryptionType:
        case 1:
            newMessage = ""
            aplha = "abcdefghijklmnopqrstuvwxyz"
            revAlpha = "zyxwvutsrqponmlkjihgfedcba"
            #iterating through every char(letter) from the message
            for letter in message:
                if letter.isalpha():
                    #finding the index of the letter in the reversed alphabet
                    index = revAlpha.index(letter)
                    #adding corresponding letter at same index in alphabet to newMessage
                    newMessage += aplha[index]
                else:
                    # if any spaces,numbers or special chars than move onto next char
                    newMessage += letter
            #printing result to user
            print(newMessage)
        case 2:
            invalidAlphabet = True
            
            # loop through the user input until a valid alphabet is entered
            # assume it is invalid at start
            while invalidAlphabet:

                checkedLetters = "" 
                alphabetlengthIsInvalid = False
                hasInvalidCharacter = False

                userAlpha = input("Please enter the mixed alphabet:").lower()        
                

                if not(len(userAlpha) == 26 ):

                    print("Alphabet has to contain all 26 letters of the english alphabet, no more or less. Please try again.")
                    alphabetlengthIsInvalid = True

                else:
                    #Checking to see if user alphabet is valid
                    for letter in userAlpha:
                        #no numbers, special characters or spaces
                        if letter.isnumeric() or not(letter.isalnum()) or letter.isspace():
                            print("Alphabets have no numbers, special characters or spaces. Please try again")
                            hasInvalidCharacter = True
                            break

                        #has to have one of each letter aka no duplicates
                        if not(checkedLetters.find(letter) == -1):
                            print("Alphabets have no repeating chars")
                            hasInvalidCharacter = True
                            break

                        else:
                            # if char in loop not in string add char
                            checkedLetters += letter

                          
                if hasInvalidCharacter or alphabetlengthIsInvalid:
                    invalidAlphabet = True
                else:
                    invalidAlphabet = False
                        
            # here the checkedLetters will have always the valid input
            cesarianOrMonoEncryption(False, userAlpha + userAlpha)
        case 3:
            cesarianOrMonoEncryption(True, "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
        case 4:
            vigenreCypher(message)