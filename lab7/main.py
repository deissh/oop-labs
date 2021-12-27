import time
import tkinter as tk
import itertools
import threading
from PIL import Image, ImageTk


class StaticImage(tk.Frame):
    image_path: str = "img.png"
    bg_color: str = "white"

    canvas_size = (300, 300)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.img = Image.open(self.image_path)

        self.__setup_canvas()
        self.__grid()

    def __setup_canvas(self):
        self.canvas = tk.Canvas(
            self,
            width=self.canvas_size[0],
            height=self.canvas_size[0],
            background=self.bg_color
        )
        self.canvas.pack()

        self.__draw_img(self.img)

    def __grid(self):
        self.canvas.grid()

    def __draw_img(self, img):
        photo = ImageTk.PhotoImage(img)
        self.label = tk.Label(self, image=photo)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)


class DynamicImage(StaticImage):
    color = itertools.cycle(["white", "red", "green", "blue", "pink", "gray"])

    def __init__(self, parent):
        super(DynamicImage, self).__init__(parent)

        thread = threading.Thread(target=self.__animate)
        thread.daemon = True
        thread.start()

    def __animate(self):
        while True:
            self.__change_image()
            time.sleep(.5)

    def __change_image(self):
        # img = self.img_set.__next()
        # self.__draw_img(img)
        self.canvas.create_rectangle(0, 0, self.canvas_size[0], self.canvas_size[1], fill=self.color.__next__(), outline="")


root = tk.Tk()

tk.Label(root, text="Static image").grid()
StaticImage(root).grid()

tk.Label(root, text="Dynamic image").grid()
DynamicImage(root).grid()

root.mainloop()
