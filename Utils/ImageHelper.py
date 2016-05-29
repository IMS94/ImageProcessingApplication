from PIL import Image, ImageTk
import numpy as np


class ImageHelper:
    # pixels array is in the form [height,width,(r g b)]
    def __init__(self, image_name=""):
        if len(image_name) != 0:
            self.image = Image.open(image_name)
            self.pixels = np.array(self.image)
            self.width, self.height = self.image.size

    def print_image(self):
        print(self.pixels)

    def get_photo_image(self):
        return ImageTk.PhotoImage(self.image)

    # height->width, width->height. shape[0]=>height, shape[1]=>width
    def transpose(self):
        new_image = np.zeros((self.pixels.shape[1], self.pixels.shape[0], 3))
        # Assign each row to a column in the new matrix
        for i in range(self.pixels.shape[0]):
            new_image[:, i, :] = self.pixels[i, :, :]
        self.pixels = new_image
        self.image = Image.fromarray(np.uint8(new_image))

    # Vertically flips the image
    def vertically_flip(self):
        new_image = np.zeros((self.pixels.shape[0], self.pixels.shape[1], 3))
        width = self.pixels.shape[1]
        # Traverse the columns and interchange them
        for i in range(self.pixels.shape[1]):
            new_image[:, i, :] = self.pixels[:, width - i - 1, :]
        self.pixels = new_image
        self.image = Image.fromarray(np.uint8(new_image))

    def crop(self, xLeft, yLeft, xRight, yRight):
        if xLeft<xRight and yLeft<yRight:
            new_image = self.pixels[yLeft:yRight, xLeft:xRight, :]
            croppedImage = Image.fromarray(np.uint8(new_image))
            return ImageTk.PhotoImage(croppedImage)
        return None