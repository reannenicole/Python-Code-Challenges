# write code that is like a quiz ame, and keeps track of user score

questions = [
    ["What is the capital of the UK?\nA London\nB Sheffield\nC Birmingham? ", "london"],
    ["What is the highest grossing movie of all time?\nA Dune 2\nB Avatar\nC Avengers Engame", "avatar"],
    ["What is the planet closest to the sun?\nA Earth\nB Mercury\nC Venus", "mercury"],
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