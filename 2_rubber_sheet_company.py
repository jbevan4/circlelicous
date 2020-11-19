from circles.circle import Circle

cuts = [1, 1.5, 0.8, 0.7]
circles = (Circle(cut) for cut in cuts)

for circle in circles:
    print(f"A circle with radius {circle.radius:.2f}\n"
          f"has a perimeter of {circle.perimeter():.2f}\n"
          f"and a cold area of {circle.area():.2f}")
    circle.radius *= 1.1
    print(f"and a warm area of {circle.area():.2f}")
