from PIL import Image
import numpy as np


class ImageHelper:
    def __init__(self, image_name):
        self.image = Image.open(image_name)
        self.width, self.height = self.image.size
        self.pixels = False

    # Load the image and store all the pixels.
    def load_image(self):
        self.pixels = np.zeros((self.width, self.height, 3))
        pixels = self.image.load()
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = pixels[i, j]
                self.pixels[i, j, :] = r, g, b

    def print_image(self):
        print(self.pixels)
