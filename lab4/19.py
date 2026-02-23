import sys
import math

r = float(sys.stdin.readline())
x1, y1 = map(float, sys.stdin.readline().split())
x2, y2 = map(float, sys.stdin.readline().split())

def dist(xa, ya, xb, yb):
    return math.hypot(xa - xb, ya - yb)

d = dist(x1, y1, x2, y2)

# line-circle intersection check
dx = x2 - x1
dy = y2 - y1
a = dx*dx + dy*dy
b = 2*(x1*dx + y1*dy)
c = x1*x1 + y1*y1 - r*r
D = b*b - 4*a*c

intersects = False
if D > 0:
    sqrtD = math.sqrt(D)
    t1 = (-b - sqrtD) / (2*a)
    t2 = (-b + sqrtD) / (2*a)
    if (0 < t1 < 1) or (0 < t2 < 1):
        intersects = True

if not intersects:
    print(f"{d:.10f}")
else:
    d1 = math.hypot(x1, y1)
    d2 = math.hypot(x2, y2)
    
    theta = math.acos((x1*x2 + y1*y2) / (d1*d2))
    alpha = math.acos(r / d1)
    beta = math.acos(r / d2)
    
    arc = r * (theta - alpha - beta)
    tangent1 = math.sqrt(d1*d1 - r*r)
    tangent2 = math.sqrt(d2*d2 - r*r)
    
    result = tangent1 + tangent2 + arc
    print(f"{result:.10f}")