a = int(input())

def fibonacci(n):
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x + y

first = True
for num in fibonacci(a):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False