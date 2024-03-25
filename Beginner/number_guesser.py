import random 

last_number = input("Tell me a number: ")
if last_number.isdigit():
    last_number = int(last_number)

    if last_number == 0:
        print("Type a number larger than 0")
        quit()
else:
    ("please type a number!")
    quit()
     
 
random_number = random.randrange(1, last_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Now guess a number! ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please guess a number!")
        continue
    
    if user_guess == random_number:
        print("That is correct!")
        break
    elif user_guess > random_number:
        print("Go lower!")
    else:
        print("Try higher!")


print("You got it in", guesses, "guesses!" )




