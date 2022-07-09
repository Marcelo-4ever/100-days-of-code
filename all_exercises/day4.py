#Rock Paper Scissor 
from random import randint 
from time import sleep

def validateChoice(player_choice):
    while True:
        if len(player_choice[0]) == 1:    #validade if it was written only ONE number
            if player_choice[0] in '012': #and if the number is 0, 1, 2
                return player_choice[0]
        if  player_choice[0] not in '012': #validate if is 0, 1 or 2 (but here the play still can write things like "01", "12", "012")
            print('You didn\'t type the correct number! Try again:')
            player_choice = str(input('0 / 1 / 2: ')).split()
            continue
        print('You have to type only ONE number among 0, 1 or 2.')
        player_choice = str(input('0 / 1 / 2: ')).split()
        continue

def result(player):
    try:
        if validateChoice(player) == '0':
            if computer in '0':
                return "It's a tie!"
            if computer in '1':
                return "Computer won!"
            if computer in '2':
                return "You won! Amazing!"
        elif validateChoice(player) == '1':
            if computer == '0':
                return "You won! Amazing!"
            if computer == '1':
                return "It's a tie!"
            if computer == '2':
                return "Computer won!"
        elif validateChoice(player) == '2':
            if computer == '0':
                return "Computer won!"
            if computer == '1': 
                return 'You won! Amazing!'
            if computer == '2':
                return "It's a tie!"
    except IndexError:
        return 'You have to write an option!'

print('This is the Rock Paper Scissors game!')
sleep(1)
print('Make your choice: 0 for Rock, 1 for Paper or 2 for Scissors')
sleep(1)
while True:
    computer = str(randint(0,2)) 
    player = str(input('0 / 1 / 2: ')).split()  
    print(result(player))

