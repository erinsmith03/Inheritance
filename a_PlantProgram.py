import a_PlantClass as pc

primrose = pc.Plant("Green") #superclass

sunflower = pc.Flower("Yellow",20) #

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


print(primrose.get_petals())
