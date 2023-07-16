import sys
from easygui import *
from pyfpdf.fpdf import FPDF
from PIL import Image

# Initialize FPDF - for Py3 please use FPDF in this direcctory
pdf = FPDF(unit='mm')
pdf.set_auto_page_break(0)

# Select images for conversion using easygui from computer
def SelectImage():
    msg = "Please select Images to convert to PDF!\nOr Press <cancel> to exit."
    title = "PDFiy"
    choices = ["Select Images", "Exit"]
    reply = buttonbox(msg, title=title, choices=choices)

    if reply == "Exit":
        sys.exit(0)

    if reply == "Select Images":
        inputPath = fileopenbox(title="Select Images", default="*.png",
                                filetypes=["*.jpg", "*.jpeg", "*.png", "*"], multiple=True)

        StartConversion(inputPath)

# Begin conversion of images into a single PDF
def StartConversion(inputPath):
    msg = "Let the magic begin!\nOr Press <cancel> to exit."
    title = "PDFiy"
    choices = ["Convert & Save", "Exit"]
    reply = buttonbox(msg, title=title, choices=choices)

    if reply == "Exit":
        sys.exit(0)

    if reply == "Convert & Save":

        savePath = filesavebox(title="Save PDF", default="Output.pdf")

        try:
            for img in inputPath:
                if img.split(".")[-1] in ("png", "jpg", "jpeg"):
                    cover = Image.open(img)
                    width, height = cover.size
                    print(width, height)
                    width, height = float(
                        width * 0.264583), float(height * 0.264583)
                    pdf.add_page(format=(width, height))
                    pdf.image(img, 0, 0, width, height)
            pdf.output(savePath)
            print("Conversion complete!")

            NewConversion(
                "Conversion Complete! Enjoy!\nOr Press <cancel> to exit.")
        except:
            NewConversion(
                f'An exception occurred: {pdf.error(msg="Error while conversion!")}\nOr Press < cancel > to exit.')

# Start new conversion flow based on success or failure
def NewConversion(message):
    msg = message
    title = "PDFiy"
    choices = ["Convert Another"]
    reply = buttonbox(msg, title=title, choices=choices)

    if reply == "Convert Another":
        SelectImage()

def main():
    # Start the application with a Welcome message!
    ret_val = msgbox("Welcome to PDFiy!")
    if ret_val is None:  # User closed msgbox
        sys.exit(0)
    else:
        SelectImage()

main()