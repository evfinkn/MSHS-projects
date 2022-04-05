def Multiplication(side):
    b = False
    if (len(side) == 3):
        for x in range(len(side)):
            if (x < len(side) - 2):
                #Positive number and positive number
                if (side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    side.insert(x, str(int(side[x]) * int(side[x + 2])))
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side = Multiplication(side)
                    break
                    
                #Positive number and positive variable
                elif (side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
                    if (len(side[x + 2] >= 2)):
                        numbers = FindNums(side[x + 2])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 2])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 2] < 2)):
                        side.insert(x, side[x] + side[x + 2])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and positive number
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    if (len(side[x + 2] >= 2)):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x + 2]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x] < 2)):
                        side.insert(x, side[x] + side[x + 2])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and positive variable
                elif (not side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
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
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, num + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
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
                        side = Multiplication(side)
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
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 2]) < 2):
                        var = MultiplyVars(side[x], side[x + 2])
                        side.insert(x, var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
    elif (len(side) == 4):
        for x in range(len(side)):
            if (x == len(side) - 3):
                #Positive number and positive number
                if (side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    side.insert(x, str(int(side[x]) * int(side[x + 2])))
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side = Multiplication(side)
                    break
                    
                #Positive number and positive variable
                elif (side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
                    if (len(side[x + 2] >= 2)):
                        numbers = FindNums(side[x + 2])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 2])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 2] < 2)):
                        side.insert(x, side[x] + side[x + 2])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                
                #Positive variable and positive number
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    if (len(side[x + 2] >= 2)):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x + 2]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x] < 2)):
                        side.insert(x, side[x] + side[x + 2])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and positive variable
                elif (not side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
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
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, num + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
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
                        side = Multiplication(side)
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
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 2]) < 2):
                        var = MultiplyVars(side[x], side[x + 2])
                        side.insert(x, var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
            elif (x < len(side) - 3):
                #Positive number and negative number
                if (side[x].isdigit() and side[x + 1] == "*" and side[x + 2] == "-" and side[x + 3].isdigit()):
                    side.insert(x, "-")
                    side.insert(x + 1, str(int(side[x + 1]) * int(side[x + 4])))
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side = Multiplication(side)
                    break
                    
                #Negative number and positive number
                elif (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3].isdigit()):
                    side.insert(x + 1, str(int(side[x + 1]) * int(side[x + 3])))
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side = Multiplication(side)
                    break
                
                #Positive number and negative variable
                elif(side[x].isdigit() and  side[x + 1] == "*" and side[x + 2] == "-" and not side[x + 3].isdigit()):
                    if (len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 3])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, "-")
                        side.insert(x + 1, str(int(side[x + 1]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 3]) < 2):
                        side.insert(x, "-")
                        side.insert(x + 1, side[x] + side[x + 3])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                
                #Negative number and positive variable
                elif (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "*" and not side[x + 3].isdigit()):
                    if (len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 3])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x + 1, str(int(side[x + 1]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 3]) < 2):
                        side.insert(x + 1, side[x + 1] + side[x + 3])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                
                #Positive variable and negative number
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2] == "-" and side[x + 3].isdigit()):
                    if (len(side[x]) >= 2):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, "-")
                        side.insert(x + 1, str(int(side[x + 4]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif(len(side[x]) < 2):
                        side.insert(x, "-")
                        side.insert(x + 1, side[x + 4] + side[x + 1])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                
                #Negative variable and positive number
                elif (side[x] == "-" and not side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3].isdigit()):
                    if (len(side[x + 1]) >= 2):
                        numbers = FindNums(side[x + 1])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side(x + 1, str(int(side[x + 3]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2):
                        side.insert(x + 1, side[x + 3] + side[x + 1])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and negative variable
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2] == "-" and not side[x + 3].isdigit()):
                    if (len(side[x]) >= 2 and len(side[x + 3]) >= 2):
                        numbers1 = FindNums(side[x])
                        num1 = ""
                        variables1 = FindVars(side[x])
                        numbers2 = FindNums(side[x + 3])
                        num2 = ""
                        variables2 = FindVars(side[x + 3])
                        
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
                            side.insert(x, "-")
                            side.insert(x + 1, var)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, "-")
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) >=2 and len(side[x + 3]) < 2):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x])
                        var = MultiplyVars(variables1, side[x + 3])
                        side.insert(x, "-")
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 3])
                        var = MultiplyVars(variables1, side[x])
                        side.insert(x, "-")
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 3]) < 2):
                        var = MultiplyVars(side[x], side[x + 3])
                        side.insert(x, "-")
                        side.insert(x + 1, var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Negative variable and positive variable
                elif (side[x] == "-" and not side[x + 1].isdigit() and side[x + 2] == "*" and not side[x + 3].isdigit()):
                    if (len(side[x + 1]) >= 2 and len(side[x + 3]) >= 2):
                        numbers1 = FindNums(side[x + 1])
                        num1 = ""
                        variables1 = FindVars(side[x + 1])
                        numbers2 = FindNums(side[x + 3])
                        num2 = ""
                        variables2 = FindVars(side[x + 3])
                        
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
                            side.insert(x + 1, var)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) >=2 and len(side[x + 3]) < 2):
                        numbers = FindNums(side[x + 1])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 1])
                        var = MultiplyVars(variables1, side[x + 3])
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2 and len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 3])
                        var = MultiplyVars(variables1, side[x + 1])
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2 and len(side[x + 3]) < 2):
                        var = MultiplyVars(side[x + 1], side[x + 3])
                        side.insert(x + 1, var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Positive number and positive number
                elif (side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    side.insert(x, str(int(side[x]) * int(side[x + 2])))
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side = Multiplication(side)
                    break
                    
                #Positive number and positive variable
                elif (side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
                    if (len(side[x + 2]) >= 2):
                        numbers = FindNums(side[x + 2])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 2])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 2]) < 2):
                        side.insert(x, side[x] + side[x + 2])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                
                #Positive variable and positive number
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    if (len(side[x]) >= 2):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x + 2]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2):
                        side.insert(x, side[x + 2] + side[x])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and positive variable
                elif (not side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
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
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, num + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
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
                        side = Multiplication(side)
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
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 2]) < 2):
                        var = MultiplyVars(side[x], side[x + 2])
                        side.insert(x, var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
    elif (len(side) >= 5):
        for x in range(len(side)):
            if (x == len(side) - 3):
                #Positive number and positive number
                if (side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    side.insert(x, str(int(side[x]) * int(side[x + 2])))
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side = Multiplication(side)
                    break
                    
                #Positive number and positive variable
                elif (side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
                    if (len(side[x + 2] >= 2)):
                        numbers = FindNums(side[x + 2])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 2])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 2] < 2)):
                        side.insert(x, side[x] + side[x + 2])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                
                #Positive variable and positive number
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    if (len(side[x + 2] >= 2)):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x + 2]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x] < 2)):
                        side.insert(x, side[x] + side[x + 2])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                
                #Positive variable and positive variable
                elif (not side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
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
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, num + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
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
                        side = Multiplication(side)
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
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 2]) < 2):
                        var = MultiplyVars(side[x], side[x + 2])
                        side.insert(x, var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
            elif (x == len(side) - 4):
                #Positive number and negative number
                if (side[x].isdigit() and side[x + 1] == "*" and side[x + 2] == "-" and side[x + 3].isdigit()):
                    side.insert(x, "-")
                    side.insert(x + 1, str(int(side[x + 1]) * int(side[x + 4])))
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side = Multiplication(side)
                    break
                    
                #Negative number and positive number
                elif (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3].isdigit()):
                    side.insert(x + 1, str(int(side[x + 1]) * int(side[x + 3])))
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side = Multiplication(side)
                    break
                    
                #Positive number and negative variable
                elif(side[x].isdigit() and  side[x + 1] == "*" and side[x + 2] == "-" and not side[x + 3].isdigit()):
                    if (len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 3])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, "-")
                        side.insert(x + 1, str(int(side[x + 1]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 3]) < 2):
                        side.insert(x, "-")
                        side.insert(x + 1, side[x] + side[x + 3])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                
                #Negative number and positive variable
                elif (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "*" and not side[x + 3].isdigit()):
                    if (len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 3])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x + 1, str(int(side[x + 1]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 3]) < 2):
                        side.insert(x + 1, side[x + 1] + side[x + 3])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                
                #Positive variable and negative number
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2] == "-" and side[x + 3].isdigit()):
                    if (len(side[x]) >= 2):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, "-")
                        side.insert(x + 1, str(int(side[x + 4]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif(len(side[x]) < 2):
                        side.insert(x, "-")
                        side.insert(x + 1, side[x + 4] + side[x + 1])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                
                #Negative variable and positive number
                elif (side[x] == "-" and not side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3].isdigit()):
                    if (len(side[x + 1]) >= 2):
                        numbers = FindNums(side[x + 1])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side(x + 1, str(int(side[x + 3]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2):
                        side.insert(x + 1, side[x + 3] + side[x + 1])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and negative variable
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2] == "-" and not side[x + 3].isdigit()):
                    if (len(side[x]) >= 2 and len(side[x + 3]) >= 2):
                        numbers1 = FindNums(side[x])
                        num1 = ""
                        variables1 = FindVars(side[x])
                        numbers2 = FindNums(side[x + 3])
                        num2 = ""
                        variables2 = FindVars(side[x + 3])
                        
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
                            side.insert(x, "-")
                            side.insert(x + 1, var)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, "-")
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) >=2 and len(side[x + 3]) < 2):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x])
                        var = MultiplyVars(variables1, side[x + 3])
                        side.insert(x, "-")
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 3])
                        var = MultiplyVars(variables1, side[x])
                        side.insert(x, "-")
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 3]) < 2):
                        var = MultiplyVars(side[x], side[x + 3])
                        side.insert(x, "-")
                        side.insert(x + 1, var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Negative variable and positive variable
                elif (side[x] == "-" and not side[x + 1].isdigit() and side[x + 2] == "*" and not side[x + 3].isdigit()):
                    if (len(side[x + 1]) >= 2 and len(side[x + 3]) >= 2):
                        numbers1 = FindNums(side[x + 1])
                        num1 = ""
                        variables1 = FindVars(side[x + 1])
                        numbers2 = FindNums(side[x + 3])
                        num2 = ""
                        variables2 = FindVars(side[x + 3])
                        
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
                            side.insert(x + 1, var)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) >=2 and len(side[x + 3]) < 2):
                        numbers = FindNums(side[x + 1])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 1])
                        var = MultiplyVars(variables1, side[x + 3])
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2 and len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 3])
                        var = MultiplyVars(variables1, side[x + 1])
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2 and len(side[x + 3]) < 2):
                        var = MultiplyVars(side[x + 1], side[x + 3])
                        side.insert(x + 1, var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Positive number and positive number
                elif (side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    side.insert(x, str(int(side[x]) * int(side[x + 2])))
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side = Multiplication(side)
                    break
                    
                #Positive number and positive variable
                elif (side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
                    if (len(side[x + 2]) >= 2):
                        numbers = FindNums(side[x + 2])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 2])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 2]) < 2):
                        side.insert(x, side[x] + side[x + 2])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and positive number
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    if (len(side[x]) >= 2):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x + 2]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2):
                        side.insert(x, side[x + 2] + side[x])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and positive variable
                elif (not side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
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
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, num + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
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
                        side = Multiplication(side)
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
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 2]) < 2):
                        var = MultiplyVars(side[x], side[x + 2])
                        side.insert(x, var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
            elif (x < len(side) - 4):
                #Negative number and negative number
                if (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3] == "-" and side[x +4].isdigit()):
                    side.insert(x, str(int(side[x + 1]) * int(side[x + 4])))
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side = Multiplication(side)
                    break
                        
                #Negative number and negative variable    
                elif (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3] == "-" and not side[x + 4].isdigit()):
                    if (len(side[x + 4]) >= 2):
                        numbers = FindNums(side[x + 4])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 4])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x + 1]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 4]) < 2):
                        side.insert(x, side[x + 1] + side[x + 4])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
                #Negative variable and negative number        
                elif (side[x] == "-" and not side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3] == "-" and side[x + 4].isdigit()):
                    if (len(side[x + 1]) >= 2):
                        numbers = FindNums(side[x + 1])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 1])
                        var = ""
                        for z in range(len(numbers)):
                            var = var + variables
                        side.insert(x, str(int(side[x + 4]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2):
                        side.insert(x, side[x + 4] + side[x + 1])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    
                #Negative variable and negative variable
                elif (side[x] == "-" and not side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3] == "-" and not side[x + 4].isdigit()):
                    if (len(side[x + 1]) >= 2 and len(side[x + 4]) >= 2):
                        numbers1 = FindNums(side[x + 1])
                        num1 = ""
                        variables1 = FindVars(side[x + 1])
                        numbers2 = FindNums(side[x + 4])
                        num2 = ""
                        variables2 = FindVars(side[x + 4])
                        
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
                            side.pop(x + 1)
                            side.pop(x + 1)
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, num + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) >=2 and len(side[x+4]) < 2):
                        numbers = FindNums(side[x + 1])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 1])
                        var = MultiplyVars(variables1, side[x + 4])
                        side.insert(x, num + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2 and len(side[x + 4]) >= 2):
                        numbers = FindNums(side[x + 4])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 4])
                        var = MultiplyVars(variables1, side[x + 1])
                        side.insert(x, num + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2 and len(side[x + 4]) < 2):
                        var = MultiplyVars(side[x + 1], side[x + 4])
                        side.insert(x, var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
                #Positive number and negative number    
                elif (side[x].isdigit() and side[x + 1] == "*" and side[x + 2] == "-" and side[x + 3].isdigit()):
                    side.insert(x, "-")
                    side.insert(x + 1, str(int(side[x + 1]) * int(side[x + 4])))
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side = Multiplication(side)
                    break
                    
                #Negative number and positive number
                elif (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3].isdigit()):
                    side.insert(x + 1, str(int(side[x + 1]) * int(side[x + 3])))
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side.pop(x + 2)
                    side = Multiplication(side)
                    break
                    
                #Positive number and negative variable
                elif(side[x].isdigit() and  side[x + 1] == "*" and side[x + 2] == "-" and not side[x + 3].isdigit()):
                    if (len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 3])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, "-")
                        side.insert(x + 1, str(int(side[x + 1]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 3]) < 2):
                        side.insert(x, "-")
                        side.insert(x + 1, side[x] + side[x + 3])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Negative number and positive variable
                elif (side[x] == "-" and side[x + 1].isdigit() and side[x + 2] == "*" and not side[x + 3].isdigit()):
                    if (len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 3])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x + 1, str(int(side[x + 1]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 3]) < 2):
                        side.insert(x + 1, side[x + 1] + side[x + 3])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and negative number
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2] == "-" and side[x + 3].isdigit()):
                    if (len(side[x]) >= 2):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, "-")
                        side.insert(x + 1, str(int(side[x + 4]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif(len(side[x]) < 2):
                        side.insert(x, "-")
                        side.insert(x + 1, side[x + 4] + side[x + 1])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Negative variable and positive number
                elif (side[x] == "-" and not side[x + 1].isdigit() and side[x + 2] == "*" and side[x + 3].isdigit()):
                    if (len(side[x + 1]) >= 2):
                        numbers = FindNums(side[x + 1])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side(x + 1, str(int(side[x + 3]) * int(num)) + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2):
                        side.insert(x + 1, side[x + 3] + side[x + 1])
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and negative variable
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2] == "-" and not side[x + 3].isdigit()):
                    if (len(side[x]) >= 2 and len(side[x + 3]) >= 2):
                        numbers1 = FindNums(side[x])
                        num1 = ""
                        variables1 = FindVars(side[x])
                        numbers2 = FindNums(side[x + 3])
                        num2 = ""
                        variables2 = FindVars(side[x + 3])
                        
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
                            side.insert(x, "-")
                            side.insert(x + 1, var)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, "-")
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) >=2 and len(side[x + 3]) < 2):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x])
                        var = MultiplyVars(variables1, side[x + 3])
                        side.insert(x, "-")
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 3])
                        var = MultiplyVars(variables1, side[x])
                        side.insert(x, "-")
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 3]) < 2):
                        var = MultiplyVars(side[x], side[x + 3])
                        side.insert(x, "-")
                        side.insert(x + 1, var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                        
                #Negative variable and positive variable
                elif (side[x] == "-" and not side[x + 1].isdigit() and side[x + 2] == "*" and not side[x + 3].isdigit()):
                    if (len(side[x + 1]) >= 2 and len(side[x + 3]) >= 2):
                        numbers1 = FindNums(side[x + 1])
                        num1 = ""
                        variables1 = FindVars(side[x + 1])
                        numbers2 = FindNums(side[x + 3])
                        num2 = ""
                        variables2 = FindVars(side[x + 3])
                        
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
                            side.insert(x + 1, var)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side.pop(x + 2)
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) >=2 and len(side[x + 3]) < 2):
                        numbers = FindNums(side[x + 1])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 1])
                        var = MultiplyVars(variables1, side[x + 3])
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2 and len(side[x + 3]) >= 2):
                        numbers = FindNums(side[x + 3])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables1 = FindVars(side[x + 3])
                        var = MultiplyVars(variables1, side[x + 1])
                        side.insert(x + 1, num + var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 1]) < 2 and len(side[x + 3]) < 2):
                        var = MultiplyVars(side[x + 1], side[x + 3])
                        side.insert(x + 1, var)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side.pop(x + 2)
                        side = Multiplication(side)
                        break
                
                #Positive number and positive number
                elif (side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    side.insert(x, str(int(side[x]) * int(side[x + 2])))
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side.pop(x + 1)
                    side = Multiplication(side)
                    break
                    
                #Positive number and positive variable
                elif (side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
                    if (len(side[x + 2]) >= 2):
                        numbers = FindNums(side[x + 2])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x + 2])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x + 2]) < 2):
                        side.insert(x, side[x] + side[x + 2])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and positive number
                elif (not side[x].isdigit() and side[x + 1] == "*" and side[x + 2].isdigit()):
                    if (len(side[x]) >= 2):
                        numbers = FindNums(side[x])
                        num = ""
                        for y in range(len(numbers)):
                            num = num + numbers[y]
                        variables = FindVars(side[x])
                        var = ""
                        for z in range(len(variables)):
                            var = var + variables[z]
                        side.insert(x, str(int(side[x + 2]) * int(num)) + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2):
                        side.insert(x, side[x + 2] + side[x])
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
                        break
                        
                #Positive variable and positive variable
                elif (not side[x].isdigit() and side[x + 1] == "*" and not side[x + 2].isdigit()):
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
                            side = Multiplication(side)
                            break
                        
                        var = MultiplyVars(variables1, variables2)
                        side.insert(x, num + var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
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
                        side = Multiplication(side)
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
                        side = Multiplication(side)
                        break
                    elif (len(side[x]) < 2 and len(side[x + 2]) < 2):
                        var = MultiplyVars(side[x], side[x + 2])
                        side.insert(x, var)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side.pop(x + 1)
                        side = Multiplication(side)
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


#Multiply variables by variables
def MultiplyVars(variables1, variables2):
    boolean = False
    variables = []
    
    l1 = len(variables1)
    for a in range(len(variables1)):
        for b in range(len(variables2)):
            if (variables1[a] == variables2[b]):
                variables.append(variables1[a])
                variables1.pop(a)
                variables2.pop(b)
                boolean = True
                break
        if (boolean):
            break
    boolean = False
    l2 = len(variables1)
    while (l1 != l2):
        l1 = len(variables1)
        for a in range(len(variables1)):
            for b in range(len(variables2)):
                if (variables1[a] == variables2[b]):
                    variables.append(variables1[a])
                    variables1.pop(a)
                    variables2.pop(b)
                    boolean = True
                    break
            if (boolean):
                break
        l2 = len(variables1)
    
    squaredVars = []
    for x in range(len(variables)):
        squaredVars.append(variables[x])    
    
    for c in range(len(variables1)):
        variables.append(variables1[c])
    for d in range(len(variables2)):
        variables.append(variables2[d])
        
    for e in range(len(variables)):
        for f in range(len(variables)):
            if (e == f):
                break
            if (variables[f] < variables[e]):
                if (e < f):
                    storedVar = variables[e]
                    variables[e] = variables[f]
                    variables[f] = storedVar
            elif (variables[e] < variables[f]):
                if (f < e):
                    storedVar = variables[f]
                    variables[f] = variables[e]
                    variables[e] = storedVar
    var = ""
    for g in range(len(variables)):
        for h in range(len(squaredVars)):
            if (variables[g] == squaredVars[h]):
                var = var + variables[g] + "^2"
            else:
                var = var + variables[g]
    return var



side = ["3", "*", "4x", "*", "xyz", "*", "ay"]
print (side)
print (Multiplication(side))