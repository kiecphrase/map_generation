import random as r, math as m

#######################################################################################
# Data                                                                                #
#######################################################################################

class REGION ():
    def __init__(self):
        self.r = 0
        self.one = []
        self.two = []
        self.three = []
        self.four = []
        self.five = []

'''
Land Types:
O = Ocean
L = Lake
M = Mountain
H = Hills
F = Forest
G = Grassland
D = Desert

'''

#######################################################################################
# Functions                                                                           #
#######################################################################################

def generate_spot(t):
    x = ""
    vals = []
    choice = r.randint(0,101)

    if t == True:
        vals = [25,27,40,65,80,100]
    else:
        vals = [1,15,27,47,77,100]

    if choice < vals[0]:
        x="O"
    elif choice < vals[1]:
        x="L"
    elif choice < vals[2]:
        x="M"
    elif choice < vals[3]:
        x="H"
    elif choice < vals[4]:
        x="F"
    elif choice < vals[5]:
        x="G"
    else:
        x="D"


    return(x)

def generate_row(oceanRow, oceanColumn):
    x = []
    i = 0

    while i < 5:
        if oceanRow:
            x.append("O")
        elif i == oceanColumn:
            x.append("O")
        else:
            if oceanColumn == 0:
                if i == 1:
                    x.append(generate_spot(True))
                else:
                    x.append(generate_spot(False))
            else:
                if i == 3:
                    x.append(generate_spot(True))
                else:
                    x.append(generate_spot(False))

        i += 1

    return(x)

def create_region(rVal):
    x = REGION()
    x.r = rVal

    # create all the stuff
    oceancolumn = 0

    if x.r == 1 or x.r == 4:
        oceancolumn = 4

    if x.r == 1 or x.r == 2:
        x.one = generate_row(True, oceancolumn)
    else:
        x.one = generate_row(False, oceancolumn)

    x.two = generate_row(False, oceancolumn)
    x.three = generate_row(False, oceancolumn)
    x.four = generate_row(False, oceancolumn)
    
    if x.r == 3 or x.r == 4:
        x.five = generate_row(True, oceancolumn)
    else:
        x.five = generate_row(False, oceancolumn)

    return(x)

#######################################################################################
# Testing                                                                             #
#######################################################################################

print("spot generation not next to ocean row")
test_count = 0
while test_count < 10:
    print(generate_spot(False))
    test_count += 1

print(" ")

print("spot generation next to ocean row")
test_count = 0
while test_count < 10:
    print(generate_spot(True))
    test_count += 1

print(" ")

print("Row Generation Ocean Row")
test_row = []
test_row = generate_row(True, 0)
print(f"{test_row[0]} {test_row[1]} {test_row[2]} {test_row[3]} {test_row[4]}")

print(" ")

print("Row Generation Non Ocean Row")
test_row = []
test_row = generate_row(False, 0)
print(f"{test_row[0]} {test_row[1]} {test_row[2]} {test_row[3]} {test_row[4]}")

print(" ")

print("Row Generation Non Ocean Row Alt")
test_row = []
test_row = generate_row(False, 4)
print(f"{test_row[0]} {test_row[1]} {test_row[2]} {test_row[3]} {test_row[4]}")

print(" ")

print("Generate NE Region")
test_region = create_region(1)
print(f"{test_region.one[0]} {test_region.one[1]} {test_region.one[2]} {test_region.one[3]} {test_region.one[4]}")
print(f"{test_region.two[0]} {test_region.two[1]} {test_region.two[2]} {test_region.two[3]} {test_region.two[4]}")
print(f"{test_region.three[0]} {test_region.three[1]} {test_region.three[2]} {test_region.three[3]} {test_region.three[4]}")
print(f"{test_region.four[0]} {test_region.four[1]} {test_region.four[2]} {test_region.four[3]} {test_region.four[4]}")
print(f"{test_region.five[0]} {test_region.five[1]} {test_region.five[2]} {test_region.five[3]} {test_region.five[4]}")

print(" ")

print("Generate NW Region")
test_region = create_region(2)
print(f"{test_region.one[0]} {test_region.one[1]} {test_region.one[2]} {test_region.one[3]} {test_region.one[4]}")
print(f"{test_region.two[0]} {test_region.two[1]} {test_region.two[2]} {test_region.two[3]} {test_region.two[4]}")
print(f"{test_region.three[0]} {test_region.three[1]} {test_region.three[2]} {test_region.three[3]} {test_region.three[4]}")
print(f"{test_region.four[0]} {test_region.four[1]} {test_region.four[2]} {test_region.four[3]} {test_region.four[4]}")
print(f"{test_region.five[0]} {test_region.five[1]} {test_region.five[2]} {test_region.five[3]} {test_region.five[4]}")

print(" ")

print("Generate SW Region")
test_region = create_region(3)
print(f"{test_region.one[0]} {test_region.one[1]} {test_region.one[2]} {test_region.one[3]} {test_region.one[4]}")
print(f"{test_region.two[0]} {test_region.two[1]} {test_region.two[2]} {test_region.two[3]} {test_region.two[4]}")
print(f"{test_region.three[0]} {test_region.three[1]} {test_region.three[2]} {test_region.three[3]} {test_region.three[4]}")
print(f"{test_region.four[0]} {test_region.four[1]} {test_region.four[2]} {test_region.four[3]} {test_region.four[4]}")
print(f"{test_region.five[0]} {test_region.five[1]} {test_region.five[2]} {test_region.five[3]} {test_region.five[4]}")

print(" ")

print("Generate SE Region")
test_region = create_region(4)
print(f"{test_region.one[0]} {test_region.one[1]} {test_region.one[2]} {test_region.one[3]} {test_region.one[4]}")
print(f"{test_region.two[0]} {test_region.two[1]} {test_region.two[2]} {test_region.two[3]} {test_region.two[4]}")
print(f"{test_region.three[0]} {test_region.three[1]} {test_region.three[2]} {test_region.three[3]} {test_region.three[4]}")
print(f"{test_region.four[0]} {test_region.four[1]} {test_region.four[2]} {test_region.four[3]} {test_region.four[4]}")
print(f"{test_region.five[0]} {test_region.five[1]} {test_region.five[2]} {test_region.five[3]} {test_region.five[4]}")