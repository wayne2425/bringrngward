number = input("enter a number that I can tell you even or odd. :")
number =int(number)

if number % 2 == 0:
    print(f"\n {number} is even.")
else:
    print(f"\n {number} is odd.")