# write a program that counts the occurence of each word into a report

user_input = input("Tell me something I don't know! ").lower().strip()

words = user_input.split()
word_count = {} 

for word in words:
    if word in word_count:
        word_count[word] =+ 1 
    else:
        word_count[word] = 1 

for word, count in word_count.items():
    print(f"{word}: {count}")