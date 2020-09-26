# -*- coding: utf-8 -*-

import pytest
from pibooth import fonts
from pibooth.pictures import sizing
from PIL import Image, ImageDraw, ImageOps


def overlay_legacy(size, text, alpha, font=None):
    """Legacy implementation in pibooth==2.0.0.
    """
    image = Image.new('RGBA', size)
    draw = ImageDraw.Draw(image)

    font = fonts.get_pil_font(text, fonts.CURRENT, 0.9 * size[0], 0.9 * size[1])
    txt_width, txt_height = draw.textsize(text, font=font)

    position = ((size[0] - txt_width) // 2, (size[1] - txt_height) // 2 - size[1] // 10)
    draw.text(position, text, (255, 255, 255, alpha), font=font)
    return image


def overlay_rework1(size, text, alpha, font=None):
    """Avoid creating a font object for each new overlay. Creat a font
    require IO operations on drive.
    """
    image = Image.new('RGBA', size)
    draw = ImageDraw.Draw(image)
    txt_width, txt_height = draw.textsize(text, font=font)

    position = ((size[0] - txt_width) // 2, (size[1] - txt_height) // 2 - size[1] // 10)
    draw.text(position, text, (255, 255, 255, alpha), font=font)
    return image


def pil_legacy(image, resolution, rect, hflip=True, overlay=None):
    """Legacy implementation in pibooth==2.0.0.
    """
    # Crop to keep aspect ratio of the resolution
    image = image.crop(sizing.new_size_by_croping_ratio(image.size, resolution))
    # Resize to fit the available space in the window
    image = image.resize(sizing.new_size_keep_aspect_ratio(image.size, (rect.width, rect.height), 'outer'))

    if hflip:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)

    if overlay:
        image.paste(overlay, (0, 0), overlay)

    return image


def pil_rework1(image, resolution, rect, hflip=True, overlay=None):
    """Use the ``ImageOps.fit`` function to crop and resize the preview.
    """
    image = ImageOps.fit(image, (rect.width, rect.height), method=Image.NEAREST)

    if hflip:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)

    if overlay:
        image.paste(overlay, (0, 0), overlay)

    return image


def pil_rework2(image, resolution, rect, hflip=True, overlay=None):
    """Use a faster algo to resize preview, but with a worse quality.
    """
    box = sizing.new_size_by_croping_ratio(image.size, resolution)
    image = image.resize((rect.width, rect.height), resample=Image.NEAREST, box=box, reducing_gap=1.5)

    if hflip:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)

    if overlay:
        image.paste(overlay, (0, 0), overlay)

    return image


@pytest.mark.parametrize("builder", [overlay_legacy, overlay_rework1])
def test_build_overlay(builder, preview_rect, benchmark):
    font = fonts.get_pil_font("Smile", fonts.CURRENT, 0.9 * preview_rect.size[0], 0.9 * preview_rect.size[1])
    benchmark(builder, preview_rect.size, "Smile", 80, font)


@pytest.mark.parametrize("builder", [pil_legacy, pil_rework1, pil_rework2])
def test_preview(builder, resolution, preview_path, preview_rect, benchmark):
    image = benchmark(builder, Image.open(preview_path), resolution, preview_rect, False)
    image.save(builder.__name__ + ".jpg")


@pytest.mark.parametrize("builder", [pil_legacy, pil_rework1, pil_rework2])
def test_preview_flip(builder, resolution, preview_path, preview_rect, benchmark):
    image = benchmark(builder, Image.open(preview_path), resolution, preview_rect, True)
    image.save(builder.__name__ + "_flip.jpg")


@pytest.mark.parametrize("builder", [pil_legacy, pil_rework1, pil_rework2])
def test_preview_flip_overlay(builder, resolution, preview_path, preview_rect, benchmark):
    overlay = overlay_legacy(preview_rect.size, "Smile", 80)
    image = benchmark(builder, Image.open(preview_path), resolution, preview_rect, True, overlay)
    image.save(builder.__name__ + "_flip_overlay.jpg")
