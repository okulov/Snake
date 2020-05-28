class Point:
    def __init__(self, x, y, sym):
        self.x = x
        self.y = y
        self.sym = sym

    def draw(self, holst):
        holst.drawing_sym(self.x, self.y, self.sym)


class HorizontalLine:
    # def __init__(self):
    #     self.pList = []

    def __init__(self, xLeft, xRight, y, sym):
        self.pList = []
        for i in range(xLeft, xRight):
            p = Point(i, y, sym)
            self.pList.append(p)

    def draw(self,holst):
        for point in self.pList:
            print(point.x)
            point.draw(holst)
