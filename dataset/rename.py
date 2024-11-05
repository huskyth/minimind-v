#

import cv2
import shutil

for i in range(1025):
    key = (4 - len(str(i + 1))) * '0' + str(i + 1)
    name = key + '.png'

    src = f"sft_images\\{name}"
    to = "cp\\COCO_train2014_" + name
    shutil.copy(src, to)
