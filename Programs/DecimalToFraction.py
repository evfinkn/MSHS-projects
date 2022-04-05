def GCF (nums):
    c = 0
    factors = []
    for a in range(len(nums)):
        factors.append([])
        for x in range(nums[a], 0, -1):
            if (nums[a] % x == 0):
                factors[c].append(x)
        c = c + 1
    for fctr in factors[0]:
        if all(fctr in f for f in factors):
            return fctr

def decToFrac(dec):
    for x in range(1, 100001):
        if (x / 100000.0 == dec):
            comFctr = GCF([x, 100000])
            return [x/comFctr, 100000/comFctr]
    
decimal = float(input("Enter a decimal:"))
fraction = decToFrac(decimal)
print (str(fraction[0]) + "/" + str(fraction[1]) + " = " + str(decimal))