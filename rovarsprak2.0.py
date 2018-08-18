#be om en mening och gör om till lista
valdmening = (input("Skriv din mening: "))

#kons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "W", "x", "z"]
konssmall="bcdfghjklmnpqrstywxz"
konsbig = konssmall.capitalize()

kons = konssmall + konsbig

nymening = ""

for i in range(len(valdmening)):
    if valdmening[i] in kons:
        nymening += (valdmening[i] + "o" + valdmening[i])
    if valdmening[i] not in kons:
        nymening += (valdmening[i])

print("Rövarspråk: " + nymening)
