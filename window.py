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
        # Set the ranges of cropping scales
        cropXRight.configure(from_=0, to=imageHelper.width)
        cropYTop.configure(from_=0, to=imageHelper.height)
        cropXLeft.configure(from_=0, to=imageHelper.width)
        cropYBottom.configure(from_=0, to=imageHelper.height)


# Rotate the image left
def transpose():
    if imageHelper:
        imageHelper.transpose()
        image = imageHelper.get_photo_image()
        set_image(image)


def vertically_flip():
    if imageHelper:
        imageHelper.vertically_flip()
        image = imageHelper.get_photo_image()
        set_image(image)


# Crop method, which in turns call the crop method of image helper class
def crop():
    if imageHelper:
        image = imageHelper.crop(cropParams[0][0].get(), cropParams[0][1].get(), cropParams[1][0].get(),
                                 cropParams[1][1].get())
        if image:
            set_image(image)


def set_image(image):
    imageLabel.configure(image=image)
    imageLabel.image = image


def show_original():
    image = imageHelper.get_photo_image()
    set_image(image)


window = tk.Tk()
# Screen size
screen_size = window.winfo_screenwidth(), window.winfo_screenheight()
# Set the geometry of the screen. 100 pixels less from actual size of the screen
window.geometry(str(screen_size[0] - 200) + "x" + str(screen_size[0] - 200))

# Frame on the top. This will be used to shw buttons.
topFrame = tk.Frame(window)
topFrame.grid()

# add load button
loadButton = tk.Button(topFrame, text="Load Image", command=load_image)
loadButton.grid(row=0, column=0)
# add rotate button
rotateButton = tk.Button(topFrame, text="Transpose", command=transpose)
rotateButton.grid(row=0, column=1)
# Add Vertical Flip button
verticalFlipButton = tk.Button(topFrame, text="Vertical Flip", command=vertically_flip)
verticalFlipButton.grid(row=0, column=2)

# The list of lists used to track the values of the sliders
cropParams = [[tk.DoubleVar(), tk.DoubleVar()], [tk.DoubleVar(), tk.DoubleVar()]]
cropXLeft = tk.Scale(topFrame, orient=tk.HORIZONTAL, from_=0, to=100, label="X Axis - Left", variable=cropParams[0][0])
cropXLeft.grid(row=0, column=3)
cropYTop = tk.Scale(topFrame, orient=tk.HORIZONTAL, from_=0, to=100, label="Y Axis - Top", variable=cropParams[0][1])
cropYTop.grid(row=1, column=3)
cropXRight = tk.Scale(topFrame, orient=tk.HORIZONTAL, from_=0, to=100, label="X Axis - Right",
                      variable=cropParams[1][0])
cropXRight.grid(row=0, column=4)
cropYBottom = tk.Scale(topFrame, orient=tk.HORIZONTAL, from_=0, to=100, label="Y Axis - Bottom",
                       variable=cropParams[1][1])
cropYBottom.grid(row=1, column=4)

# Crop Button.
croptButton = tk.Button(topFrame, text="Crop", command=crop)
croptButton.grid(row=0, column=5)
showOriginalButton = tk.Button(topFrame, text="Show Original", command=show_original)
showOriginalButton.grid(row=1, column=5)

# Add label to show image
imageLabel = tk.Label(topFrame)
imageLabel.grid(row=2, column=0, columnspan=6)

window.mainloop()
