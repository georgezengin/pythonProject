while True:
    try:
        n1 = int(input("Enter n1: "))
        n2 = int(input("Enter n2: "))
        res = n1 / n2
        print("res = ", res)
    except TypeError as e:
        print('not number', e.args)
    except ValueError as e:
        print('value error: ', e)
    except ZeroDivisionError as e:
        print('division by zero: ', e)
        n2 = 999
        continue
    except BaseException as e:
        print(f"Error: ", e)
        break
