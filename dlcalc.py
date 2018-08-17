
print("*********BAKING MACHINE*************")

task = input("Do you want to transform cups or dl or neither? ")

#def cups_to_dl(cup, dl_cup):
   # dl_cup=2.37*cup

while task!="stop":
    if task == "cups":
        cup = float(input("Please enter amount in cups: "))
        #calc_cup = cups_to_dl(cup, dl_cup)
        calc = cup*2.37
        print("{} cups is {} dl".format(cup, calc_cup))
        print("*********BAKING MACHINE*************")
        task = input("Do you want to transform cups or dl? ")
    elif task == "dl":
        dl = float(input("Please enter amount in dl: "))
        calc = dl*0.422
        print("{} dl is {} cups".format(dl, calc))
        print("*********BAKING MACHINE*************")
        task = input("Do you want to transform cups or dl? ")
    elif task == "neither":
        tasktwo = input("Do you want a recepie for a chocolate cake? (yes or no) ")

        if tasktwo == "yes":
            print("Mix butter, eggs, cocoa, sugar and vanilla extract in a big pot. \n"
                    "put in a form and stick in in the oven for 20 min \n"
                    "take out and enjoy")
            break
        elif tasktwo == "no":
            print("There is nothing else I can do for you today, good bye")
            task = "stop"

if task == "stop":
    print("The baking machine has stopped")