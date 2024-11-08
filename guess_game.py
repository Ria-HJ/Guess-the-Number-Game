import random

def guess_the_number():
     print("Welcome to the 'Guess the Number' game!")
     number_to_guess = random.randint(1, 100)
     attempts = 0
 
     while True:
         try:
             guess = int(input("Guess a number between 1 and 100: "))
             attempts += 1
 
             if guess < number_to_guess:
                 print("Too low! Try again.")
             elif guess > number_to_guess:
                 print("Too high! Try again.")
             else:
                 print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                 break
         except ValueError:
             print("Please enter a valid number.")
 
 # Start the game
guess_the_number()
