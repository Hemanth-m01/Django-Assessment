class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Yield length first, then width
        yield {'length': self.length}
        yield {'width': self.width}

rect = Rectangle(10, 5)

for dimension in rect:
    print(dimension)