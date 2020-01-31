import random
sides = 0
rolls = 0
roll_count = 0

print("This program is a simple dice roll program.")
input("press enter to continue...")

sides = int(input("How many sides do you want the dice to have? "))
rolls = int(input("How many dice do you want to roll? "))

while roll_count < rolls:
    print(random.randint(1, sides))
    roll_count += 1
