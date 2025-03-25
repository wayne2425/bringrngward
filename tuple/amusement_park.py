age = 65
if age < 4: #3
    price = 0
    #print("admission cost is $0.")
elif age < 18: #17
    price =25
elif age < 65:
    price = 40
    #print("admission cost is $25.")
else: #18 or higher
    price = 20
    #print("admission cost is $40.")
print(f"your admission cost is ${price}")
