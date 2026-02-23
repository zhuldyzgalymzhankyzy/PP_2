import sys
import math

r = float(sys.stdin.readline().strip())
x1, y1 = map(float, sys.stdin.readline().split())
x2, y2 = map(float, sys.stdin.readline().split())

dx = x2 - x1
dy = y2 - y1

a = dx * dx + dy * dy
b = 2 * (x1 * dx + y1 * dy)
c = x1 * x1 + y1 * y1 - r * r

D = b * b - 4 * a * c

def point_inside(x, y):
    return x * x + y * y <= r * r

if a == 0:
    print("0.0000000000")
    sys.exit()

t0, t1 = 0.0, 1.0

if D < 0:
    if point_inside(x1, y1):
        length = math.hypot(dx, dy)
    else:
        length = 0.0
else:
    sqrtD = math.sqrt(D)
    t_enter = (-b - sqrtD) / (2 * a)
    t_exit = (-b + sqrtD) / (2 * a)
    t_low = max(t0, min(t_enter, t_exit))
    t_high = min(t1, max(t_enter, t_exit))
    if t_low > t_high:
        if point_inside(x1, y1):
            length = math.hypot(dx, dy)
        else:
            length = 0.0
    else:
        length = math.hypot(dx, dy) * max(0.0, t_high - t_low)

print(f"{length:.10f}")