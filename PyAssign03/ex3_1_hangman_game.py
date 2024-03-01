# Hanging Man Game

import random

good_chars = []
bad_chars = []
mistake = 0

words_bank = ["hello","fish","clear","laptop","open","bike","flower","red","green"]

#x=random.randint(0,len(words_bank)-1)
#word=words_bank[x]
word = random.choice(words_bank)

while mistake < 6:
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end=" ")
        else:
            print("-", end=" ")
    if len(word) == len(good_chars):
        print("you win")
        print("👏")
        break

    user_char = input("please write your guess: ").lower()
    if len(user_char) == 1:
        if user_char in word:
            good_chars.append(user_char)
            print("✔")
        else:
            bad_chars.append(user_char)
            mistake += 1
            print("❌")
    else:
        print("enter one char correctly")      
if mistake == 6:
    print("game over 💀 ")  