# take a word and print it backwards
wordin = input("Type your word that you want typed backwards: ")


def swapper(word):
    j = word.upper()
    h = j[::-1]
    print(h)

swapper(wordin)


