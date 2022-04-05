import math
def isrational(num):
    if (int(num) == float(num)):
        return True
    decimal = num - int(num)
    if (decimal != 0.0):
        for x in range(1, 100001):
            ratio = x / 100000.0
            if (decimal == ratio):
                rational = True
            else:
                rational = False
            if (rational):
                return True
    return False
    
num = float(input("Enter a number:"))

print (num)
if (isrational(num)):
    print (str(num) + " is a rational number.\n")
else:
    print (str(num) + " is an irrational number.\n")
    
print (math.sqrt(num))
if (isrational(math.sqrt(num))):
    print (str(math.sqrt(num)) + " is a rational number.")
else:
    print (str(math.sqrt(num)) + " is an irrational number.")