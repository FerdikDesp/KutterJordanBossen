import random
from textEditor import TextEditor


class ImageEditor:

    def encode(image, text, lyambda):

        binarytext = TextEditor.toBinary(text)
        pixelMap = image.load()
        pixels = []
        for i in range(0, len(binarytext)):
            pixels.append((random.randint(10, image.size[0] - 11), random.randint(10, image.size[1] - 11)))
        
        for i in range(0, len(binarytext)):
            symbol = binarytext[i]
            x, y = pixels[i]
            if (symbol == "0"):
                summary = pixelMap[x, y][2] + lyambda * (0.299 * pixelMap[x, y][0] +  0.587 * pixelMap[x, y][1] + 0.114 * pixelMap[x, y][2])
                if (summary > 255):
                    summary = 255
            elif (symbol == "1"):
                summary = pixelMap[x, y][2] - lyambda * (0.299 * pixelMap[x, y][0] +  0.587 * pixelMap[x, y][1] + 0.114 * pixelMap[x, y][2])
                if (summary < 0):
                    summary = 0
            pixelMap[x, y] = (pixelMap[x, y][0], pixelMap[x, y][1], int(summary))
        return image.save("encoded.png"), pixels
    
    def decode(image, pixels, sigma):

        binarytext = ""
        pixelMap = image.load()

        for x, y in pixels:
            bluePixel = pixelMap[x, y][2]
            summary = 0
            for i in range(1, sigma + 1):
                summary += pixelMap[x + i, y][2]
                summary += pixelMap[x - i, y][2]
                summary += pixelMap[x, y + i][2]
                summary += pixelMap[x, y - i][2]
            summary /= (sigma * 4)
            if (summary > bluePixel):
                binarytext += "1"
            else:
                binarytext += "0"
        
        return binarytext