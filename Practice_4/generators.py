# generators.py

# 1. Squares generator
def squares(n):
    for i in range(n + 1):
        yield i * i


# 2. Even numbers generator
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


# 3. Divisible by 3 and 4
def divisible_by_3_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


# 4. Custom iterator class
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value