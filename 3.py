a=4
while True:
    try:
        b = int(input('number: '))
        res = a + b
        if res == 14:
            print('good')
        else:
            print('bad')
    except Exception as e:
        print(e)
        b = 'x'
    finally:
        if b=='x':
            print('finito')
            break

# aviel33@gmail.com