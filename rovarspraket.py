#Define a function called rovarsprak that takes in a string
# and for each consonant in the string adds 'o' and that consonant

#lagg till konsonanter och vokaler

vok = ["a", "e", "i", "o", "u", "y"]

kons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "W", "x", "z"]

nymening = []
def rovarsprak(mening):
    for i in kons:
        if kons[i] not in mening:
            return nymening.append(kons[i])
        elif kons[i] in mening:
            return nymening.append[kons[i]]
            return nymening.append("o")


valdmening= input("Skriv en mening: ")
calc = rovarsprak(valdmening)

print(calc)
