alien_color = ['red', 'green','yellow']

alien_color = input("enter alien color.")
for color in alien_color:
    if color=='green':
        print("you earned 5 points.")
    else:
        print("you fail shooting.")


        for color in alien_color:
            if color=='green':
                print("you earned 5 points.")
            elif color == 'yellow':
                print("you earned 10 points.")
            else:
                print("you earned 15 points.")