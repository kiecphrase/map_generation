import random as r, math as m
import region

#######################################################################################
# Data                                                                                #
#######################################################################################

class ISLAND:
    def __init__(self):
        self.name = ""
        self.latitude = 0
        self.percipitation = 0
        self.regionNE = []
        self.regionNW = []
        self.regionSE = []
        self.regionSW = []

    def __str__(self):
        return f"name: {self.name} \nlatitude: {self.latitude} \npercipitation: {self.percipitation}"

#######################################################################################
# Functions                                                                           #
#######################################################################################

'''
generates name for island
'''
def generate_name():
    n = ""
    l = r.randint(1,20)

    lower = "qwertyuiopasdfghjklzxcvbnm"
    upper = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

    n = n + upper[m.trunc(len(upper) * r.random())]
    
    counter = 1
    while counter < l:
        n = n + lower[m.trunc(len(lower) * r.random())]
        counter += 1

    return(n)

'''
generates latitude for island. Temps for island based on latitude
'''
def lat():
    return(r.randint(0,90))


'''
generates percipitation level for island:

1 - infrequent annual percipitation
2 - seasonal percipitation (rainy seasions and dry seasons)
3 - monthly percipitation (~5 days a month on average recieve percipitation)
4 - heavy monthly percipitation (~5-10 days a month on average recieve significant percipitation, other days may have some insignificant percipitation)
5 - rainforest (rainforest-like conditions on the island)
'''
def perc():
    return(r.randint(1,5))

def generate_island():
    x = ISLAND()
    x.name = generate_name()
    x.latitude = lat()
    x.percipitation = perc()
    x.regionNE = region.create_region(1)
    x.regionNW = region.create_region(2)
    x.regionSW = region.create_region(3)
    x.regionSE = region.create_region(4)

    return x


#######################################################################################
# Testing                                                                             #
#######################################################################################
test_island = generate_island()
print(test_island)
print(f"{test_island.regionNW.one[0]} {test_island.regionNW.one[1]} {test_island.regionNW.one[2]} {test_island.regionNW.one[3]} {test_island.regionNW.one[4]} {test_island.regionNE.one[0]} {test_island.regionNE.one[1]} {test_island.regionNE.one[2]} {test_island.regionNE.one[3]} {test_island.regionNE.one[4]}")
print(f"{test_island.regionNW.two[0]} {test_island.regionNW.two[1]} {test_island.regionNW.two[2]} {test_island.regionNW.two[3]} {test_island.regionNW.two[4]} {test_island.regionNE.two[0]} {test_island.regionNE.two[1]} {test_island.regionNE.two[2]} {test_island.regionNE.two[3]} {test_island.regionNE.two[4]}")
print(f"{test_island.regionNW.three[0]} {test_island.regionNW.three[1]} {test_island.regionNW.three[2]} {test_island.regionNW.three[3]} {test_island.regionNW.three[4]} {test_island.regionNE.three[0]} {test_island.regionNE.three[1]} {test_island.regionNE.three[2]} {test_island.regionNE.three[3]} {test_island.regionNE.three[4]}")
print(f"{test_island.regionNW.four[0]} {test_island.regionNW.four[1]} {test_island.regionNW.four[2]} {test_island.regionNW.four[3]} {test_island.regionNW.four[4]} {test_island.regionNE.four[0]} {test_island.regionNE.four[1]} {test_island.regionNE.four[2]} {test_island.regionNE.four[3]} {test_island.regionNE.four[4]}")
print(f"{test_island.regionNW.five[0]} {test_island.regionNW.five[1]} {test_island.regionNW.five[2]} {test_island.regionNW.five[3]} {test_island.regionNW.five[4]} {test_island.regionNE.five[0]} {test_island.regionNE.five[1]} {test_island.regionNE.five[2]} {test_island.regionNE.five[3]} {test_island.regionNE.five[4]}")
print(f"{test_island.regionSW.one[0]} {test_island.regionSW.one[1]} {test_island.regionSW.one[2]} {test_island.regionSW.one[3]} {test_island.regionSW.one[4]} {test_island.regionSE.one[0]} {test_island.regionSE.one[1]} {test_island.regionSE.one[2]} {test_island.regionSE.one[3]} {test_island.regionSE.one[4]}")
print(f"{test_island.regionSW.two[0]} {test_island.regionSW.two[1]} {test_island.regionSW.two[2]} {test_island.regionSW.two[3]} {test_island.regionSW.two[4]} {test_island.regionSE.two[0]} {test_island.regionSE.two[1]} {test_island.regionSE.two[2]} {test_island.regionSE.two[3]} {test_island.regionSE.two[4]}")
print(f"{test_island.regionSW.three[0]} {test_island.regionSW.three[1]} {test_island.regionSW.three[2]} {test_island.regionSW.three[3]} {test_island.regionSW.three[4]} {test_island.regionSE.three[0]} {test_island.regionSE.three[1]} {test_island.regionSE.three[2]} {test_island.regionSE.three[3]} {test_island.regionSE.three[4]}")
print(f"{test_island.regionSW.four[0]} {test_island.regionSW.four[1]} {test_island.regionSW.four[2]} {test_island.regionSW.four[3]} {test_island.regionSW.four[4]} {test_island.regionSE.four[0]} {test_island.regionSE.four[1]} {test_island.regionSE.four[2]} {test_island.regionSE.four[3]} {test_island.regionSE.four[4]}")
print(f"{test_island.regionSW.five[0]} {test_island.regionSW.five[1]} {test_island.regionSW.five[2]} {test_island.regionSW.five[3]} {test_island.regionSW.five[4]} {test_island.regionSE.five[0]} {test_island.regionSE.five[1]} {test_island.regionSE.five[2]} {test_island.regionSE.five[3]} {test_island.regionSE.five[4]}")
