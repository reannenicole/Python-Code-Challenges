# create a function that checks if a string is a palindrome

def is_palindrome(string):
    string_to_check = string.lower().strip()
    return string_to_check == string_to_check[::-1]

print(is_palindrome("racecar"))
print(is_palindrome(" racecar"))
print(is_palindrome("hathesage"))
print(is_palindrome("2112"))