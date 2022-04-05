def encrypt (text, shiftNum, direction):
    cipherText = ""
    if (direction == "left" or direction == "l"):
        shiftNum = -shiftNum
    for char in text:
        if (char != " "):
            code = ord(char)
            if (code > 96 and code < 123):
                code += shiftNum
                if (code > 122):
                    code = 97 + (code - 123)
                elif (code < 97):
                    code = 123 - (97 - code)
            elif (code > 64 and code < 91):
                code += shiftNum
                if (code > 90):
                    code = 65 + (code - 91)
                elif (code < 65):
                    code = 91 - (65 - code)
            cipherText += chr(code)
        else:
            cipherText += " "
    return cipherText
    
def decryptKnown(cipherText, shiftNum, direction):
    text = ""
    if (direction == "right" or direction == "r"):
        shiftNum = -shiftNum
    for char in cipherText:
        if (char != " "):
            code = ord(char)
            if (code > 96 and code < 123):
                code += shiftNum
                if (code > 122):
                    code = 97 + (code - 123)
                elif (code < 97):
                    code = 123 - (97 - code)
            elif (code > 64 and code < 91):
                code += shiftNum
                if (code > 90):
                    code = 65 + (code - 91)
                elif (code < 65):
                    code = 91 - (65 - code)
            text += chr(code)
        else:
            text += " "
    return text

def decryptUnknown(cipherText):
    for shiftNum in range(1, 26):
        text = ""
        for char in cipherText:
            if (char != " "):
                code = ord(char)
                if (code > 96 and code < 123):
                    code += shiftNum
                    if (code > 122):
                        code = 97 + (code - 123)
                    elif (code < 97):
                        code = 123 - (97 - code)
                elif (code > 64 and code < 91):
                    code += shiftNum
                    if (code > 90):
                        code = 65 + (code - 91)
                    elif (code < 65):
                        code = 91 - (65 - code)
                text += chr(code)
            else:
                text += " "
        deciphered = input("Does " + text + " make sense?")
        deciphered = deciphered.lower()
        if (deciphered == "yes" or deciphered == "y"):
            return text
    for shiftNum in range(1, 26):
        text = ""
        for char in cipherText:
            if (char != " "):
                code = ord(char)
                if (code > 96 and code < 123):
                    code += -shiftNum
                    if (code > 122):
                        code = 97 + (code - 123)
                    elif (code < 97):
                        code = 123 - (97 - code)
                elif (code > 64 and code < 91):
                    code += -shiftNum
                    if (code > 90):
                        code = 65 + (code - 91)
                    elif (code < 65):
                        code = 91 - (65 - code)
                text += chr(code)
            else:
                text += " "
        deciphered = input("Does " + text + " make sense?")
        deciphered = deciphered.lower()
        if (deciphered == "yes" or deciphered == "y"):
            return text
    return ("The text couldn't be deciphered.")

typeOf = input("Are you encrypting or decrypting?")
typeOf = typeOf.lower()

if (typeOf == "encrypting" or typeOf == "encrypt" or typeOf == "e"):
    text = input("Enter the text to encrypt:")
    shiftNum = int(input("How many positions should it shift?"))
    direction = input("Should it shift left or right?")
    direction = direction.lower()
    
    print (encrypt(text, shiftNum, direction))

elif (typeOf == "decrypting" or typeOf == "decrypt" or typeOf == "d"):
    knownBool = input("Do you know the shift?")
    knownBool = knownBool.lower()
    
    if (knownBool == "yes" or knownBool == "y"):
        cipherText = input("Enter the text to decrypt:")
        shiftNum = int(input("How many positions did it shift?"))
        direction = input("Did it shift left or right?")
        direction = direction.lower()
        
        print (decryptKnown(cipherText, shiftNum, direction))
        
    elif (knownBool == "no" or knownBool == "n"):
        cipherText = input("Enter the text to decrypt:")
        print(decryptUnknown(cipherText))
        
    else:
        print ("You entered something wrong. Make sure to enter \'yes\' or \'no\'")
        
else:
    print ("You entered something wrong. Make sure to input \'encrypting\' or \'decrypting\'")