users ={
    'aeinstein':{
    'first': 'albert',
    'last': 'eistein',
    'lcation':'princeton',
    },
    'mcurie': {
        'first' : 'marie',
        'last' : 'curie',
        'location':'paris',
    }
}
for username, user_info in users.item():
    print(f"Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull Name:{full_name.title()}")
    print(f"\tLocation: {location.title()}")