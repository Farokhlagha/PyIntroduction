# A program that receives the student's score
# until the user enters the exit command 
# and finally prints the student's score point average.

print("Welcome User")

name = input("Please enter your name:")
family = input("Please enter your family:")

i = 0
sum = 0

while True:
    score = input("Please enter your scores(0-20) or type 'exit' to finish: ")

    if score == "exit":
        break

    else:
        i += 1
        sum += float(score)

average = sum/i

if average >=17:
    print("Great 😀")
elif average <17 and average >=12:
    print("Normal 😉")
elif average <12:
    print("Fail 🙁")

print(name, family,", your average is:",average)