# Name: Becky Tseng
# StudentID Number: 2038591

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agaveNectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
serving = float(input('How many servings does this make?\n'))
print('')
# FIXME (1): Finish reading other items into variables, then output the three ingredients
print('Lemonade ingredients - yields', f'{serving:.2f}', 'servings')
print(f'{lemon_juice_cups:.2f}', 'cup(s) lemon juice')
print(f'{water_cups:.2f}', 'cup(s) water')
print(f'{agaveNectar_cups:.2f}', 'cup(s) agave nectar')
print('')

# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
ServingsToMake = float(input('How many servings would you like to make?'))
print('')
print('')
print('Lemonade ingredients - yields', f'{ServingsToMake:.2f}', 'servings')
lemon_juice_cups2 = (lemon_juice_cups / serving) * ServingsToMake
print(f'{lemon_juice_cups2:.2f}', 'cup(s) lemon juice')
water_cups2 = (water_cups / serving) * ServingsToMake
print(f'{water_cups2:.2f}', 'cup(s) water')
AgaveNectar_cups2 = (agaveNectar_cups / serving) * ServingsToMake
print(f'{AgaveNectar_cups2:.2f}', 'cup(s) agave nectar')
print('')

# FIXME (3): Convert and output the ingredients from (2) to gallons
print('Lemonade ingredients - yields', f'{ServingsToMake:.2f}', 'servings')
gallonLemonJuice = lemon_juice_cups2 / 16
print(f'{gallonLemonJuice:.2f}', 'gallon(s) lemon juice')
gallonWater = water_cups2 / 16
print(f'{gallonWater:.2f}', 'gallon(s) water')
gallonAgaveNectar = AgaveNectar_cups2 / 16
print(f'{gallonAgaveNectar:.2f}', 'gallon(s) agave nectar')
