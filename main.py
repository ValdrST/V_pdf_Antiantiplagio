from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

if __name__ == "__main__":
    images = convert_from_path('./pdfs/in.pdf')
    images[0].save("out.pdf", save_all=True, append_images=images[1:])