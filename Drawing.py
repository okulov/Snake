from tkinter import Tk, Canvas, Frame, BOTH, W


class Holst(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        # self.initUI()
        self.parent.title("Snake")
        self.pack(fill=BOTH, expand=1)

    #
    # def initUI(self):
    #     self.parent.title("Snake")
    #     self.pack(fill=BOTH, expand=1)
    #
    #     canvas = Canvas(self)
    #     canvas.pack(fill=BOTH, expand=1)

    def drawing_sym(self, x, y, sym):
        canvas = Canvas(self)
        canvas.create_text(x, y, anchor=W, font="Purisa", text=sym)
        canvas.pack(fill=BOTH, expand=1)
