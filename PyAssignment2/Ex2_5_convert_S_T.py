#Convert seconds to time

sec=int(input("please enter seconds: "))


hr=sec//3600
m=(sec%3600)//60
s=(sec%60)

print(sec, "seconds = ", hr, ":" ,m , ":", s)