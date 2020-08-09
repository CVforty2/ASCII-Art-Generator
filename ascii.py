from PIL import Image
import numpy as np


def __convert_to_grayscale(image):
    """
    rgb to grayscale using the pillow library
    """
    return image.convert('L')


def __pixel_to_ascii_char(image):
    """
    converts the pixel value into a designated ascii char
    """
    ascii_list = []

    # list of values ranging from 0-255
    list_of_pixel_vals = list(image.getdata())

    for i in range(len(list_of_pixel_vals)):
        val = list_of_pixel_vals[i] / 255

        if 0.0 <= val and val < 0.1:
            ascii_list.append('.')
        elif 0.1 <= val and val < 0.2:
            ascii_list.append(',')
        elif 0.2 <= val and val < 0.3:
            ascii_list.append(';')
        elif 0.3 <= val and val < 0.4:
            ascii_list.append('!')
        elif 0.4 <= val and val < 0.5:
            ascii_list.append('v')
        elif 0.5 <= val and val < 0.6:
            ascii_list.append('l')
        elif 0.6 <= val and val < 0.7:
            ascii_list.append('L')
        elif 0.7 <= val and val < 0.8:
            ascii_list.append('F')
        elif 0.8 <= val and val < 0.9:
            ascii_list.append('E')
        else:
            #  0.9 <= val and val < 1.0:
            ascii_list.append('$')


    width, height = image.size

    # reshape the 1D List into a 2D array based on image dimensions
    ascii_list = np.reshape(ascii_list, (width, height))

    return ascii_list


def __write_to_txt_file(grid, filename):
    """
    converts a 2D Array into a text file
    """
    with open(filename, 'w') as ascii_art:
        for h in range(len(grid)):
            for r in range(len(grid[h])):
                print(grid[h][r], file=ascii_art, end='')
            print('', file=ascii_art)


def generate_ascii_art(image):

    image_name = image.split('.')[0]
    image = Image.open(image)
    image = __convert_to_grayscale(image)
    image = __pixel_to_ascii_char(image)
    __write_to_txt_file(image, f"{image_name}_ascii_art.txt")



def main():
    filename = "hotdog.png"
    generate_ascii_art(filename)


if __name__ == "__main__":
    main()
