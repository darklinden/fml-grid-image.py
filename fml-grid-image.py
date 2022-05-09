#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import os

from PIL import Image

w = 420
h = 420

count_w = 21
count_h = 21

color_bg = '#F0F0F0'
color_light = '#BAE5DB'
color_dark = '#55D2BA'

# 3AD4FB,#2E7979,#55D2BA,#BAE5DB,#C9ECE9


def make_img():

    name = 'img.png'
    path = os.path.join(os.getcwd(), name)
    if os.path.isfile(path):
        os.remove(path)

    newImg = Image.new('RGBA', (w, h), (0, 0, 0, 255))

    cell_width = math.floor(w / count_w)
    cell_height = math.floor(h / count_h)

    for x in range(0, count_w):
        is_color_x = x % 2 == 1
        left = x * cell_width

        for y in range(0, count_h):
            is_color_y = y % 2 == 1
            top = y * cell_height

            color = hex_to_color(color_bg)
            if is_color_x and is_color_y:
                color = hex_to_color(color_dark)
            elif is_color_x or is_color_y:
                color = hex_to_color(color_light)

            cell = Image.new('RGBA', (cell_width, cell_height), color)
            newImg.paste(cell, (left, top))

    newImg.save(path)


def hex_to_color(s: str):
    h = s.lstrip('#')
    if len(h) == 8:
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4, 6))
    elif len(h) == 6:
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    else:
        raise s + ' is not color'


def main():

    make_img()

    print('Done')


if __name__ == "__main__":
    main()
