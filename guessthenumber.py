import random
import math

# Ask for Inputs
lower = int(input("Enter Lowest number: "))
upper = int(input("Enter Highest number: "))

n = int(random.randint(lower, upper))
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

def odd_even():
    if (n % 2) == 0:
        print('"It is Even number"')
    else:
        print('"It is Odd number"')

multiple = n / 2
print("Hint: The number is a multiple of: ", + multiple)

count = 0
while count < math.log(upper - lower + 1, 2):
    count += 1
    if count > math.log(upper - lower + 1):
        odd_even()

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
