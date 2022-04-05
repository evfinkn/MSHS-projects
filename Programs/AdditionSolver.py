def Addition(side):
    if (len(side) == 3):
        side = addLen3(side)
        side = Addition(side)
    elif (len(side) == 4):
        side = addLen4(side)
        side = Addition(side)
    elif (len(side) >= 5):
        side = addLen5(side)
        side = Addition(side)
    
    return side

def addLen3(side):
    for x in range(len(side)):
        if (x < len(side) - 2):
            #Positive number and Positive number
            if (side[x].isdigit() and side[x + 1] == "+" and side[x + 2].isdigit()):
                side.insert(x, str(int(side[x]) + int(side[x + 2])))
                side.pop(x + 1)
                side.pop(x + 1)
                side.pop(x + 1)
                break
            #Positive variable and Positive variable
            elif (not side[x].isdigit() and side[x + 1] == "+" and not side[x + 2].isdigit()):
                if (len(side[x]) >= 2 and len(side[x + 2]) >= 2):
                    numbers1 = FindNums(side[x])
                    num1 = ""
                    variables1 = FindVars(side[x])
                    numbers2 = FindNums(side[x + 2])
                    num2 = ""
                    variables2 = FindVars(side[x + 2])
                     
                    for y in range(len(numbers1)):
                        num1 = num1 + numbers1[y]
                    for z in range(len(numbers2)):
                        num2 = num2 + numbers2[z]
                      
                    if (len(num1) != 0 and len(num2) != 0):
                        num = str(int(num1) + int(num2))
                    elif (len(num1) == 0 and len(num2) != 0):
                        num = num2
                    elif (len(num1) != 0 and len(num2) == 0):
                        num = num1
                    elif (len(num1) == 0 and len(num2) == 0):
                        if (variables1 == variables2):
                            side.insert(x, variables1)
                            side.pop(x + 1)
                            side.pop(x + 1)
                            side.pop(x + 1)
                            break
                       
                    if (variables1 == variables2):
                        side.insert(x, str(int(num) + 1) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        break
                elif (len(side[x]) >=2 and len(side[x + 2]) < 2):
                    numbers = FindNums(side[x])
                    num = ""
                    for y in range(len(numbers)):
                        num = num + numbers[y]
                    variables1 = FindVars(side[x])
                    if (side[x + 2] == variables1):
                        side.insert(x, str(int(num) + 1) + side[x + 2])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        break
                elif (len(side[x]) < 2 and len(side[x + 2]) >= 2):
                    numbers = FindNums(side[x + 2])
                    num = ""
                    for y in range(len(numbers)):
                        num = num + numbers[y]
                    variables1 = FindVars(side[x + 2])
                    if (side[x] == variables1):
                        side.insert(x, str(int(num) + 1) + side[x])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        break
                elif (len(side[x]) < 2 and len(side[x + 2]) < 2):
                    if (side[x] == side[x + 2]):
                        side.insert(x, str(2) + side[x])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        break
    return side

def addLen4(side):
    for x in range(len(side)):
        if (x == len(side) - 3):
            side = addLen3(side)
        elif (x < len(side) - 3):
            #Positive number and Negative number
            if (side[x].isdigit() and side[x + 1] == "+" and side[x + 2] == "-" and side[x + 3].isdigit()):
                if (int(side[x]) - int(side[x + 3]) >= 0):
                    side.insert(x, str(int(side[x]) - int(side[x + 3])))
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    break
                elif (int(side[x]) - int(side[x + 3]) < 0):
                    side.insert(x, "-")
                    side.insert(x + 1, str((int(side[x]) - int(side[x + 3])) * -1))
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    break
            #Negative number and Positive number
            elif (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "+" and side[x + 3].isdigit()):
                if (int(side[x + 3]) - int(side[x + 1]) >= 0):
                    side.insert(x, str(int(side[x + 3]) - int(side[x + 1])))
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    break
                elif (int(side[x + 3]) - int(side[x + 1]) < 0):
                    side.insert(x + 1, str((int(side[x + 3]) - int(side[x + 1])) * -1))
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    break
            #Positive variable and Negative variable
            elif (not side[x].isdigit() and side[x + 1] == "+" and side[x + 2] == "-" and not side[x + 3].isdigit()):
                
            #Negative variable and Positive variable
            elif (side[x] == "-" and not side[x + 1].isdigit() and side[x + 2] == "+" and not side[x + 3].isdigit()):
            
            else:
                side = addLen3(side)
                break
    return side

def addLen5(side):
    for x in range(len(side)):
        if (x == len(side) - 3):
            side = addLen3(side)
        elif (x == len(side) - 4):
            side = addLen4(side)
        elif (x < len(side) - 4):
            #Negative number and Negative number
            if (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "+" and side[x + 3] == "-" and side[x + 4].isdigit()):
                side.insert(x + 1, str(int(side[x + 1]) + int(side[x + 4])))
                side.pop(x + 2)
                side.pop(x + 2)
                side.pop(x + 2)
                side.pop(x + 2)
                break
            #Negative variable and Negative variable
            elif (side[x] == "-" and not side[x + 1].isdigit() and side[x + 2] == "+" and side[x + 3] == "-" and not side[x + 4].isdigit()):
                
            else:
                side = addLen4(side)
                break
                
    return side
            
#Find numbers in a string
def FindNums(string):
    if (type(string) == type("string")):
        string = list(string)
    for y in range(len(string)):
        if (string[y] == "^"):
            string.pop(y)
            string.pop(y)
            string = FindNums(string)
            break
        elif (not string[y].isdigit()):
            string.pop(y)
            string = FindNums(string)
            break
    return string

#Find variables in a string
def FindVars(string):
    if (type(string) == type("string")):
        string = list(string)
    for y in range(len(string)):
        if (string[y] == "^"):
            string[y - 1] = string[y - 1] + string[y] + string[y + 1]
            string.pop(y)
            string.pop(y)
            string = FindVars(string)
            break
        elif (string[y].isdigit()):
            string.pop(y)
            string = FindVars(string)
            break
    return string

side = ["10", "+", "-", "12", "+", "10x", "+", "3x"]
print (side)
print (Addition(side))