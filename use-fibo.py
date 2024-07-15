import fibo
fibo.fib(10)
print(fibo.fib2(10))
print('rfibo ',fibo.rfibo(10))

# Example usage:
n = 10
result = fibo.rfibo(n)
print(f"Fibonacci series up to {n} terms: {result['series']}")
print(f"Total of the series: {result['total']}")
#print(f"Fibonacci series up to {n} terms: {fib_series}")