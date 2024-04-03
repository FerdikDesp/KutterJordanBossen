from PIL import Image
from imageEditor import ImageEditor
from textEditor import TextEditor
from metrics import Metrics
from plot import Plot
import numpy as np

#Объявление переменных
sigma = 3
lyambda = 1.5
text = "This is awesome text!"
imageSRC = "nature.jpg"
encodedImageSRC = "encoded.png"

image = Image.open(imageSRC)

encodedImage, pixels = ImageEditor.encode(image, text, lyambda)

encodedImage = Image.open(encodedImageSRC)

binarytext = ImageEditor.decode(encodedImage, pixels, sigma)

print(TextEditor.toBinary(text), text)
print(binarytext, TextEditor.toString(binarytext))

image, encodedImage = Image.open(imageSRC), Image.open(encodedImageSRC)

print("Максимальное абсолютное отклонение:", Metrics.maxD(image, encodedImage))
print("Нормированное среднее квадратичное отклонение:", Metrics.nmse(image, encodedImage))
print("Универсальный индекс качества:", Metrics.uqi(image, encodedImage))

lyambdaFirst = 0.1
lyambdaLast = 1.5
n = (lyambdaLast - lyambdaFirst) // 0.1

lambdas = np.linspace(lyambdaFirst, lyambdaLast, int(n))
errPrb = Plot.errorProbabilities(lambdas, sigma, text, imageSRC, encodedImageSRC)
Plot.plot(lambdas, errPrb)