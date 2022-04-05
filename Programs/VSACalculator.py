#Volume & Surface Area Calculator

def prismSA(mode):
    mode = input("What mode would you like to use? (fast / complete)  |  Fast mode asks you to find the perimeter of the base, area of the base, etc. Best for when the dimensions of the shape are simple.  |  Complete mode asks for the shape of the base, and then the dimensions of the shape.")
    mode = mode.lower()
    if (mode == "fast" or mode == "f"):
        bPerimeter = float(input("What is the perimeter of the base?"))
        bArea = float(input("What is the area of the base?"))
        pHeight = float(input("What is the height of the prism?"))
        surfaceArea = bPerimeter * pHeight + 2 * bArea
        return surfaceArea
    elif (mode == "complete" or mode == "c"):   
        baseShape = input("What is the shape of the base? (triangle, square, rectangle, regular pentagon, regular hexagon)")
        baseShape = baseShape.lower()
        if (baseShape == "triangle" or baseShape == "t"):
            tSide1 = float(input("What is the length of the base of the triangle?"))
            tSide2 = float(input("What is the length of the 2nd side of the triangle?"))
            tSide3 = float(input("What is the length of the 3rd side of the triangle?"))
            tPerimeter = tSide1 + tSide2 + tSide3
            tHeight = float(input("What is the height of the triangle?"))
            tArea = tSide1 * tHeight / 2
            pHeight = float(input("What is the height of the prism?"))
            surfaceArea = tPerimeter * pHeight + 2 * tArea
            return surfaceArea
        elif (baseShape == "square" or baseShape == "s"):
            sSide = float(input("What is the length of a side of the square?"))
            sPerimeter = sSide * 4
            sArea = sSide ** 2
            pHeight = float(input("What is the height of the prism?"))
            surfaceArea = sPerimeter * pHeight + 2 * sArea
            return surfaceArea
        elif (baseShape == "rectangle" or baseShape == "r"):
            rLength = float(input("What is the length of the rectangle?"))
            rWidth = float(input("What is the width of the rectangle?"))
            rPerimeter = rLength * 2 + rWidth * 2
            rArea = rLength * rWidth
            pHeight = float(input("What is the height of the prism?"))
            surfaceArea = rPerimeter * pHeight + 2 * rArea
            return surfaceArea
        elif (baseShape == "pentagon" or baseShape == "p" or baseShape == "regular pentagon"):
            pSide = float(input("What is the length of a side of the pentagon?"))
            pArea = (1.0/4.0) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pSide ** 2
            pPerimeter = pSide * 5
            pHeight = float(input("What is the height of the prism?"))
            surfaceArea = pPerimeter * pHeight + 2 * pArea
            return surfaceArea
        elif (baseShape == "hexagon" or baseShape == "h" or baseShape == "regular hexagon"):
            hSide = float(input("What is the length of a side of the pentagon?"))
            hArea = (3 * math.sqrt(3)) / 2 * hSide ** 2
            hPerimeter = hSide * 6
            pHeight = float(input("What is the height of the prism?"))
            surfaceArea = hPerimeter * pHeight + 2 * hArea
            return surfaceArea
