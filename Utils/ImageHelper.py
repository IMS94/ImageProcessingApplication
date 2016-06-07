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
            # Keeps the temporarily processed image pixels
            self.pixels = np.array(self.image)
            # Keep the cropped image's pixels
            self.cropped_pixels = None
            self.temp_pixels = None
            self.width, self.height = self.image.size

    def get_photo_image(self):
        return ImageTk.PhotoImage(self.image)

    def get_original_image(self):
        return ImageTk.PhotoImage(self.original)

    def reset(self):
        self.pixels = np.array(self.original)
        self.update_image(self.original.copy())

    def update_image(self, image):
        self.image = image
        self.width, self.height = self.image.size

    # height->width, width->height. shape[0]=>height, shape[1]=>width
    def transpose(self):
        new_image = np.zeros((self.pixels.shape[1], self.pixels.shape[0], 3))
        # Assign each row to a column in the new matrix
        for i in range(self.pixels.shape[0]):
            new_image[:, i, :] = self.pixels[i, :, :]
        self.pixels = new_image
        self.update_image(Image.fromarray(np.uint8(new_image)))

    # Vertically flips the image
    def vertically_flip(self):
        new_image = np.zeros((self.pixels.shape[0], self.pixels.shape[1], 3))
        width = self.pixels.shape[1]
        # Traverse the columns and interchange them
        for i in range(self.pixels.shape[1]):
            new_image[:, i, :] = self.pixels[:, width - i - 1, :]
        self.pixels = new_image
        self.update_image(Image.fromarray(np.uint8(new_image)))

    def crop(self, xLeft, yLeft, xRight, yRight):
        width = self.pixels.shape[1]
        height = self.pixels.shape[0]
        if xLeft < xRight and yLeft < yRight and xRight <= width and yRight <= height:
            cropped_pixels = self.pixels[yLeft:yRight, xLeft:xRight, :]
            self.cropped_pixels = cropped_pixels
            self.image = Image.fromarray(np.uint8(cropped_pixels))

    def set_cropped(self):
        if self.cropped_pixels is not None:
            self.pixels = self.cropped_pixels
            self.update_image(Image.fromarray(np.uint8(self.pixels)))

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
            plt.xlim([-1, 256])
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

    def adjust_contrast(self, percentage):
        percentage = 1 - int(percentage) / 100
        uppermargin = 255 * percentage
        enhanced = (255 - uppermargin) / 2 + percentage * self.pixels
        np.clip(enhanced, 0, 255, out=enhanced)
        self.temp_pixels = enhanced.astype(np.uint8)
        self.image = Image.fromarray(np.uint8(self.temp_pixels))

    def accept_brightness_contrast(self):
        if self.temp_pixels is not None:
            self.pixels = self.temp_pixels
            self.update_image(Image.fromarray(np.uint8(self.pixels)))
