import random
playing=True
number =str(random.randint(0,9))
print("I will generate a numberfrom 0 to 9,and you have to guess the number one digitat the time.")
print("The game ends when you get one hero!")
while playing:
    guess=input("Give me your best!\n")
    if number==guess:
        print("You win the game")
        print("The number was",number)
        break
    else:
        print("Your guess isn't correct,try again.\n")