from math import ceil

wallHeight = input('Enter wall height (feet):\n')
wallWidth = input('Enter wall width (feet):\n')
wallArea = int(wallHeight) * int(wallWidth)
print('Wall area:', wallArea, 'square feet')
gallonPaint = 350
paintNeeded = wallArea / gallonPaint
print(f"Paint needed: {paintNeeded:.2f} gallons")
cansNeeded = ceil(paintNeeded)
if cansNeeded == 0:
    cansNeeded = 1
else:
    cansNeeded = ceil(paintNeeded)
print("Cans needed:", cansNeeded,"can(s)\n")
#dictionary for different color paints and price.
paint = { 'red':35,'blue':25, 'green':23}
paintColor = input('Choose a color to paint the wall:\n')
paintCost = paint.get(paintColor) * cansNeeded
print(f'Cost of purchasing {paintColor} paint: ${paintCost}')

