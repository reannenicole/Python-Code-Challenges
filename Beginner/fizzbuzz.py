for num in range(1,101):
    if num %3 == 0:
        print("fizz")
    elif num %5 == 0:
        print("buzz")
    elif num %3 == 0 and num %5 == 0:
        print("fizzbuzz")
    else:
        print(num)