def pyramidSA(mode):
    mode = input("What mode would you like to use? (fast / complete)  |  Fast mode asks you to find the perimeter of the base, area of the base, etc. Best for when the dimensions of the shape are simple.  |  Complete mode asks for the shape of the base, and then the dimensions of the shape.")
    mode = mode.lower()
    if (mode == "fast" or mode == "f"):
        bPerimeter = float(input("What is the perimeter of the base?"))
        bArea = float(input("What is the area of the base?"))
        pSlantHeight = float(input("What is the slant height of the pyramid?"))
        surfaceArea = 0.5 * bPerimeter * pSlantHeight + bArea
        return surfaceArea
    elif (mode == "complete" or mode == "c"):   
        baseShape = input("What is the shape of the base? (triangle, square, rectangle, regular pentagon, regular hexagon)")
        baseShape = baseShape.lower()
        if (baseShape == "triangle" or baseShape == "t"):
            tSide1 = float(input("What is the length of the base of the triangle?"))
            tSide2 = float(input("What is the length of the 2nd side of the triangle?"))
            tSide3 = float(input("What is the length of the 3rd side of the triangle?"))
            tPerimeter = tSide1 + tSide2 + tSide3
            tHeight = float(input("What is the height of the triangle?"))
            tArea = tSide1 * tHeight / 2
            pSlantHeight = float(input("What is the slant height of the pyramid?"))
            surfaceArea = 0.5 * tPerimeter * pSlantHeight + tArea
            return surfaceArea
        elif (baseShape == "square" or baseShape == "s"):
            sSide = float(input("What is the length of a side of the square?"))
            sPerimeter = sSide * 4
            sArea = sSide ** 2
            pSlantHeight = float(input("What is the slant height of the pyramid?"))
            surfaceArea = 0.5 * sPerimeter * pSlantHeight + sArea
            return surfaceArea
        elif (baseShape == "rectangle" or baseShape == "r"):
            rLength = float(input("What is the length of the rectangle?"))
            rWidth = float(input("What is the width of the rectangle?"))
            rPerimeter = rLength * 2 + rWidth * 2
            rArea = rLength * rWidth
            pSlantHeight = float(input("What is the slant height of the pyramid?"))
            surfaceArea = 0.5 * rPerimeter * pSlantHeight + rArea
            return surfaceArea
        elif (baseShape == "pentagon" or baseShape == "p" or baseShape == "regular pentagon"):
            pSide = float(input("What is the length of a side of the pentagon?"))
            pArea = (1.0/4.0) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pSide ** 2
            pPerimeter = pSide * 5
            pSlantHeight = float(input("What is the slant height of the pyramid?"))
            surfaceArea = 0.5 * pPerimeter * pSlantHeight + pArea
            return surfaceArea
        elif (baseShape == "hexagon" or baseShape == "h" or baseShape == "regular hexagon"):
            hSide = float(input("What is the length of a side of the pentagon?"))
            hArea = (3 * math.sqrt(3)) / 2 * hSide ** 2
            hPerimeter = hSide * 6
            pSlantHeight = float(input("What is the slant height of the pyramid?"))
            surfaceArea = 0.5 * hPerimeter * pSlantHeight + hArea
            return surfaceArea
def coneSA(mode):
    radius = float(input("What is the radius?"))
    slantHeight = float(input("What is the slant height?"))
    surfaceArea = math.pi * radius * slantHeight + math.pi * radius ** 2
    return surfaceArea
def sphereSA(mode):
    radius = float(input("What is the radius?"))
    surfaceArea = 4 * math.pi * radius ** 2
    return surfaceArea
def cylinderSA(mode):
    radius = float(input("What is the radius?"))
    height = float(input("What is the height?"))
    surfaceArea = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    return surfaceArea   


def prismV(mode):
    mode = input("What mode would you like to use? (fast / complete)  |  Fast mode asks you to find the area of the base. Best for when the dimensions of the shape are simple.  |  Complete mode asks for the shape of the base, and then the dimensions of the shape.")
    mode = mode.lower()
    if (mode == "fast" or mode == "f"):
        bArea = float(input("What is the area of the base?"))
        pHeight = float(input("What is the height of the prism?"))
        volume = bArea * pHeight
        return volume
    elif (mode == "complete" or mode == "c"):   
        baseShape = input("What is the shape of the base? (triangle, square, rectangle, regular pentagon, regular hexagon)")
        baseShape = baseShape.lower()
        if (baseShape == "triangle" or baseShape == "t"):
            tSide = float(input("What is the base of the triangle?"))
            tHeight = float(input("What is the height of the triangle?"))
            tArea = tSide1 * tHeight / 2
            pHeight = float(input("What is the height of the prism?"))
            volume = pHeight * tArea
            return volume
        elif (baseShape == "square" or baseShape == "s"):
            sSide = float(input("What is the length of a side of the square?"))
            sArea = sSide ** 2
            pHeight = float(input("What is the height of the prism?"))
            volume = pHeight * sArea
            return volume
        elif (baseShape == "rectangle" or baseShape == "r"):
            rLength = float(input("What is the length of the rectangle?"))
            rWidth = float(input("What is the width of the rectangle?"))
            rArea = rLength * rWidth
            pHeight = float(input("What is the height of the prism?"))
            volume = pHeight * rArea
            return volume
    	elif (baseShape == "pentagon" or baseShape == "p" or baseShape == "regular pentagon"):
            pSide = float(input("What is the length of a side of the pentagon?"))
            pArea = (1.0/4.0) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pSide ** 2
            pHeight = float(input("What is the height of the prism?"))
            volume = pHeight * pArea
            return volume
        elif (baseShape == "hexagon" or baseShape == "h" or baseShape == "regular hexagon"):
            hSide = float(input("What is the length of a side of the pentagon?"))
            hArea = (3 * math.sqrt(3)) / 2 * hSide ** 2
            pHeight = float(input("What is the height of the prism?"))
            volume = pHeight * hArea
            return volume
