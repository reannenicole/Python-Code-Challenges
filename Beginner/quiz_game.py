# write code that is like a quiz ame, and keeps track of user score
print("\t\t~~~~~~~~~~~~~~~~~~~")
print("\t\tWELCOME TO THE QUIZ")
print("\t\t~~~~~~~~~~~~~~~~~~~\n")

playing = input("Want to play? ")
if playing != "yes":
    quit()

print("\nLet's play!")

questions = [
    ["\nWhat is the capital of the UK?\nA London\nB Sheffield\nC Birmingham? ", "london"],
    ["\nWhat is the highest grossing movie of all time?\nA Dune 2\nB Avatar\nC Avengers Engame", "avatar"],
    ["\nWhat is the planet closest to the sun?\nA Earth\nB Mercury\nC Venus", "mercury"],
]

score = 0 

for question, answer in questions:
    print(question)

    user_answer = input("Your answer: ").lower().strip()

    if user_answer == answer:
        print("Correct")
        score += 1

    else:
        print(f"That's wrong! The answer is {answer}.")

print(f"Your final score is: {score}/{len(questions)}")