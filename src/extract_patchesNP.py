import pandas as pd
import numpy as np
from skimage import img_as_ubyte
from skimage.io import imread, imsave
import matplotlib.pyplot as plt
import os
import warnings

if not os.path.exists('PATCHES_NP'):
    os.mkdir('PATCHES_NP')

# Change to the paths of your annotated files
path_annotated_ODS2 = r'Annotated ODS2/'
path_annotated_ODS3 = r'Annotated ODS3/'

# Change to the path of your digital field
path_digital_field = r'S05TR2EDFT038.bmp'

basename = os.path.basename(path_digital_field)
print(basename)
folder_name = basename[0:9]
print(folder_name)
file_name = os.path.splitext(basename)[0]
print(file_name)

slide = int(file_name[1:3])

image_df = imread(path_digital_field)
plt.figure(f"{file_name}")
plt.imshow(image_df)
plt.axis('off')

try:
    if 1 <= slide <= 15:
        annotated_file = path_annotated_ODS2 + 'ANNOTATIONS/' + folder_name + '/ImageAnnotation/' + file_name + '.csv'
    else:
        annotated_file = path_annotated_ODS3 + 'ANNOTATIONS/' + folder_name + '/ImageAnnotation/' + file_name + '.csv'

    file_an = pd.read_csv(annotated_file, header=None)
    print(file_an)
    total = file_an.shape[0]
    print(total)

    if total == 0:
        print("Negative Digital Field")

        count = 1
        stride_i = 0
        for i in range(10):
            for j in range(10):
                stride_j = 0
                path_np = 'PATCHES_NP/'
                name_fileNP = f"{path_np}{file_name[0:6]}{file_name[9:14]}NP{count}.bmp"
                print(name_fileNP)

                patch = image_df[i * 40 + stride_i:40 + i * 40 + stride_i, j * 40 + stride_j:40 + j * 40 + stride_j]

                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    imsave(name_fileNP, img_as_ubyte(patch))

                count += 1
                stride_j += 10
            stride_i += 10
        print("The patches were saved in the PATCHES_NP/ directory")

    else:
        print("The digital field has bacilli.")

except FileNotFoundError as e:
    print("The CSV file does not exists")
    print("Negative Digital Field")

    count = 1
    stride_i = 0
    for i in range(10):
        for j in range(10):
            stride_j = 0
            path_np = 'PATCHES_NP/'
            name_fileNP = f"{path_np}{file_name[0:6]}{file_name[9:14]}NP{count}.bmp"
            print(name_fileNP)

            patch = image_df[i * 40 + stride_i:40 + i * 40 + stride_i, j * 40 + stride_j:40 + j * 40 + stride_j]

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                imsave(name_fileNP, img_as_ubyte(patch))

            count += 1
            stride_j += 10
        stride_i += 10
    print("The patches were saved in the PATCHES_NP/ directory")

plt.show()