import random
import time

first: int = 7
second: float = 44.3
print("first + second =", first + second)

print("first * second =", first * second)

print("second / first =", second / first)

a: int = 9
b: int = 6
c: int = a + b
# b = c + a
b = 8
print(f"a={a} b={b} c={c} ->", end='')
print(' ***')

print("\tgeorge", end='')
time.sleep(.7)
print("\r\tzengin")

print(random.randint(0, 100), end='')
time.sleep(0.3)
print("\r             ")
d: str = "abcdef"
print(len(d))

