usernames = ['admin', 'robert', 'kevin', 'sofia', 'marie']
print(len(usernames))
if len(usernames)==0:
    print("we need to find some users.")
else:
    for user in range(0,len(usernames)):
        print(usernames.pop())

print("after popping out users!!")
print(usernames)