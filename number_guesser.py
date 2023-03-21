import random

print("guess a number from 1 to 10. you have 5 guess's")

value = random.randint(1, 10)

guess = int(input("what is your guess: "))

if guess > value:
    print("too high")
elif guess < value:
    print("too low")
else:
    print("you won!")
    quit()

guess = int(input("what is your guess: "))

if guess > value:
    print("too high")
elif guess < value:
    print("too low")
else:
    print("you won!")
    quit()

guess = int(input("what is your guess: "))

if guess > value:
    print("too high")
elif guess < value:
    print("too low")
else:
    print("you won!")
    quit()
    
guess = int(input("what is your guess: "))

if guess > value:
    print("too high")
elif guess < value:
    print("too low")
else:
    print("you won!")
    quit()

guess = int(input("what is your guess: "))

if guess > value:
    print("too high")
elif guess < value:
    print("too low")
else:
    print("you won!")
    quit()

print("you lost")
quit()
