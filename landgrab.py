import random as r, math as m

#######################################################################################
# Functions                                                                           #
#######################################################################################

'''
calculate random percipitation bonus

'''
def perc():
    return(r.randint(1,3))


'''
calculate the base weighted values for determining new land based on what land is around it

tiles = [tile to left, tile directly above, tile up and to the left]
vals = weighted values for land generation

    Land Types:
    O = Ocean
    L = Lake
    M = Mountain
    H = Hills
    F = Forest
    G = Grassland
    D = Desert

'''
def weighted(tiles=["O","O","O"]):

    vals = [1,1,1,1,1,1,1] #ocean, lake, mountain, hills, forest, grassland, desert

    for t in tiles:
        if t == "O":
            gals = [3,1,2,2,1,1,1]
        elif t == "L":
            gals = [1,3,2,2,2,2,1]
        elif t == "M":
            gals = [1,2,3,2,1,1,1]
        elif t == "H":
            gals = [1,1,2,2,1,1,1]
        elif t == "F":
            gals = [1,1,1,2,3,2,1]
        elif t == "G":
            gals = [1,2,1,1,2,3,1]
        else:
            gals = [1,1,1,1,1,3,3]

        count = 0
        while count < len(vals):
            vals[count] += gals[count]
            
            count +=1

    return vals


'''
adds percipitation bonus to weighted values for calculating land

lisp = list of weighted values
pman = percipitation modification bonus

'''
def mod_perc(lisp, pman):
    lisp[0] += pman
    lisp[1] += pman

    return lisp


'''
returns a tile selected from the weighted values

v = percipitation modified weighted values for land generation
x = selected land
max_val = sum of all weighted values
choice = random value between 0 and the max_val
sums = list of weighted values for land generation
select = list of potential land values that coorilate to the sums
gotcha = boolean value to determine if the tile has been selected

'''
def get_tile(v = []):
    x = "Z"
    max_val = 0
    choice = 0
    sums = []
    select = ["O","L","M","H","F","G","D"]
    gotcha = True

    for i in v:
        max_val += i
        sums.append(max_val)
    
    choice = r.randint(0,max_val)

    j = 0
    while j < len(sums) and gotcha:
        if choice <= sums[j]:
            gotcha = False
            x = select[j]

        j += 1
    
    return x


'''
Bureau of Land Management function that generates the new world map based on weighted averages and random chance

land = imported blank map with surrounding ocean
sip = percipitation bonus
rowcount = current row in lands
new_lands = newly generated map
curent_row = list of land tiles of the current row
tilecount = counter to go through each land tile
t = value of current tile
values_for_tiles = weighted values for land generation
row_above = list of tiles one row above current_row 

'''
def BLM(land, sip):
    rowcount = 0
    new_lands = []

    while rowcount < len(land): # each row of land
        current_row = land[rowcount]
        tilecount = 0
        values_for_tiles = []

        while tilecount < len(current_row): #each tile in row
            row_above = land[rowcount-1]
            t = current_row[tilecount]
            
            if t == "Z":
                values_for_tiles = weighted([current_row[tilecount-1],row_above[tilecount], row_above[tilecount-1]])
                values_for_tiles = mod_perc(values_for_tiles, sip)
                current_row[tilecount] = get_tile(values_for_tiles)

            tilecount += 1

        new_lands.append(current_row)
        rowcount += 1

    return(new_lands)


'''
generate a new map and percipitation level for new world
x = [new map, percipitation level]

'''
def make (land = None):
    x = [[],0]
    
    x[1] = perc()

    # okay so now with percipitation and in theory, all the land, make some sweet maps 
    if land != None:
        x[0] = BLM(land, x[1])

    return x

#######################################################################################
# Testing                                                                             #
#######################################################################################
print('weights testing (default)')
v = weighted()
print(v)

print(' ')
print('weights testing (O,G,M)')
v = weighted(["O","G","M"])
print(v)

print(' ')
print('weights testing (D,D,D)')
v = weighted(["D","D","D"])
print(v)