def pyramidV(mode):
    mode = input("What mode would you like to use? (fast / complete)  |  Fast mode asks you to find the perimeter of the base, area of the base, etc. Best for when the dimensions of the shape are simple.  |  Complete mode asks for the shape of the base, and then the dimensions of the shape.")
    mode = mode.lower()
    if (mode == "fast" or mode == "f"):
        bArea = float(input("What is the area of the base?"))
        pHeight = float(input("What is the height of the pyramid?"))
        volume = (1.0/3.0) * bArea * pHeight
        return volume
    elif (mode == "complete" or mode == "c"):   
        baseShape = input("What is the shape of the base? (triangle, square, rectangle, regular pentagon, regular hexagon)")
        baseShape = baseShape.lower()
        if (baseShape == "triangle" or baseShape == "t"):
            tSide1 = float(input("What is the length of the base of the triangle?"))
            tHeight = float(input("What is the height of the triangle?"))
            tArea = tSide1 * tHeight / 2
            pHeight = float(input("What is the height of the pyramid?"))
            volume = (1.0/3.0) * tArea * pHeight
            return volume
        elif (baseShape == "square" or baseShape == "s"):
            sSide = float(input("What is the length of a side of the square?"))
            sArea = sSide ** 2
            pHeight = float(input("What is the height of the pyramid?"))
            volume = (1.0/3.0) * sArea * pHeight
            return volume
        elif (baseShape == "rectangle" or baseShape == "r"):
            rLength = float(input("What is the length of the rectangle?"))
            rWidth = float(input("What is the width of the rectangle?"))
            rArea = rLength * rWidth
            pHeight = float(input("What is the height of the pyramid?"))
            volume = (1.0/3.0) * rArea * pHeight
            return volume
        elif (baseShape == "pentagon" or baseShape == "p" or baseShape == "regular pentagon"):
            pSide = float(input("What is the length of a side of the pentagon?"))
            pArea = (1.0/4.0) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pSide ** 2
            pHeight = float(input("What is the height of the pyramid?"))
            volume = (1.0/3.0) * pArea * pHeight
            return volume
        elif (baseShape == "hexagon" or baseShape == "h" or baseShape == "regular hexagon"):
            hSide = float(input("What is the length of a side of the pentagon?"))
            hArea = (3 * math.sqrt(3)) / 2 * hSide ** 2
            pHeight = float(input("What is the height of the pyramid?"))
            volume = (1.0/3.0) * hArea * pHeight
            return volume
def coneV(mode):
    radius = float(input("What is the radius?"))
    bArea = math.pi * radius ** 2
    height = float(input("What is the height?"))
    volume = (1.0/3.0) * bArea * height
    return volume
def sphereV(mode):
    radius = float(input("What is the radius?"))
    volume = (4.0/3.0) * math.pi * radius ** 3
    return volume
def cylinderV(mode):
    radius = float(input("What is the radius?"))
    height = float(input("what is the height?"))
    volume = math.pi * (radius ** 2) * height
    
    
find = input("Would you like to find volume or surface area?")
shape = input("What is the shape? (prism, pyramid, cone, sphere, or cylinder)")
                    
find = find.lower()
shape = shape.lower()

if (find == "sa" or find == "surface area"):
    if (shape == "prism"):
        surfaceArea = prismSA()
        print ("The surface area is: " + str(round(surfaceArea)) + "\n(" + str(surfaceArea) + ")")
    elif (shape == "pyramid"):
        surfaceArea = pyramidSA()
        print ("The surface area is: " + str(round(surfaceArea)) + "\n(" + str(surfaceArea) + ")")
    elif (shape == "cone"):
        surfaceArea = coneSA()
        print ("The surface area is: " + str(round(surfaceArea)) + "\n(" + str(surfaceArea) + ")")
    elif (shape == "sphere"):
        surfaceArea = sphereSA()
        print ("The surface area is: " + str(round(surfaceArea)) + "\n(" + str(surfaceArea) + ")")
    elif (shape == "cylinder"):
        surfaceArea = cylinderSA
        print ("The surface area is: " + str(round(surfaceArea)) + "\n(" + str(surfaceArea) + ")")

elif (find == "v" or find == "volume"):
    if (shape == "prism"):
        volume = prismV()
        print ("The volume is: " + str(round(volume)) + "\n(" + str(volume) + ")")
    elif (shape == "pyramid"):
        volume = pyramidV()
        print ("The volume is: " + str(round(volume)) + "\n(" + str(volume) + ")")
    elif (shape == "cone"):
        volume = coneV()
        print ("The volume is: " + str(round(volume)) + "\n(" + str(volume) + ")")
    elif (shape == "sphere"):
        volume = sphereV()
        print ("The volume is: " + str(round(volume)) + "\n(" + str(volume) + ")")
    elif (shape == "cylinder"):
        volume = cylinderV()
        print ("The volume is: " + str(round(volume)) + "\n(" + str(volume) + ")")
    
    
    
