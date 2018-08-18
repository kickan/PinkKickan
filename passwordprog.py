import random

# Skapar listor

adj = ["stor", "vacker", "snäll", "underbar", "rund", "cool"]

sub = ["glass", "boll", "groda", "troll", "tröja", "piska"]

sign = ["=", "/", "!", ":", "?", "#"]

num = []

for i in range(1, 101, 1):
    num.append(i)

listan = [adj, sub, sign, num]

#***************************************'
rand = 1

def randfunc(rand):
    return rand[random.randrange(len(rand))]



#*****************************************



svar = input("vill du ha ett magiskt lösenord? (ja eller nej) ")

while svar != "nej":
    losen = []
    for word in listan:
        hej = randfunc(word)
        losen.append(hej)
    random.shuffle(losen)
    losenstr = "".join(str(e) for e in losen)
    print("".join(losenstr))
    svar = input("Vill du ha ett till magiskt lösenord? (ja eller nej) ")

#Fixa så den kan skriva ut i ett ord
print(num)