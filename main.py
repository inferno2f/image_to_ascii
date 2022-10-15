import os

from PIL import Image


ascii_map = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def read_image(image_name: str) -> Image:
    return Image.open(os.path.join(f'media/{image_name}'))

def get_image_pixel_data(image: Image) -> list:
    """ Gets RGB data for every pixel of the image """
    return list(image.getdata())

def get_average_brightness(pixel_data: list) -> list:
    """ Converts RGB values to a single value (average brightness) """
    for i in range(len(pixel_data)):
        pixel_data[i] = sum(pixel_data[i]) // 3
    return pixel_data

def calculate_brightness_percentage(brightness: int) -> float:
    return (brightness // (255 / 100))

def pixel_to_ascii(pixel_data: list, ascii_map: str) -> str:
    pixel_data = get_average_brightness(pixel_data)
    for i in range(len(pixel_data)):
        index = int(len(ascii_map) / 100 * calculate_brightness_percentage(pixel_data[i]))
        pixel_data[i] = ascii_map[index-1]
    return pixel_data


if __name__ == '__main__':
    image_name = 'Mario.jpeg'
    image = read_image(image_name)
    pixel_data = get_image_pixel_data(image)
    print("".join(pixel_to_ascii(pixel_data, ascii_map)))
