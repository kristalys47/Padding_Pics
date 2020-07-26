from PIL import Image, ImageOps
import numpy as np
import sys,os


def pic(photo_import, photo_export):
    size_6 = 6
    size_4 = 4
    print(photo_import)
    image = Image.open(photo_import)
    original_size = image.size # (width -, height |)
    padded_image = None
    new_size = None

    if original_size[0] <= original_size[1]:
        # width is <= than length (4x6)
        unit_4 = original_size[0] / size_4
        unit_6 = original_size[1] / size_6
        proportions4 = int(unit_4 * size_6)
        proportions6 = int(unit_6 * size_4)

        if proportions4 <= original_size[1]:
            # heigth is the norm
            new_size = (proportions6, original_size[1])
            # padding side
        else:
            # weigth is the norm
            new_size = (original_size[0], proportions4)
            # padding down

    else:
        # width is > than length (6x4)
        unit_4 = original_size[1] / size_4
        unit_6 = original_size[0] / size_6
        proportions4 = int(unit_4 * size_6)
        proportions6 = int(unit_6 * size_4)

        if proportions4 <= original_size[0]:
            # weight is the norm
            new_size = (original_size[0],proportions6)
            # padding down
        else:
            # heigth is the norm
            new_size = (proportions4, original_size[1])
            # padding side


    print("new size ", new_size)

    padded_image = Image.new("RGB", new_size, (255,255,255)) # White padding, can change to black (0,0,0) or any other color that is prefered

    img = np.asarray(padded_image)
    new_img=img.copy()
    org_img = np.asarray(image)

    for x in range(new_size[1]):
        for y in range(new_size[0]):
            try:
                new_img[x, y] = org_img[x, y]
            except:
                continue

    padded_image = Image.fromarray(new_img, 'RGB')
    padded_image.save(photo_export)
    print("Done")


photos = os.listdir("Photos")
count = len(photos)
n_file = ".DS_Store"

for photo in photos:
    if photo == n_file:
        continue
    print("Start # ", count)
    path_in = "Photos/" + photo
    path_out = "Edited/" + photo
    pic(path_in, path_out)
    count -= 1
