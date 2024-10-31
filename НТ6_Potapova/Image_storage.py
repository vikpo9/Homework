#1
class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []

    def __repr__(self):
        return f"Image ({self.width}x{self.height})"

    def display(self):
        for row in self.pixels:
            print(" ".join(map(str, row)))

class BinaryImage(Image):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.pixels = [[0 for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, value):
        if value in (0, 1):
            self.pixels[y][x] = value
        else:
            raise ValueError("Binary image can only have values 0 or 1")

    def __repr__(self):
        return f"BinaryImage ({self.width}x{self.height})"

class MonochromeImage(Image):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.pixels = [[0 for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, value):
        if 0 <= value <= 255:
            self.pixels[y][x] = value
        else:
            raise ValueError("Monochrome image can only have values from 0 to 255")

    def __repr__(self):
        return f"MonochromeImage ({self.width}x{self.height})"

class ColorImage(Image):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.pixels = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, value):
        if (isinstance(value, tuple) and len(value) == 3 and
                all(0 <= v <= 255 for v in value)):
            self.pixels[y][x] = value
        else:
            raise ValueError("Color image pixels must be a tuple with 3 values (R, G, B) in range 0-255")

    def __repr__(self):
        return f"ColorImage ({self.width}x{self.height})"



binary_image = BinaryImage(4, 4)
binary_image.set_pixel(1, 1, 1)
binary_image.set_pixel(2, 2, 1)
print(binary_image)
binary_image.display()

mono_image = MonochromeImage(3, 3)
mono_image.set_pixel(0, 0, 100)
mono_image.set_pixel(1, 1, 150)
mono_image.set_pixel(2, 2, 255)
print(mono_image)
mono_image.display()

color_image = ColorImage(2, 2)
color_image.set_pixel(0, 0, (255, 0, 0))  # Красный
color_image.set_pixel(1, 0, (0, 255, 0))  # Зеленый
color_image.set_pixel(0, 1, (0, 0, 255))  # Синий
color_image.set_pixel(1, 1, (255, 255, 0))  # Желтый
print(color_image)
color_image.display()

#2

import math

class ImageConverter:
    @staticmethod
    def monochrome_to_monochrome(image, correction_factor=1.0):
        new_image = MonochromeImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                new_value = min(255, max(0, int(image.pixels[y][x] * correction_factor)))
                new_image.set_pixel(x, y, new_value)
        return new_image

    @staticmethod
    def color_to_color(image, correction_factors=(1.0, 1.0, 1.0)):
        new_image = ColorImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                r, g, b = image.pixels[y][x]
                new_r = min(255, max(0, int(r * correction_factors[0])))
                new_g = min(255, max(0, int(g * correction_factors[1])))
                new_b = min(255, max(0, int(b * correction_factors[2])))
                new_image.set_pixel(x, y, (new_r, new_g, new_b))
        return new_image

    @staticmethod
    def binary_to_binary(image):
        return image

    @staticmethod
    def color_to_monochrome(image):
        new_image = MonochromeImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                r, g, b = image.pixels[y][x]
                gray = (r + g + b) // 3
                new_image.set_pixel(x, y, gray)
        return new_image

    @staticmethod
    def monochrome_to_color(image, palette):
        new_image = ColorImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                gray_value = image.pixels[y][x]
                color = palette.get(gray_value, (0, 0, 0))
                new_image.set_pixel(x, y, color)
        return new_image

    @staticmethod
    def monochrome_to_binary(image, threshold=128):
        new_image = BinaryImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                pixel_value = image.pixels[y][x]
                binary_value = 1 if pixel_value >= threshold else 0
                new_image.set_pixel(x, y, binary_value)
        return new_image

    @staticmethod
    def binary_to_monochrome(image):
        new_image = MonochromeImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                if image.pixels[y][x] == 1:
                    new_image.set_pixel(x, y, 0)
                else:
                    min_dist = float('inf')
                    for j in range(image.height):
                        for i in range(image.width):
                            if image.pixels[j][i] == 1:
                                dist = math.sqrt((x - i) ** 2 + (y - j) ** 2)
                                min_dist = min(min_dist, dist)
                    new_value = min(255, max(0, int(min_dist)))
                    new_image.set_pixel(x, y, new_value)
        return new_image

    @staticmethod
    def color_to_binary(image, threshold=128):
        monochrome_image = ImageConverter.color_to_monochrome(image)
        return ImageConverter.monochrome_to_binary(monochrome_image, threshold)

    @staticmethod
    def binary_to_color(image, palette):
        monochrome_image = ImageConverter.binary_to_monochrome(image)
        return ImageConverter.monochrome_to_color(monochrome_image, palette)


binary_image = BinaryImage(4, 4)
binary_image.set_pixel(1, 1, 1)
binary_image.set_pixel(2, 2, 1)

mono_image = MonochromeImage(4, 4)
mono_image.set_pixel(0, 0, 100)
mono_image.set_pixel(1, 1, 150)

color_image = ColorImage(4, 4)
color_image.set_pixel(0, 0, (255, 0, 0))
color_image.set_pixel(1, 1, (0, 255, 0))

gray_image = ImageConverter.color_to_monochrome(color_image)
print(gray_image)

binary_from_mono = ImageConverter.monochrome_to_binary(mono_image, threshold=120)
print(binary_from_mono)

palette = {0: (0, 0, 0), 1: (255, 255, 255)}
color_from_binary = ImageConverter.binary_to_color(binary_image, palette)
print(color_from_binary)
