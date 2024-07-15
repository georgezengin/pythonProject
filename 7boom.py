import random
def is_boom(number):
    return not (number % 7) or '7' in str(number)


def play_7_boom(n):
    x = 0
    while (x < 100):
        i = random.randint(1,  n) #range(1, n + 1, 1))
        x += 1
        if is_boom(x):
            print("\U0001F4A5", end=' ')
        else:
            print(x, end=' ')


# Play the game from 1 to 50
play_7_boom(100)
