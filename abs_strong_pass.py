import re

upperRegex = re.compile(r'[A-Z]')
lowerRegex = re.compile(r'[a-z]')
isDigitRegex = re.compile(r'\d+')
lengthRegex = re.compile(r'\w{8,}')

def isStrong(passw):
    if upperRegex.search(passw) is None:
        return False
    if lowerRegex.search(passw) is None:
        return False
    if isDigitRegex.search(passw) is None:
        return False
    if lengthRegex.search(passw) is None:
        return False
    else:
        return True

while True:
    password = input('Enter password: ')
    if password == 'exit':
        break
    if isStrong(password):
        print('Strong')
    else:
        print('Not strong')

    
            
