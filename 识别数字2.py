from PIL import Image
import pytesseract

Img = Image.open('95.png')

Img = Img.convert('RGB')

print(pytesseract.image_to_string(Img))