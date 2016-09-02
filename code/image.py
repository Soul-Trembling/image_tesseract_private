
import pytesseract
import Image
image = Image.open('6m44nn.jpg')
print pytesseract.image_to_string(image)
