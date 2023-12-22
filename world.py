import random as r, math as m
import landgrab as l
#######################################################################################
# Data                                                                                #
#######################################################################################

class SIMPLEWORLD:
    def __init__(self):
        self.name = ""
        self.percipitation = 0
        self.land = []

    def __str__(self):
        return f"name: {self.name}"
    

#######################################################################################
# Functions                                                                           #
#######################################################################################

'''
generate a blank map canvas that is an 18 * 18 grid

'''
def simple_map_static():
    x = []
    i = 0

    while i < 18:
        x.append(["Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z"])
        i+=1
    
    return x

'''
generate a blank map canvas that is a user defined size. (works best in multiples of 3)

lat = the total amount of rows
lng = the total amount of columns

'''
def simple_map_dynamic(lat,lng):
    x = []
    i = 0

    while i < lat:
        y = []
        j = 0

        while j < lng:
            y.append("Z")
            j+=1

        x.append(y)
        i+=1

    return x

'''
generate map canvas with ocean boarder. Size of map either based on static or dynamic map generation

boo = boolean to determine static or dynamic map generation
lat = total number of rows
lng = total number of columns

'''
def with_ocean_boarder(boo = True, lat = 0, lng = 0):
    i = 0

    if boo:
        x = simple_map_static()
        lat = 18
    else:
        x = simple_map_dynamic(lat, lng)


    for lattitudes in x:
        
        if i == 0 or i == lat-1:
            j = 0
            while j < len(lattitudes):
                lattitudes[j] = "O"
                j+=1

            
        else:
            lattitudes[0] = "O"
            lattitudes[len(lattitudes)-1] = "O"
        
        i += 1
    
    return x


def generate_world():
    x = SIMPLEWORLD()

    x.land = with_ocean_boarder()

    # intelligently generate land
    hold = l.make(x.land)
    x.land = hold[0]
    x.percipitation = hold[1]

    return x

#######################################################################################
# Testing                                                                             #
#######################################################################################

print("18 x 18 world simple static map test")
teest = simple_map_static()

for t in teest:
    print(t)

print(" ")
print("dynamic map test 18 x 18")
peest = simple_map_dynamic(18,18)

for p in peest:
    print(p)

print(" ")
print("dynamic map test 13 x 7")
geest = simple_map_dynamic(13,7)

for g in geest:
    print(g)

print(" ")
print("ocean boarder static map test")
quest = with_ocean_boarder(True)
for qu in quest:
    print(qu)

print(" ")
print("ocean boarder dynamic map test 18 x 18")
best = with_ocean_boarder(False, 18, 18)
for b in best:
    print(b)

print(" ")
print("ocean boarder dynamic map test 14 x 8")
jest = with_ocean_boarder(False, 14, 8)
for j in jest:
    print(j)

print(" ")
print("worl generation test with all in one function")

funk = generate_world()

funky = funk.land

for f in funky:
    print(f)