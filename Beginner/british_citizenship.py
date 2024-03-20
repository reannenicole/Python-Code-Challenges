print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~A CITIZENSHIP TEST~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

british_output = ("\nCongratulations, you are officially a brit! OORAH")
not_british_output = ("\nYou must be one of those damn frenchies!")

british = 0 
not_british = 0 

questions = [
    ("\nWho is England's best Barry?\n\tA Lyndon\n\tB From Eastenders\n\tC 63", "from eastenders"),
    ("\nWhich country is the worst?\n\tA England\n\tB France\n\tC Australia", "france"),
    ("\nWhat is the best sport?\n\tA Football\n\tB Basketball\n\tC Tennis", "football"),
]

for question, answer in questions:
    print(question)

    user_input = input("Your answer: ").lower().strip()

    if user_input == answer:
        british += 1
        print("Gu on geezer!")
    else:
        not_british +=1 
        print("You're on thin ice")

if british > not_british:
    print(british_output)
else:
    print(not_british_output)