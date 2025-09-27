import random
print("welcome to the number guessing game ")

secret_num  =random.randint(1,100)
attempts = 0
while True:
        guess =int(input("Enter your guess number (1-100)"))
        attempts += 1
        if guess < 50:
            print("To low ....please try again")
        elif guess > 75:
            print("To high .... Try agin")
        else:
            print("congratulation You guessed it right number {attempts}")
            break