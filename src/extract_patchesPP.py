import pandas as pd
import numpy as np
from skimage import img_as_ubyte
from skimage.io import imread, imsave
import matplotlib.pyplot as plt
import os

if not os.path.exists('PATCHES_PP'):
    os.mkdir('PATCHES_PP')
    os.mkdir('PATCHES_PP/BACILLUS')
    os.mkdir('PATCHES_PP/CLUSTER')
    os.mkdir('PATCHES_PP/UNDEFINED')

# Change to the paths of your annotated files
path_annotated_ODS2 = r'Annotated ODS2/'
path_annotated_ODS3 = r'Annotated ODS3/'

# Change to the path of your digital field
path_digital_field = r'S18TR1EDFT109.bmp'

basename = os.path.basename(path_digital_field)
print(basename)
folder_name = basename[0:9]
print(folder_name)
file_name = os.path.splitext(basename)[0]
print(file_name)

slide = int(file_name[1:3])
exists = False

try:
    if 1 <= slide <= 15:
        annotated_file = path_annotated_ODS2 + 'ANNOTATIONS/' + folder_name + '/ImageAnnotation/' + file_name + '.csv'
        mark_file = path_annotated_ODS2 + 'MARKS/' + folder_name + 'M/' + folder_name + 'M' + file_name[10:] + '.bmp'
        exists = True
    else:
        annotated_file = path_annotated_ODS3 + 'ANNOTATIONS/' + folder_name + '/ImageAnnotation/' + file_name + '.csv'
        mark_file = path_annotated_ODS3 + 'MARKS/' + folder_name + 'M/' + folder_name + 'M' + file_name[10:] + '.bmp'
        exists = True

    file_an = pd.read_csv(annotated_file, header=None)
    print(file_an)

except FileNotFoundError as e:
    exists = False
    print("The CSV file does not exists")
    print("Negative Digital Field")

# Read image
image_df = imread(path_digital_field)
plt.figure(f"ORIGINAL IMAGE - {file_name}")
plt.imshow(image_df)
plt.axis('off')

# Read marked image
image_mark = imread(mark_file)
plt.figure(f"MARKED IMAGE - {file_name}")
plt.imshow(image_mark)
plt.axis('off')

patch_size = 40
half = patch_size // 2

image_padded = np.pad(image_df, ((half, half), (half, half), (0, 0)), mode='constant', constant_values=255)

if exists:
    for index, row in file_an.iterrows():
        type_bacillus = row[0]
        x = int(row[1]) + half
        y = int(row[2]) + half

        patch = image_padded[y-half:y+half, x-half:x+half]

        if type_bacillus == 'b':
            path_pp = 'PATCHES_PP/BACILLUS/'
        elif type_bacillus == 'bc':
            path_pp = 'PATCHES_PP/CLUSTER/'
        else:
            path_pp = 'PATCHES_PP/UNDEFINED/'

        name_filePP = f"{path_pp}{file_name[0:6]}{file_name[9:14]}PP{index}.bmp"
        imsave(name_filePP, img_as_ubyte(patch))

    print("The patches were saved in the PATCHES_PP/ directory")

plt.show()