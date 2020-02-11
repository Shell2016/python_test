import random

streak_number = int(input('Enter streak number: '))
toss_number = int(input('Enter number of tosses: '))
numberOfStreaks = 0
for x in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flip_list = []
    for i in range(toss_number):
        if random.randint(0, 1) == 0:
            flip_list.append('H')
        else:
            flip_list.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 0
    streak_bool = False
    for i in range(len(flip_list) - 1):
        if streak == streak_number:
            streak_bool = True
            break
        if flip_list[i + 1] == flip_list[i]:
            streak += 1
        else:
            streak = 0

    if streak_bool == True:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))


