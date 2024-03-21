# create a function that checks a string for vowels 

def vowel_counter(string):
    vowels = set("aeiou")
    count = 0

    for character in string.lower():
        if character in vowels:
            count +=1
    
    return count

print(vowel_counter("there are four e's"))
print(vowel_counter("rythm)"))

