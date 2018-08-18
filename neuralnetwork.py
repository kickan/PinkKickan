import csv
#laddae in csv fil
csv_file = open('trees.csv')
#läser fil och definierar ,
csv_reader = csv.reader(csv_file, delimiter=',')

# Skip first row if it only contains the column headers
next(csv_reader)
max_volume = 0

for row in csv_reader:
    Index, Girth, Height, Volume = row
    if float(Volume) > max_volume:
        max_volume = float(Volume)

print("The tree with the highest volume has a volume of {} meters^3.".format(max_volume))

csv_file.close()