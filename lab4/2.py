a = int(input())

def even_gen(n):
    for i in range(0, n+1, 2):
        yield i

first = True
for num in even_gen(a):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False