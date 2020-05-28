from random import *
from tkinter import Tk, Canvas, Frame, BOTH, W
import Drawing, Point


def main():
    root = Tk()
    root.geometry("600x600+100+100")
    panel = Drawing.Holst(root)
    p1 = Point.Point(10, 20, 'w')
    p2 = Point.Point(100, 200, '*')
    p1.draw(panel)
    p2.draw(panel)

    line = Point.HorizontalLine(20, 30, 10, '+')
    line.draw(panel)
    root.mainloop()


if __name__ == "__main__":
    main()
