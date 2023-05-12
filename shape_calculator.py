class Rectangle:
  def __init__(self, w, h):
    self.width = w
    self.height = h
  def set_width(self, x):
    self.width = x
  def set_height(self, x):
    self.height = x
  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    rect = str()
    for x in range(self.height):
        rect += "*" * self.width + "\n"
    return rect
  def get_amount_inside(self, obj):
    return (self.width // obj.width) * (self.height // obj.height)
  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    
class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side,side)
  def set_side(self, side):
    self.width = side
    self.height = side
  def __str__(self):
    return "Square(side=" + str(self.width) + ")"
  def set_width(self, x):
    super().set_width(x)
    super().set_height(x)
  def set_height(self, x):
    super().set_width(x)
    super().set_height(x)