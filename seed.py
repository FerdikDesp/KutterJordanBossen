class Seed:


    def generate(text, seed):
        pixels = []
        countOfBits = (len(text) + 1) * 8
        countOfPixels = countOfBits // 3 if countOfBits % 3 == 0 else (countOfBits // 3) + 1

        startPixel = seed
        for i in range(countOfPixels):
            pixels.append(startPixel)
            startPixel += 1
        
        return pixels

    def getnext(x):
        return x + 5