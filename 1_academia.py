from random import random, seed
from circles.circle import Circle

seed(4513410)

n = 10

print(f"using circlelicous version {Circle.version}")
circles = (Circle(random()) for _ in range(10))
print(
    f"the average area of {n} circles is {sum(circle.area() for circle in circles) / n}")
