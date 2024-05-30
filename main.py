from PIL import Image
from imageEditor import ImageEditor
from textEditor import TextEditor


#Объявление переменных
sigma = 3
lyambda = 0.3
text = "This is awesome text!"

image = Image.open("nature_old.jpg")

encodedImage, pixels = ImageEditor.encode(image, text, lyambda)

encodedImage = Image.open("encoded.png")

binarytext = ImageEditor.decode(encodedImage, pixels, sigma)

print(TextEditor.toBinary(text), text)
print(binarytext, TextEditor.toString(binarytext))