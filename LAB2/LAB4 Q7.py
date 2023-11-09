friends = input('friends:')
friends = friends.split(' ')
presents = input('presents:')
presents = presents.split(' ')
wish = input('what is in his mind:')
if wish in presents:
    index=presents.index(wish)
    print('oh',friends[index],', Thank you friend')
else:
    print('Opps, Sorry none. ')