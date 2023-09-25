class Cube:

    # constructor of the class
    def __init__(self, length, breadth, height):
        print(id(self))
        self.length = length
        self.breadth = breadth
        self.height = height

    # second constructor -> TypeError: Cube.__init__() takes 1 positional argument but 4 were given, as overrides the first one
    # def __init__(self):
    #     pass

    def calculate_lid_area(self):
        return self.length * self.breadth
    
    def calculate_surface_area(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height)
    
    def calculate_volume(self):
        return self.length * self.breadth * self.height
    
cube1 = Cube(10, 5, 3)
print(cube1.calculate_lid_area(), cube1.calculate_volume()) # self -> c1
print('ID value of cube1 obj: ', id(cube1), '\n')

cube2 = Cube(20, 10, 5)
print(cube1.calculate_surface_area(), cube2.calculate_volume()) # self -> c2
print('ID value of cube2 obj: ', id(cube2))

