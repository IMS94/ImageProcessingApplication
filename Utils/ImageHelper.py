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
        return ImageTk.PhotoImage(self.image);

    # height->width, width->height. shape[0]=>height, shape[1]=>width
    def rotate_left(self):
        new_image = np.zeros((self.pixels.shape[1], self.pixels.shape[0], 3))
        for i in range(self.pixels.shape[0]):
            for j in range(self.pixels.shape[1]):
                new_image[j, i, :] = self.pixels[i, j, :]
        self.pixels = new_image
        self.image = Image.fromarray(np.uint8(new_image))
