favorite_numbers = {
    'marie': [1,3,4,7,9],
    'theingi': [2,5,6],
    'shweyi' : [1,2,3,4],
    'bob' : [5,6,7]
}
print(favorite_numbers.key())
for user in favorite_numbers.keys():
    print(f"{user}'s favorite numbers")
    for number in favorite_numbers[user]:
        print(number, end="\t")
        print()


        print(favorite_numbers['marie'])