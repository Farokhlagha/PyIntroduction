# reverse of list

my_list = []

while True:
    user_input= input("please enter a number/word or 'f' to finish: ")
    if user_input=="f":
        break
    else:
        my_list.append(user_input)

print(my_list[::-1])