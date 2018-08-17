
#ask for a price return a tip suggestion


def tip_suggest(cheap, expensive):
    return 1.05*cheap + 1.1*expensive

def print_tip(tipping):
    print("You should pay: {} money".format(tipping))

amount = int(input("What is your amount? "))

while amount!="stop":
    if amount <=100:
        tipping = tip_suggest(amount,0)
        print_tip(tipping)
    elif amount > 100:
        tipping = tip_suggest(0, amount)
        print_tip(tipping)
    amount = int(input("What is your amount? "))

def tip_fun2(meal):
    if meal <= 100:
        return 1.05 * meal
    elif meal > 100:
        return 1.1 * meal

