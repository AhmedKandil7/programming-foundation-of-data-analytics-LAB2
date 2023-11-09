n = int(input('enter the number of multiplication tables : '))
for i in range(n+1):
    for j in range(1,i+1):
      print('%-8d'%(i * j), end='')
    print('')