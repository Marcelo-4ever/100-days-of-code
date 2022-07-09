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
    
        
        
letters = int(input('How many letters would like in your password? '))
numbers = int(input('How many numbers? '))
symbols = int(input('How many symbols? '))
get_letters(letters)
get_numbers(numbers)
get_symbols(symbols)

copy_list = my_list[:]
my_list.clear()
for each_list in copy_list:
    for character in each_list: 
        my_list.append(character)


print('Here is your password: ',end='')

my_list_copy = my_list[:]
counter = 0
for character in my_list_copy:
    list_size = len(my_list) - 1
    choose_index = randint(0, list_size)
    print(my_list[choose_index],end= '')
    del my_list[choose_index]
    
    
    #print(my_list[randint(0, list_size)])
    