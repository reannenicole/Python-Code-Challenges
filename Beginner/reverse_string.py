# define a function that reverses a string



def string_reverser():
    your_string = input("tell me something cool and I'll flip it around! ")
    string_reverser = " "
    for char in your_string[::-1]:
       string_reverser += char
    
    return string_reverser

string_reverser = string_reverser()
print(string_reverser)
