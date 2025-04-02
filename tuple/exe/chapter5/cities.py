cities = {'Yangon': {
    'country':'myanmar',
    'population': 5.1,
    'fact': "Where ShweDagon Locate"
},
          'Bangkok': {
    'country':'thailand',
    'population': 11.23,
    'fact' : "Capital of Thai"
    },
          'Tokyo': {
    'country':'japan',
    'population': 37.1,
    'fact' : "Capital of JP"
          },
          'Aukland': {
    'country':'new zealand',
    'population': 1.7,
    'fact' : "Capital of NZ"
          },
          'toranto': {
    'country':'canada',
    'population': 2.8,
    'fact' : "Capital of Canada"
          }
}

for city, info in cities.items():
    print(f"{city}'s Information")
    for k, v in info.items():
        print(f"\t{k} : {v}")
    print()