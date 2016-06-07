from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt


class ImageHelper:
    # pixels array is in the form [height,width,(r g b)]
    def __init__(self, image_name=""):
        if len(image_name) != 0:
            self.image = Image.open(image_name)
            # Keep the original image for future use
            self.original = self.image.copy()
            self.pixels = np.array(self.image)
            self.temp_pixels = self.pixels.copy()
            self.width, self.height = self.image.size

    def get_photo_image(self):
        return ImageTk.PhotoImage(self.image)

    def get_original_image(self):
        return ImageTk.PhotoImage(self.original)

    # height->width, width->height. shape[0]=>height, shape[1]=>width
    def transpose(self):
        new_image = np.zeros((self.pixels.shape[1], self.pixels.shape[0], 3))
        # Assign each row to a column in the new matrix
        for i in range(self.pixels.shape[0]):
            new_image[:, i, :] = self.pixels[i, :, :]
        self.temp_pixels = new_image
        self.image = Image.fromarray(np.uint8(new_image))

    # Vertically flips the image
    def vertically_flip(self):
        new_image = np.zeros((self.pixels.shape[0], self.pixels.shape[1], 3))
        width = self.pixels.shape[1]
        # Traverse the columns and interchange them
        for i in range(self.pixels.shape[1]):
            new_image[:, i, :] = self.pixels[:, width - i - 1, :]
        self.temp_pixels = new_image
        self.image = Image.fromarray(np.uint8(new_image))

    def crop(self, xLeft, yLeft, xRight, yRight):
        if xLeft < xRight and yLeft < yRight:
            cropped_pixels = self.pixels[yLeft:yRight, xLeft:xRight, :]
            self.image = Image.fromarray(np.uint8(cropped_pixels))
            self.temp_pixels = cropped_pixels

    def show_histogram(self):
        histogram = self.image.histogram()
        bands = self.image.getbands()
        plt.close("all")
        figure = plt.figure(1)
        figure.suptitle("Histograms")
        for x in range(len(bands)):
            plt.subplot(310 + x + 1)
            intensities = histogram[x * 256:(x + 1) * 256]
            plt.bar(range(0, len(intensities)), intensities, color=bands[x].lower())
            plt.grid(True)
        plt.show()

    def adjust_brightness(self, percentage):
        val = (100 + int(percentage)) / 100
        if val < 1:
            self.temp_pixels = val * self.pixels
            self.temp_pixels = self.temp_pixels.astype(np.int8)
        elif val > 1:
            enhanced = val * self.pixels
            np.clip(enhanced, 0, 255, out=enhanced)
            self.temp_pixels = enhanced.astype(np.uint8)
        self.image = Image.fromarray(np.uint8(self.temp_pixels))
