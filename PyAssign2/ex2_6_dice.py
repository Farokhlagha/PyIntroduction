# Simulate throwing the dice. Until the number 6 comes.
# As a bonus, the dice are rolled again

import random

while True:
    input("throw the dice (press enter)")
    dice = random.randint(1, 6)
    print("your dice is: ", dice)

    if dice != 6:
        break