#Tip  Calculator

def tipPercentage(bill_amount, tip_percentage, people):
    total_bill = bill_amount + (bill_amount * tip_percentage/100)
    total_each = total_bill / people
    if people == 1:
        return f'You will have to pay: ${total_each:.2f}'
    return f'Each person will pay: ${total_each:.2f}'

print('Welcome to the Tip Calculator')
bill = float(input('What is the total bill amount? \n$: '))
tip = float(input('How much tip would you like to give? \nPercent: '))
people = float(input('How many people to split the bill? \nPeople: '))

print(tipPercentage(bill, tip, people))
