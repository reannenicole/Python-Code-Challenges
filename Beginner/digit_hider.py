def validate_and_hide(card_number):

    if len(card_number) < 16 or len(card_number) > 16:
        print("Please make sure your card number is 16 digits in length")
    elif len(card_number) == 16:
         last_4 = card_number[12:]
         print(f"To confirm, the last four digits of our card number are {last_4}")

card_input = input("Please enter your 16 digit card number: ")

validate_and_hide(card_input)
