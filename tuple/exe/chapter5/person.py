person = {'first_name': 'Brian', 'last_name': 'Davidson', 'age':23, 'city':'Mandalay'}
# printing raw form
print(person)
print(person.get('first_name')) # when using [], it raise an expection when key does not exist.
print(person.get('last_name'))
print(person.get('age'))
print(person.get('city'))