# -*- coding: utf-8 -*-
# @Time    : 26/11/2020 23:24
# @Author  : Aydar
# @FileName: convert.py
# @Software: PyCharm
# @Telegram   ：aydardev

from PIL import Image, ImageDraw, ImageFont
import logging
from datetime import datetime

from settings import (
    FONT_PATH,
    FONT_COLOR,
    OUT_IMG_FORMAT,
    OUT_IMG_NAME,
    OUT_IMG_FOLDER_PATH,
    LOG_FOLDER_PATH,
    ALIGN
)

log_name = datetime.today().strftime('%Y-%m-%d')
logging.basicConfig(
    format='%(asctime)s :: %(message)s',
    level=logging.INFO,
    filename=LOG_FOLDER_PATH + "/" + log_name + '.log'
)


def convert_image(image_, text_, index_):
    try:
        img = Image.open(image_)
        draw = ImageDraw.Draw(img)
        fonts = ImageFont.truetype(FONT_PATH + ".ttf", size=80)
        draw.text(
            (30, 30), str(text_), font=fonts, fill=FONT_COLOR,
        )
        img.save(
            OUT_IMG_FOLDER_PATH + "/" + OUT_IMG_NAME + str(index_) + "." + OUT_IMG_FORMAT,
            OUT_IMG_FORMAT
        )
        logging.info("Success file = {}, message: {}".format(image_, "convert success"))
    except Exception as e:
        logging.error("Error file = {}, message: {}".format(image_, e))
