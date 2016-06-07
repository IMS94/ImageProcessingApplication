import tkinter as tk
from tkinter.filedialog import askopenfilename
from Utils.ImageHelper import ImageHelper

# Image Helper instance to be used through out the application
imageHelper = None


# Load the image from a file picker when the button is clicked
def load_image():
    global imageHelper
    image_name = askopenfilename(title="Select an Image",
                                 filetypes=[('all files', '.*'), ('image files', '.jpg')])
    if len(image_name) > 0:
        imageHelper = ImageHelper(image_name)
        image = imageHelper.get_photo_image()
        set_image(image)
        update_scales()


def update_scales():
    if imageHelper:
        # Set the ranges of cropping scales
        cropXRight.configure(from_=0, to=imageHelper.width)
        cropXRight.set(imageHelper.width)
        cropYTop.configure(from_=0, to=imageHelper.height)
        cropYTop.set(0)
        cropXLeft.configure(from_=0, to=imageHelper.width)
        cropXLeft.set(0)
        cropYBottom.configure(from_=0, to=imageHelper.height)
        cropYBottom.set(imageHelper.height)


# Rotate the image left
def transpose():
    if imageHelper:
        imageHelper.transpose()
        image = imageHelper.get_photo_image()
        set_image(image)
        update_scales()


def vertically_flip():
    if imageHelper:
        imageHelper.vertically_flip()
        image = imageHelper.get_photo_image()
        set_image(image)


# Crop method, which in turns call the crop method of image helper class
def crop(val):
    if imageHelper:
        imageHelper.crop(cropXLeft.get(), cropYTop.get(), cropXRight.get(), cropYBottom.get())
        image = imageHelper.get_photo_image()
        set_image(image)


def accept_crop():
    if imageHelper:
        imageHelper.set_cropped()
        image = imageHelper.get_photo_image()
        set_image(image)
        update_scales()


def show_histogram():
    if imageHelper:
        imageHelper.show_histogram()


def adjust_brightness(val):
    if imageHelper:
        imageHelper.adjust_brightness(val)
        image = imageHelper.get_photo_image()
        set_image(image)


def adjust_contrast(val):
    if imageHelper:
        imageHelper.adjust_contrast(val)
        image = imageHelper.get_photo_image()
        set_image(image)


def accept_brightness_contrast():
    if imageHelper:
        imageHelper.accept_brightness_contrast()
        image = imageHelper.get_photo_image()
        set_image(image)
        update_scales()


# Set the currently shown image
def set_image(image):
    imageLabel.configure(image=image)
    imageLabel.image = image


def show_original():
    if imageHelper:
        image = imageHelper.get_original_image()
        set_image(image)
        update_scales()


def reset():
    if imageHelper:
        imageHelper.reset()
        image = imageHelper.get_original_image()
        set_image(image)
        update_scales()


window = tk.Tk()
# Screen size
screen_size = window.winfo_screenwidth(), window.winfo_screenheight()
# Set the geometry of the screen. 100 pixels less from actual size of the screen
window.geometry(str(screen_size[0] - 200) + "x" + str(screen_size[0] - 200))
window.grid()

# Frame on the top. This will be used to shw buttons.
topFrame = tk.Frame(window)
topFrame.grid(row=0)

# add load button
loadButton = tk.Button(topFrame, text="Load Image", command=load_image)
loadButton.grid(row=0, column=0)
showOriginalButton = tk.Button(topFrame, text="Show Original", command=show_original)
showOriginalButton.grid(row=1, column=1)
resetButton = tk.Button(topFrame, text="Reset", command=reset)
resetButton.grid(row=1, column=0)

# add rotate button
rotateButton = tk.Button(topFrame, text="Transpose", command=transpose)
rotateButton.grid(row=0, column=1)
# Add Vertical Flip button
verticalFlipButton = tk.Button(topFrame, text="Vertical Flip", command=vertically_flip)
verticalFlipButton.grid(row=0, column=2)

# The list of lists used to track the values of the sliders
cropParams = [[tk.DoubleVar(), tk.DoubleVar()], [tk.DoubleVar(), tk.DoubleVar()]]
cropXLeft = tk.Scale(topFrame, orient=tk.HORIZONTAL, from_=0, to=100, label="X Axis - Left", command=crop)
cropXLeft.grid(row=0, column=3)
cropYTop = tk.Scale(topFrame, orient=tk.HORIZONTAL, from_=0, to=100, label="Y Axis - Top", command=crop)
cropYTop.grid(row=1, column=3)
cropXRight = tk.Scale(topFrame, orient=tk.HORIZONTAL, from_=0, to=100, label="X Axis - Right", command=crop)
cropXRight.grid(row=0, column=4)
cropYBottom = tk.Scale(topFrame, orient=tk.HORIZONTAL, from_=0, to=100, label="Y Axis - Bottom", command=crop)
cropYBottom.grid(row=1, column=4)

# Crop Button.
cropButton = tk.Button(topFrame, text="Crop", command=accept_crop)
cropButton.grid(row=0, column=5, rowspan=2)

# Histogram Button
histogramButton = tk.Button(topFrame, text="Histogram", command=show_histogram)
histogramButton.grid(row=0, column=7)
tk.Button(topFrame, text="Accept", command=accept_brightness_contrast).grid(row=1, column=7)

# Adjust brightness and contrast
adjustBrightness = tk.Scale(topFrame, orient=tk.HORIZONTAL, from_=-100, to=100, label="Brightness",
                            command=adjust_brightness)
adjustBrightness.grid(row=0, column=6)
adjustContrast = tk.Scale(topFrame, orient=tk.HORIZONTAL, from_=-100, to=100, label="Contrast",
                          command=adjust_contrast)
adjustContrast.grid(row=1, column=6)

# Add label to show image
imageLabel = tk.Label(topFrame)
imageLabel.grid(row=2, column=0, columnspan=8)

window.mainloop()
