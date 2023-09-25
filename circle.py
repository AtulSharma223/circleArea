import math
class circle:
  def __init__(self,r):
    self.r=r
  def area(self):
    area=math.pi*(self.r**2)
    return area
  def paremeter(self):
    p=2*math.pi*(self.r)
    return p

radius=float(input("Enter radius "))
circle1=circle(radius)
print("Arear is",circle1.area())
print("Paremeter is",circle1.paremeter())
