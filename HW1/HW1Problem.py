# Name: Becky Tseng
# StudentID Number: 2038591

currentMonth = input('Please type in the current month ')
currentDay = input('Please type in the current day ')
currentYear = input('Please type in the current year ')

print('Current date')
print('Month:' + currentMonth)
print('Day:' + currentDay)
print('Year:' + currentYear)

birthMonth = input('Please type in your birth month ')
birthDay = input('Please type in your birth day ')
birthYear = input('Please type in your birth year ')
print('Birthday')
print('Month:' + birthMonth)
print('Day:' + birthDay)
print('Year:' + birthYear)

age = int(currentYear) - int(birthYear)

if (currentMonth == birthMonth) and (currentDay == birthDay):
    print('Happy birthday!')
else:
    print('You are ' + str(age) + ' years old.')
