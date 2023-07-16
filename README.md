# PDFiy
 PDFiy is a tool that helps you convert multiple images into a single pdf file

# Implementation
Follow the below mentioned steps to setup the project in your local machine

## Step 1
Clone this repository into your machine
```
git clone https://github.com/abhiramelf/pdfiy.git
```

## Step 2
There are two major dependencies for this project. Make sure to install these dependencies before you run the project
### Easygui
```
pip install easygui
```
### FPDF
Do not use pip to install this dependency! Please use the code from their repository
```
git clone https://github.com/reingart/pyfpdf.git
cd pyfpdf
python setup.py install
```