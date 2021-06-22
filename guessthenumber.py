import random
import math

# Ask for Inputs
lower = int(input("Enter Lowest number: "))
upper = int(input("Enter Highest numbe: "))

n = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

count = 0
while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number:- "))
    # Condition testing
    if n == guess:
        print("Congratulations you did it in ",
              count, " try")
        break
    elif n > guess:
        print("You guessed too small!")
    elif n < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % n)
    print("\tBetter Luck Next time!")
