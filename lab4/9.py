n = int(input())

def power_of_two(limit):
    for i in range(limit + 1):
        yield 2 ** i

for num in power_of_two(n):
    print(num, end=" ")