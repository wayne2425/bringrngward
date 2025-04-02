favorite_language = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil':
                     'python'}
language = favorite_language['sarah'].title()
print(f" Sarah's favorite language is {language}")

# accessing value with [] and get()
language2 =favorite_language.get('je', 'person does not exist.')
print(language2.title())