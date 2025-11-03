# tbimages-data-processing
This repository contains examples of data processing in databases applied to the development of automated methods for diagnosing tuberculosis.

# Database request
The image databases used can be requested at https://tbimages.ufam.edu.br. First, users are asked to fill in and send a form to the owners, who authorize access by sending a download link. The use is restrict to academic research.

# Scripts
The ```src``` directory contains scripts for processing and visualize images of the databases as follows:
* extract_patchesNP.py - extracts 40x40 pixel patches from negative slides.
* extract_patchesPP.py - extracts 40x40 pixel patches with a bacillus, a cluster of bacilli, or an undefined object in the center, according to the annotations.
* mosaic_image.py - generate 400x400 pixel mosaic images with positive and negative patches. This script uses the DDS1 directory as an example.

# Usage
Install the required packages:
```
pip install -r requirements.txt
```
Data needed to run the scripts: 
* extract_patchesNP.py and extract_patchesPP.py: a slide of the ODS2 or ODS3 datasets, Annotated ODS2 and Annotated ODS3 
* mosaic_image.py: DDS1 dataset  

# Directory Structures
The following structures are expected in the scripts.

## Annotated ODS2
```
..\Annotated ODS2
|-- ANNOTATIONS
| |-- S01TR1EDF
| | |-- ImageAnnotation
| | | |-- S01TR1EDFT022.csv
| | | |-- ...
| |-- ...
| |-- S15TR1EDF
| |-- S15TR2EDF
|-- MARKS
| |-- S01TR1EDFM
| | |-- S01TR1EDFM001.bmp
| | |-- ...
| | |-- S01TR1EDFM164.bmp
| |-- ...
| |-- S15TR1EDFM
| |-- S15TR2EDFM
```

## Annotated ODS3
```
..\Annotated ODS3
|-- ANNOTATIONS
| |-- S16TR1EDF
| | |-- ImageAnnotation
| | | |-- S16TR1EDFT052.csv
| | | |-- ...
| |-- ...
| |-- S25TR1EDF
| |-- S25TR2EDF
| |-- MARKS
| | |-- S16TR1EDFM
| | | |-- S16TR1EDFM001.bmp
| | | |-- ...
| | | |-- S16TR1EDFM164.bmp
| | |-- ...
| | |-- S25TR1EDFM
| | |-- S25TR2EDFM
```

## DDS1
```
..\DDS1
|-- NP
| |-- IMAGE
| | |-- S01TR1T107NP1.bmp
| | |-- ...
| |-- MASK
|-- PP
| |-- IMAGE
| | |-- S01TR1T022PP1.bmp
| | |-- ...
| |-- MASK
```
