# create code that prints fizz if a number is divisible by three
# buzz if it is divisible by 5 
# and fizzbuzz if it is divisible by both

for num in range(1,101):
    if num %3 == 0:
        print("fizz")
    elif num %5 == 0:
        print("buzz")
    elif num %3 == 0 and num %5 == 0:
        print("fizzbuzz")
    else:
        print(num)