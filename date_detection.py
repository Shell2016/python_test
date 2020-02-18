import re

dateRegex = re.compile(r'''
    # DD/MM/YYYY
([0][1-9]|[1-2][0-9]|[3][0-1])/    # DD 01-31
([0][1-9]|[1][0-2])/                # MM 01-12
([1-2][0-9]{3})                    #YYYY 1000-2999
''', re.VERBOSE)

while True:
    dateInput = input('Enter date for validation DD/MM/YYYY: ')
    date = dateRegex.search(dateInput)
    if date is None:
        print('Not valid date format!')
    else:
        break

def dateValidation(dd, mm, yyyy):
    leapYear = False
    if yyyy%4==0 or (yyyy%100 == 0 and yyyy%400 ==0):
        leapYear = True
    if 1 <= dd <= 30 and (mm == 4 or mm == 6 or mm == 9 or mm == 11):
        return True
    elif 1 <= dd <= 31 and (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
        return True
    elif 1 <= dd <= 28 and (mm == 2 and leapYear == False):
        return True
    elif 1 <= dd <= 29 and (mm == 2 and leapYear == True):
        return True
    else:
        return False

day = int(date.group(1))
month = int(date.group(2))
year = int(date.group(3))
if dateValidation(day, month, year):
    print("It's a valid date.")
else:
    print("It's not a valid date.")

