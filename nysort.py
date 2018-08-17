list = [2, 6, 3, 0, 4, 13]

nylista = []

lenghtlist = len(list)

for i in range(len(list)):
    minsta = min(list)
    list.remove(minsta)
    nylista.append(minsta)

print(nylista)