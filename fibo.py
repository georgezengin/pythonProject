def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def rfibo(n):
    def fibonacci(n):
        match n:
            case _ if n <= 0:
                return 0
            case 1:
                return 1
            case _:
                return fibonacci(n - 1) + fibonacci(n - 2)

    fib_series = [fibonacci(i) for i in range(n)]
    total = sum(fib_series) # (n - 1) if n > 0 else 0
    return {"series": fib_series, "total": total}


# Write a function that takes in a numerical value, and returns
#  the word corresponding to that number.
# The program will handle numbers: 0 - 4, for other numbers it will
# return that the input is incorrect.

def get_numeric(number):
    numbers = ["zero", "one", "two", "three", "four"]
    if number < len(numbers):
        return numbers[number]
    else:
        return "not supported"


a = 6


def my_function(x):
    print(x * a)


def my_function1(x, a):
    print(x * a)


def my_function2(x):
    a = 6
    print(x * a)

