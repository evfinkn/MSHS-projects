def Division(side):
    if (len(side) == 3):
        side = divideLen3(side)
        side = Division(side)
    elif (len(side) == 4):
        side = divideLen4(side)
        side = Division(side)
    elif (len(side) >= 5):
        side = dividLen5(side)
        side = Division(side)
    
    return side

def divideLen3(side):
    for x in range(len(side)):
        if (x < len(side) - 2):
    		#Positive number and positive number
    		if (side[x].isdigit() and side[x + 1] == "/" and side[x + 2].isdigit()):
                side.insert(x, str(int(side[x]) / int(side[x + 2])))
                side.pop(x + 1)
                side.pop(x + 1)
                side.pop(x + 1)
                break    
    		#Positive variable and positive variable
    		elif (not side[x].isdigit() and side[x + 1] == "/" and not side[x + 2].isdigit()):
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
                        num = str(int(num1) * int(num2))
                    elif (len(num1) == 0 and len(num2) != 0):
                        num = num2
                    elif (len(num1) != 0 and len(num2) == 0):
                        num = num1
                    elif (len(num1) == 0 and len(num2) == 0):
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        break
                       
                    var = MultiplyVars(variables1, variables2)
                    side.insert(x, num + var)
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
                    var = MultiplyVars(variables1, side[x + 2])
                    side.insert(x, num + var)
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
                    var = MultiplyVars(variables1, side[x])
                    side.insert(x, num + var)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    break
                elif (len(side[x]) < 2 and len(side[x + 2]) < 2):
                    if (side[x] == side[x + 2]):
                        side.insert(x, "1")
                    	side.pop(x + 1)
                    	side.pop(x + 1)
                    	side.pop(x + 1)
                    break
    return side
def divideLen4(side):
    for x in range(len(side)):
        if (x == len(side) - 3):
            side = multiplyLen3(side)
        elif (x < len(side) - 3):
    		#Positive number and negative number
    		if (side[x].isdigit() and side[x + 1] == "/" and side[x + 2] == "-" and side[x + 3].isdigit()):
                side.insert(x, "-")
                side.insert(x + 1, str(int(side[x]) / int(side[x + 3])))
                side.pop(x + 2)
                side.pop(x + 2)
                side.pop(x + 2)
                side.pop(x + 2)
                break
    		#Negative number and positive number
    		elif (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3].isdigit()):
                side.insert(x + 1, str(int(side[x + 1]) / int(side[x + 3])))
                side.pop(x + 2)
                side.pop(x + 2)
                side.pop(x + 2)
                break    
    		#Positive variable and negative variable
    
    		#Negative variable and positive variable
         
def divideLen5(side):
    for x in range(len(side)):
        if (x == len(side) - 3):
            side = multiplyLen3(side)
        elif (x == len(side) - 4):
            side = multiplyLen4(side)
        elif (x < len(side) - 4):
    		#Negative number and negative number
    
    		#Negative variable and negative variable

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

side = ["30x", "/", "x", "/", "10"]
print (side)
print (Division(side))