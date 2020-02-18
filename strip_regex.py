import re

def stripR(txt, arg=''):
    if arg == '':
        leftSpaceRegex = re.compile(r'^\s*')
        rightSpaceRegex = re.compile(r'\s*$')
        mo = leftSpaceRegex.sub('', txt)
        mo = rightSpaceRegex.sub('', mo)
        print(mo)
    else:
        chrRegex = re.compile(arg)
        mo = chrRegex.sub('', txt)
        print(mo)

text = '  blablabla lkjff jfdlf     '
stripR(text)