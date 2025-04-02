prompt = "Eneter a name of city that you have visited.: "

while True:
    city = input(prompt)
    if city == 'quit' :
        break
    else:
        print(f"I love to got to {city.title()}.")