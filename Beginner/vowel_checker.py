# create a function that checks a string for vowels 

to_check = input("Tell me a sentence, and I'll count the vowels! ")

def vowel_counter(string):
    vowels = set("aeiou")
    count = 0

    for character in string.lower():
        if character in vowels:
            count +=1
    
    return count

print(vowel_counter(to_check))

