users = [
    {'username':'aeinstein',
    'first': 'albert',
    'last': 'eistein',
    'lcation':'princeton',
    },
    {'username':'mcurie',
        'first' : 'marie',
        'last' : 'curie',
        'location':'paris',
    
    },
    {'username':'elonmusk',
        'first' : 'elon',
        'last' : 'musk',
        'location':'washintonD.C',
    
    },
    {'username':'donaldtrump',
        'first' : 'donald',
        'last' : 'trump',
        'location':'washintonD.C',
    
    },
    {'username':'joebiden',
        'first' : 'joe',
        'last' : 'biden',
        'location':'scranton',
    
    
}
]
for user in users:
    for key,value in user.items():
        print(f"{key} {value.title()}")
        print()