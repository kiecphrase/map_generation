import island as w

print("we will now generate a world for you!")
user_in = str(input("name of file to create (include .txt): \n"))

f = open(user_in, "w")

print("now generating your world")

generated_world = w.generate_island()

print("your world has been successfully generated!")
print(f"your world: {generated_world}")

f.write(f"{generated_world}\n")
f.write(f"{generated_world.regionNW.one[0]} {generated_world.regionNW.one[1]} {generated_world.regionNW.one[2]} {generated_world.regionNW.one[3]} {generated_world.regionNW.one[4]} {generated_world.regionNE.one[0]} {generated_world.regionNE.one[1]} {generated_world.regionNE.one[2]} {generated_world.regionNE.one[3]} {generated_world.regionNE.one[4]}\n")
f.write(f"{generated_world.regionNW.two[0]} {generated_world.regionNW.two[1]} {generated_world.regionNW.two[2]} {generated_world.regionNW.two[3]} {generated_world.regionNW.two[4]} {generated_world.regionNE.two[0]} {generated_world.regionNE.two[1]} {generated_world.regionNE.two[2]} {generated_world.regionNE.two[3]} {generated_world.regionNE.two[4]}\n")
f.write(f"{generated_world.regionNW.three[0]} {generated_world.regionNW.three[1]} {generated_world.regionNW.three[2]} {generated_world.regionNW.three[3]} {generated_world.regionNW.three[4]} {generated_world.regionNE.three[0]} {generated_world.regionNE.three[1]} {generated_world.regionNE.three[2]} {generated_world.regionNE.three[3]} {generated_world.regionNE.three[4]}\n")
f.write(f"{generated_world.regionNW.four[0]} {generated_world.regionNW.four[1]} {generated_world.regionNW.four[2]} {generated_world.regionNW.four[3]} {generated_world.regionNW.four[4]} {generated_world.regionNE.four[0]} {generated_world.regionNE.four[1]} {generated_world.regionNE.four[2]} {generated_world.regionNE.four[3]} {generated_world.regionNE.four[4]}\n")
f.write(f"{generated_world.regionNW.five[0]} {generated_world.regionNW.five[1]} {generated_world.regionNW.five[2]} {generated_world.regionNW.five[3]} {generated_world.regionNW.five[4]} {generated_world.regionNE.five[0]} {generated_world.regionNE.five[1]} {generated_world.regionNE.five[2]} {generated_world.regionNE.five[3]} {generated_world.regionNE.five[4]}\n")
f.write(f"{generated_world.regionSW.one[0]} {generated_world.regionSW.one[1]} {generated_world.regionSW.one[2]} {generated_world.regionSW.one[3]} {generated_world.regionSW.one[4]} {generated_world.regionSE.one[0]} {generated_world.regionSE.one[1]} {generated_world.regionSE.one[2]} {generated_world.regionSE.one[3]} {generated_world.regionSE.one[4]}\n")
f.write(f"{generated_world.regionSW.two[0]} {generated_world.regionSW.two[1]} {generated_world.regionSW.two[2]} {generated_world.regionSW.two[3]} {generated_world.regionSW.two[4]} {generated_world.regionSE.two[0]} {generated_world.regionSE.two[1]} {generated_world.regionSE.two[2]} {generated_world.regionSE.two[3]} {generated_world.regionSE.two[4]}\n")
f.write(f"{generated_world.regionSW.three[0]} {generated_world.regionSW.three[1]} {generated_world.regionSW.three[2]} {generated_world.regionSW.three[3]} {generated_world.regionSW.three[4]} {generated_world.regionSE.three[0]} {generated_world.regionSE.three[1]} {generated_world.regionSE.three[2]} {generated_world.regionSE.three[3]} {generated_world.regionSE.three[4]}\n")
f.write(f"{generated_world.regionSW.four[0]} {generated_world.regionSW.four[1]} {generated_world.regionSW.four[2]} {generated_world.regionSW.four[3]} {generated_world.regionSW.four[4]} {generated_world.regionSE.four[0]} {generated_world.regionSE.four[1]} {generated_world.regionSE.four[2]} {generated_world.regionSE.four[3]} {generated_world.regionSE.four[4]}\n")
f.write(f"{generated_world.regionSW.five[0]} {generated_world.regionSW.five[1]} {generated_world.regionSW.five[2]} {generated_world.regionSW.five[3]} {generated_world.regionSW.five[4]} {generated_world.regionSE.five[0]} {generated_world.regionSE.five[1]} {generated_world.regionSE.five[2]} {generated_world.regionSE.five[3]} {generated_world.regionSE.five[4]}\n")
f.close()