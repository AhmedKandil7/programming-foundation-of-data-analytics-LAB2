for i in range (5):
    x = int(input('Enter weight:'))
    if x > 0:
        y = int(input('Enter weight unit (1 for mg, 2 for kg, 3 for ton): '))
        if y > 0:
            if y == 1:
                print(y)
            if y == 2:
                print(y * 1000)
            if y == 3:
                print(y * 1000 * 1000)
        else:
            print('invalid unit')
    else:
        print('invalid weight')
    c = input('Do you want to make another conversion? ')
    if c != 'yes':
        break