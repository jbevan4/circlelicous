class Tire(Circle):
  """Tires are circles with a corrected perimeter"""

  def perimeter(self):
    return Circle.perimeter(self) * 1.25 
