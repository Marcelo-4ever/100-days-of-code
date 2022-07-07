# Band Name Generator

print('Welcome to the Band Name Generator!')
city = str(input('What city did you grow up in? \n')).title().split()
pet = str(input('What is the name of your first pet? \n')).title()
print(f'Your Band name is {city[0]} {pet}')