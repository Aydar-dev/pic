# -*- coding: utf-8 -*-
# @Time    : 26/11/2020 23:16
# @Author  : Aydar
# @FileName: settings.py
# @Software: PyCharm
# @Telegram   ：aydardev
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME = "pci"
PROJECT_PATH = BASE_DIR + "/" + PROJECT_NAME

FONTS_FOLDER_NAME = "fonts"
FONT_FILE_NAME = "FiraCode-Regular"
FONT_PATH = PROJECT_PATH + "/" + FONTS_FOLDER_NAME + "/" + FONT_FILE_NAME
FONT_COLOR = "#000000"

OUT_IMG_FOLDER_NAME = "out"
OUT_IMG_FOLDER_PATH = PROJECT_PATH + "/" + OUT_IMG_FOLDER_NAME
OUT_IMG_FORMAT = "jpeg"
OUT_IMG_NAME = "demo"

INPUT_IMG_FOLDER_NAME = "img"
INPUT_IMG_FOLDER_PATH = PROJECT_PATH + "/" + INPUT_IMG_FOLDER_NAME

LOG_FOLDER_NAME = "log"
LOG_FOLDER_PATH = PROJECT_PATH + "/" + LOG_FOLDER_NAME

FIRST_INDEX = 1000
