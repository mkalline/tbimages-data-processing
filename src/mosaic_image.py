import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from skimage.io import imread

# Change to the path of yours DDS1 directory
path_DDS1 = r'DDS1/'

path_NP = path_DDS1 + 'NP/IMAGE/'
list_NP = os.listdir(path_NP)
path_NP_BIN = path_DDS1 + 'NP/MASK/'
list_NP_BIN = os.listdir(path_NP_BIN)

path_PP = path_DDS1 + 'PP/IMAGE/'
list_PP = os.listdir(path_PP)
path_PP_BIN = path_DDS1 + 'PP/MASK/'
list_PP_BIN = os.listdir(path_PP_BIN)

if not os.path.exists('MOSAIC_IMAGE'):
    os.mkdir('MOSAIC_IMAGE')
    os.mkdir('MOSAIC_IMAGE/IMAGE')
    os.mkdir('MOSAIC_IMAGE/MASK')
    os.mkdir('MOSAIC_IMAGE/PATCHES')

n = 1
msc = int(len(os.listdir('MOSAIC_IMAGE/IMAGE')))

img_mosaic = []
img_mosaic_bin = []
img_mosaic_names = []

while n <= 100:
    x = np.random.rand()

    if x < 0.5:
        y = np.random.randint(len(list_NP))
        img_path = os.path.join(path_NP, list_NP[y])
        mask_path = os.path.join(path_NP_BIN, list_NP[y])
    else:
        y = np.random.randint(len(list_PP))
        img_path = os.path.join(path_PP, list_PP[y])
        mask_path = os.path.join(path_PP_BIN, list_PP[y])

    img_mosaic.append(Image.open(img_path))
    img_mosaic_bin.append(Image.open(mask_path))
    img_mosaic_names.append(os.path.basename(img_path))

    n += 1

thumb_size = (40, 40)
cols, rows = 10, 10

thumbs = [im.resize(thumb_size) for im in img_mosaic]
w, h = thumb_size
mosaic = Image.new('RGB', (cols * w, rows * h))

for i, im in enumerate(thumbs):
    x = (i % cols) * w
    y = (i // cols) * h
    mosaic.paste(im, (x, y))

thumbs = [im.resize(thumb_size) for im in img_mosaic_bin]
w, h = thumb_size
mosaic_bin = Image.new('L', (cols * w, rows * h))

for i, im in enumerate(thumbs):
    x = (i % cols) * w
    y = (i // cols) * h
    mosaic_bin.paste(im, (x, y))

filename = f"MOSAIC_IMAGE/IMAGE/MSC{msc}.bmp"
mosaic.save(filename, format="BMP")

filename = f"MOSAIC_IMAGE/MASK/MSC{msc}.bmp"
mosaic_bin.save(filename, format="BMP")

filename = f"MOSAIC_IMAGE/PATCHES/MSC{msc}.txt"
with open(filename, 'w') as f:
    f.write('\n'.join(img_mosaic_names))

print("The Mosaic Image was saved in the MOSAIC_IMAGE/ directory")


# Show the mosaic image saved
img_rgb = imread(f"MOSAIC_IMAGE/IMAGE/MSC{msc}.bmp")
mask = imread(f"MOSAIC_IMAGE/MASK/MSC{msc}.bmp")

if mask.ndim == 3:
    mask = color.rgb2gray(mask)

mask = (mask > 0.5).astype(float)   # values 0 or 1

overlay = img_rgb.copy().astype(float) / 255.0
overlay[mask == 1] = [1, 0, 0]

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title('RGB')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title('Mask')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(overlay)
plt.title('Overlay')
plt.axis('off')

plt.tight_layout()
plt.show()


