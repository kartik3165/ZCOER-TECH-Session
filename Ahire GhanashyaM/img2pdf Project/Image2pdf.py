# package image2pdf
# modules pillow 
import img2pdf
from PIL import Image
import os
img_path = input("Enter the Path of Image here : ")
# img_path = r"C:\Users\mukun\OneDrive\Desktop\Django Course\Projects\img2pdf Project\design.png.jpeg"
pdf_path = r"C:\Users\mukun\OneDrive\Desktop\Django Course\Projects\img2pdf Project\file.pdf"
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(img_path)
file = open(pdf_path,"wb")
file.write(pdf_bytes)
image.close()
file.close()
print("Successfully made pdf file")
print(pdf_path)
