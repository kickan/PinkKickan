score = 0 #Set score to zero

print("''**Welcome To The Magical Game!**''")   #printing gamename

name = input("Please insert your magical name: ")

ans = int(input("What is 2*3? "))                    #question 1
if ans == 6:
    print("Good job! you got one point!")
    score = score+1                                   #add 1 point
else:
    print ("Too bad, wrong answer")

print("Your score is: {}. "
      ""
      "Here comes another question!".format(score))


ans2 = input("What is your favourite animal? ")         #question 2

if ans2 == "cat" or ans2 == "Cat":
    print("Good job! you got one point!")
    score = score + 1                                   # add 1 point
elif ans2 == "dog" or ans2 == "Dog":
    print("Cats are better than dogs, you lost one point...")
    score = score - 1                                   # remove one point
else:
    print("Too bad, wrong answer")

print("Your score is: {}. Here comes another question!".format(score))


ans3 = input("What is the meaning with life? ")         #question 3

if ans3 == "Love" or ans3 == "love":
    print("Loooove is all you neeeed <3. Congratulations, you got 32 points")
    score = score + 32
elif ans3 == "There is no meaning" or ans3 == "there is no meaning":
    print("That's depressing, you lost 42 points")
    score = score - 42
else:
    print("That's an interesting answer, you are probably right! You got one point!")
    score = score + 1

print("That was all the questions, good job on finishing the game. Lets see what score {} got:".format(name))

if score <=2 and score >=0:
    print("Your score is: {}. That was a mediocre score, better luck next time, {}!".format(score, name))
elif score >2:
    print("Your score is {}. Good job! You are very talented, {}!".format(score, name))
elif score <0:
    print("Your score is {}. That was really bad, hopefully you got other talents... {}".format(score, name))

