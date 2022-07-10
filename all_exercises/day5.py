"""
Password Generator
Using for loop, list, and range()
"""
from random import randint
my_list = [] # a list with all list of each function 

def get_letters(x):
    my_letter_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(x):
        choose_index = randint(0, 25) #one index every loop for the string above ^
        upper_lower_case = randint(0,1) # 0 is lowercase, 1 is uppercase
        if upper_lower_case == 0:
            my_letter_list.append(alphabet[choose_index])
        else:
            my_letter_list.append(alphabet[choose_index].upper())
    global my_list
    my_list = my_letter_list[:] #copying the chosen letters 
    return my_letter_list


def get_numbers(x):
    my_number_list = []
    numbers_09 = '0123456789' 
    for i in range(x):
        choose_index = randint(0, 9) #choose one index
        my_number_list.append(numbers_09[choose_index])
    global my_list #indicating is the global variable
    my_list.append(my_number_list[:]) # here we have to append, otherwise the whole list would change
    return my_number_list


def get_symbols(x):
    my_symbol_list = []
    all_symbols = r'!@#$%¨&*()_+-=¬¢£\'":><;^`[]}{,'
    for i in range(x):
        choose_index = randint(0, 30)
        my_symbol_list.append(all_symbols[choose_index])
    global my_list #indicating is the global variable
    my_list.append(my_symbol_list[:]) #have to append like the function before this one
    return my_symbol_list
    
        
#!Principal Program
while True:
    letters = str(input('How many letters would like in your password? '))
    numbers = str(input('How many numbers? '))
    symbols = str(input('How many symbols? '))
    if not letters.isdigit() or not numbers.isdigit() or not symbols.isdigit():
        print('You have to write a number! Try again!')    
        continue
    break
letters, numbers, symbols = int(letters), int(numbers), int(symbols)
get_letters(letters)
get_numbers(numbers)
get_symbols(symbols)

copy_list = my_list[:] # a copy of all lists inside a list
my_list.clear() #clear the original so I can append() each value without the '[]' of the lists 
for each_list in copy_list:
    for character in each_list: 
        my_list.append(character) #adding one by one 


print('Here is your password: ',end='')

size = len(my_list) # here I have the length to make a loop that goes through ALL the values 
counter = 0
for character in range(size): 
    list_size = len(my_list) - 1 #len start in 1, so there is the chance of having an index out of range 
    choose_password_index = randint(0, list_size) #here we use the randint to choose one index so the password gets more random
    print(my_list[choose_password_index],end= '') #we get the value from the list
    del my_list[choose_password_index] #we delete the value so we can't repeat it again
    
    
    #print(my_list[randint(0, list_size)])

#this code may have more lists that it needed, but I changed the whole code a few times, so I will see it another day :)

