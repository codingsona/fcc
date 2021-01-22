class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # print("width and height is:",width , height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
        print("Width:", width)

    def set_height(self, height):
        self.height = height
        print("Height:", height)

    def get_area(self):
        area = (self.height * self.width)
        print("Area:", area)
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.height + self.width)
        print("Perimeter:", perimeter)
        return perimeter

    def get_diagonal(self):
        print("Diagonal")
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, rectangle):
        if self.width < rectangle.width or self.height < rectangle.height:
            return 0
        width_multiple = int(self.width / rectangle.width)
        height_mutliple = int(self.height / rectangle.height)

        return width_multiple * height_mutliple


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_side(self, num):
        self.width = num
        self.height = num

    def set_width(self, num):
        self.set_side(num)

    def set_height(self, num):
        self.set_side(num)







