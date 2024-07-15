a = ['netanel', 'neta','daniel','tomer']
names = a

if 'reut' in a:
    print('match')
else:
    print('not match')

#print(*range(1,20,3))

#print(*(f'Hi {num:02}\n' for num in range(1, 51, 3)))#, sep='\n')

for i in range(len(a)):
    print(a[i])

#for name in names:

print(*(name for name in names), sep='-\/-', end='')

match s:
    case s if s == 'a':
        print(a)
        