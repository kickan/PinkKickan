
#Ask for hobbies and list them

#Skapar hobbylista
hobbylista = []
i = input("What do you like to do? ")

while i != "stop":
    hobbylista.append(i)
    i = input("what do you like to do? ")

hobbies = ""

for hobby in hobbylista:
    hobbies = hobbies + " " + hobby

print("Your hobbies are: {}".format(hobbies))


