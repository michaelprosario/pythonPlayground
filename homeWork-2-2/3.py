import math

def distance(p1, p2):
 """
 This function computes the distance between two 2D tuples.

 Args:
     p1: A 2D tuple representing the first point.
     p2: A 2D tuple representing the second point.

 Returns:
     The distance between the two points.
 """

 x1, y1 = p1
 x2, y2 = p2
 return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Example usage
p1 = (1, 2)
p2 = (3, 4)
dist = distance(p1, p2)
print(dist)  # Output: 2.8284271247461903
