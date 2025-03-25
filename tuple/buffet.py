buffet_foods = ('hamburger','pizza','fried chicken','ice cream','biryani')
print('favorite foods')
for food in buffet_foods:
    print(food)

#buffet_foods[0] = 'pasta'
buffet_foods = ('hamburger','pizza','fried chicken','ice cream','biryani','noodle','hotpot')
print("revised menu")
for ind, food in enumerate(buffet_foods): # index and value
    print(ind, food)