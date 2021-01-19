import os
import pilgram
from PIL import Image


def doFilterPIL(filter_name, pil_image):
    if filter_name == 'inkwell':
        return pilgram.inkwell(pil_image)
    elif filter_name == 'aden':
        return pilgram.aden(pil_image)
    elif filter_name == 'clarendon':
        return pilgram.clarendon(pil_image)

def doFilter(filter_name, pil_image, output_path):
    if filter_name == 'inkwell':
        pilgram.inkwell(pil_image).save(output_path)
    elif filter_name == 'aden':
        pilgram.aden(pil_image).save(output_path)
    elif filter_name == 'clarendon':
        pilgram.clarendon(pil_image).save(output_path)


def pilgram_aden(pil_image, output_path):
    pilgram.aden(pil_image).save(output_path)


def pilgram_inkwell(pil_image, output_path):
    pilgram.inkwell(pil_image).save(output_path)


def pilgram_clarendon(pil_image, output_path):
    pilgram.clarendon(pil_image).save(output_path)


def im_gray_scale(original_path, output_path):
    cmd = 'convert {} -set colorspace Gray -separate -average {}'.format(original_path, output_path)
    print(cmd)
    os.system(cmd)


def im_sepia(original_path, output_path):
    cmd = 'convert {} -set colorspace RGB -sepia-tone 80% {}'.format(original_path, output_path)
    print(cmd)
    os.system(cmd)


def im_color_temp(temperature, original_path, output_path):
    cmd = 'colortemp -t {} {} {}'.format(temperature, original_path, output_path)
    print(cmd)
    os.system(cmd)


def gray_scale(source_name, result_name):
    source = source_name  # Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
            result.putpixel((x, y), (gray, gray, gray))
    result.save(result_name, "JPEG")


def sepia(source_name, result_name):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            red = int(r * 0.393 + g * 0.769 + b * 0.189)
            green = int(r * 0.349 + g * 0.686 + b * 0.168)
            blue = int(r * 0.272 + g * 0.534 + b * 0.131)
            result.putpixel((x, y), (red, green, blue))
    result.save(result_name, "JPEG")


def contrast(source_name, result_name, coefficient=2):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)

    avg = 0
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            avg += r * 0.299 + g * 0.587 + b * 0.114
    avg /= source.size[0] * source.size[1]

    palette = []
    for i in range(256):
        temp = int(avg + coefficient * (i - avg))
        if temp < 0:
            temp = 0
        elif temp > 255:
            temp = 255
        palette.append(temp)

    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            result.putpixel((x, y), (palette[r], palette[g], palette[b]))

    result.save(result_name, "JPEG")
