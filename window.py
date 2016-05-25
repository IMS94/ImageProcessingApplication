import tkinter as tk
from tkinter.filedialog import askopenfilename
from Utils.ImageHelper import ImageHelper

# Image Helper instance to be used through out the application
imageHelper = False


# Load the image from a file picker when the button is clicked
def load_image():
    global imageHelper
    image_name = askopenfilename(title="Select an Image",
                                 filetypes=[('all files', '.*'), ('image files', '.jpg')])
    if len(image_name) > 0:
        imageHelper = ImageHelper(image_name)
        image = imageHelper.get_photo_image()
        set_image(image)


# Rotate the image left
def rotate_left():
    if imageHelper:
        imageHelper.rotate_left()
        image = imageHelper.get_photo_image()
        set_image(image)


def set_image(image):
    imageLabel.configure(image=image)
    imageLabel.image = image


window = tk.Tk()
# Screen size
screen_size = window.winfo_screenwidth(), window.winfo_screenheight()
# Set the geometry of the screen. 100 pixels less from actual size of the screen
window.geometry(str(screen_size[0] - 200) + "x" + str(screen_size[0] - 200))
# Frame on the top. This will be used to shw buttons.
topFrame = tk.Frame(window)
topFrame.pack()
# Frame on bottom. This will be used to show the loaded image.
bottomFrame = tk.Frame(window)
bottomFrame.pack()
# add load button
loadButton = tk.Button(topFrame, text="Load Image", command=load_image)
loadButton.pack(side=tk.LEFT)
# add rotate button
rotateButton = tk.Button(topFrame, text="Rotate Left", command=rotate_left)
rotateButton.pack(side=tk.LEFT)
# Add label to show image
imageLabel = tk.Label(bottomFrame)
imageLabel.pack(side=tk.BOTTOM)

window.mainloop()
