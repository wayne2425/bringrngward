favorite_numbers = {'TLM' :9, 'KKP':7, 'CMZ' :2, 'HEDO':12, 'KZYM':99}
for name, number in favorite_numbers.items():
    print(f"name{name}'s favorite number is {number}")

    print("item view")
    print(favorite_numbers.items())

    print("key view ")
    print(favorite_numbers.key())

print("values view")
print(favorite_numbers.values())