print("This is a guessing game")
print("Guess a name of a wild animal that is tall, you have three attempts.Good luck!")
animal_name = "girrafe"
guess =""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != animal_name and not (out_of_guesses):
    if guess_count < guess_limit:
       guess = input("Enter your guess: ")
       guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:    
    print("out of guesses,YOU LOSE!")
else:
    print("You win!")