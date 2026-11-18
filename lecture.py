import random

def game():
    enter_low = int(input("Enter low: "))
    enter_high = int(input("Enter high: "))

    secret = random.randint(enter_low, enter_high)  
    attempts = 0
    guess = 0

    while guess != secret:

        guess = int(input("Enter one more guess: "))
        attempts += 1

        if guess > secret:
            print("Enter lower: ") 

        if guess < secret:
            print("Enter higher: ")  

    print(f"Correct. Number of attempts are {attempts}")        

game()