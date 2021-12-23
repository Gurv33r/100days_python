# Tip calculator 
print('Welcome to the tip calculator')
total_bill = float(input("What was the total bill? $"))
tip_percentage = input("How much do you want to tip? 10%, 12%, or 15%? ")
if tip_percentage.endswith('%'):
    tip_percentage = tip_percentage[:len(tip_percentage)-1]
bill_split = int(input('How many people are splitting the bill? '))
individual_bill = round((total_bill*(1+(int(tip_percentage)/100)))/bill_split, 2)
print(f'Each person should pay: ${individual_bill}')
