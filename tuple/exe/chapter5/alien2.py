alien_0 = {'x_position' :0, 'y_position':25, 'speed': 'medium'}
# move the alien to the right based on speed
if alien_0['speed'] == 'slow':
        x_increment = 1
elif alien_0 == 'medium':
        x_increment = 2
else:
        x_increment = 3
alien_0['x_position'] = alien_0['x_position']+ x_increment
print(f"moving after alien_0 {alien_0['x_position']}")
print(alien_0)

print("before deleting")
print(alien_0)

del alien_0['speed']
print("after deleting")
print(alien_0)