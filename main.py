import os
from os import listdir
from os.path import isfile, join
from settings import (
    INPUT_IMG_FOLDER_PATH as PATH,
    INPUT_IMG_FOLDER_PATH, OUT_IMG_NAME, FIRST_INDEX,
)
from convert import (
    convert_image
)

FILE_COUNT = len([lists for lists in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, lists))])
FULL_FILE = [f for f in listdir(PATH) if isfile(join(PATH, f))]


def image_worker():
    for item in range(FILE_COUNT):
        convert_image(
            image_=INPUT_IMG_FOLDER_PATH + "/" + FULL_FILE[item],
            text_=FIRST_INDEX + item,
            index_=item,
        )


if __name__ == '__main__':
    try:
        image_worker()
        print("work done")
    except Exception as e:
        print(e)
