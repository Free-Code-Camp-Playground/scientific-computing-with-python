class Rectangle():
  def __init__(self, width, height):
    self.width=width
    self.height=height

  def set_width(self, width):
    self.width=width

  def set_height(self, height):
    self.height=height

  def get_area(self):
    w=self.width
    h=self.height
    return w*h

  def get_perimeter(self):
    w=self.width
    h=self.height
    return 2*w + 2*h

  def get_diagonal(self):
    w=self.width
    h=self.height
    return (w*w + h*h)**0.5

  def get_picture(self):
    out=""
    if self.width>50 or self.height>50:
      return "Too big for picture."

    for line in range(self.height):
      out+="*"*self.width+"\n"
    return out

  def get_amount_inside(self, shape):
    nWidth = self.width//shape.width
    nHeight = self.height//shape.height
    return int(nWidth*nHeight)

  def __str__(self):
    w=self.width
    h=self.height
    return f"Rectangle(width={w}, height={h})"

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    # Rectangle.__init__(self, side, side)

  def set_side(self, side):
    self.width=side
    self.height=side

  def __str__(self):
    w=self.width
    return f"Square(side={w})"

def main():
  rect = Rectangle(10, 5)
  print(rect.get_area())
  rect.set_height(3)
  print(rect.get_perimeter())
  print(rect)
  print(rect.get_picture())

  sq = Square(9)
  print(sq.get_area())
  sq.set_side(4)
  print(sq.get_diagonal())
  print(sq)
  print(sq.get_picture())

  rect.set_height(8)
  rect.set_width(16)
  print(rect.get_amount_inside(sq))



if __name__ == "__main__":
  main()