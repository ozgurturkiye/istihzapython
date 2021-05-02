# Circle area module
from math import pi

def circle_area(r):
  """Return area of circle with given {r} radius."""
  if type(r) not in [int, float]:
      raise TypeError("radius can not be complex number, string or bool")

  if r < 0:
    raise ValueError("radius can not be negative ")

  return pi*(r**2)
