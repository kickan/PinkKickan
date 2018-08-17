
def test_recipe(food1, food2):
    return "\'I like {} much better than {}\'".format(food1, food2)


food1 = "pasta"
food2 = "meatballs"

what_he_said = test_recipe(food1, food2)

print("This is what he said: " + what_he_said + "!")


