import math
def findNeg(num):
    tempNum = num
    tempNum = tempNum.replace("", " ")
    tempNum = tempNum.split(" ")
    tempNum.pop(0)
    tempNum.pop(len(tempNum) - 1)
    num = ""
    if (tempNum[0] == "-"):
        for x in range(1, len(tempNum)):
            num += tempNum[x]
        num = -float(num)
        return num
    else:
        for x in range(0, len(tempNum)):
            num += tempNum[x]
        num = float(num)
        return num

def quadraticFormula(a, b, c):
    x1 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt((b ** 2) - 4 * a * c)) / 2 * a
    solution = [x1, x2]
    return solution
    

#MAIN
a = input("What is \'a\' in \'ax^2 + bx + c = 0\'")
b = input("What is \'b\' in \'ax^2 + bx + c = 0\'")
c = input("What is \'c\' in \'ax^2 + bx + c = 0\'")

a = findNeg(a)
b = findNeg(b)
c = findNeg(c)

solution = quadraticFormula(a, b, c)
print ("x = " + str(solution[0]) + " or x = " + str(solution[1]))