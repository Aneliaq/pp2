# 1. Generator that generates squares up to N
def square_generator(n):
    for i in range(n + 1):
        yield i * i


for number in square_generator(5):
    print(number)


# 2. Even numbers from 0 to n (input from console)
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


n = int(input())
print(",".join(str(num) for num in even_numbers(n)))


# 3. Numbers divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


for number in divisible_by_3_and_4(100):
    print(number)


# 4. Generator squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


for value in squares(3, 7):
    print(value)


# 5. Generator that returns numbers from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


for number in countdown(5):
    print(number)

