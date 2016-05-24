from tkinter import *
from Utils.ImageHelper import ImageHelper

window = Tk()
window.geometry("500x500")


def load_image():
    image = ImageHelper("/home/imesha/Downloads/Technology-001.jpg")
    image.load_image()
    image.print_image()


button = Button(window, text="Load Image", command=load_image)
button.place(x=10, y=10)
window.mainloop()
