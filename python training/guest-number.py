import random

name = input("please input your name: ")

print (f"Welcome {name} to guess number! ")

guess_number = 0

com_guess = random.randint(1,50)
count = 0
while guess_number != com_guess:
    guess_number = int(input("please input your number 1- 50: "))
    count +=1
    if count >5:
        print ("time up")
        print(f"computer guess is: {com_guess}")    
        exit()
    if guess_number < com_guess:
        print("You guess to low!")
    if guess_number > com_guess:
        print("You guess too high!")

print("you win")
print(f"computer guess is: {com_guess}")    