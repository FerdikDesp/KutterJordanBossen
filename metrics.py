class Metrics:


    def maxD(image, encodedImage):
        
        r, g, b = 0, 0, 0

        imageMap = image.load()
        encodedImageMap = encodedImage.load()

        for col in range(image.size[1]):
            for row in range(image.size[0]):
                r = max(r, abs(imageMap[row, col][0] - encodedImageMap[row, col][0]))
                g = max(g, abs(imageMap[row, col][1] - encodedImageMap[row, col][1]))
                b = max(b, abs(imageMap[row, col][2] - encodedImageMap[row, col][2]))
        
        return (r, g, b)
    
    def nmse(image, encodedImage):

        r, g, b = 0, 0, 0

        imageMap = image.load()
        encodedImageMap = encodedImage.load()

        upperR, upperG, upperB = 0, 0, 0
        lowerR, lowerG, lowerB = 0, 0, 0

        for col in range(image.size[1]):
            for row in range(image.size[0]):
                upperR = upperR + (imageMap[row, col][0] - encodedImageMap[row, col][0])**2
                upperG = upperG + (imageMap[row, col][1] - encodedImageMap[row, col][1])**2
                upperB = upperB + (imageMap[row, col][2] - encodedImageMap[row, col][2])**2

                lowerR = lowerR + imageMap[row, col][0]**2
                lowerG = lowerG + imageMap[row, col][1]**2
                lowerB = lowerB + imageMap[row, col][2]**2
        
        r, g, b = upperR / lowerR, upperG / lowerG, upperB / lowerB

        return (r, g, b)
    
    def snr(image, encodedImage):

        r, g, b = 0, 0, 0

        imageMap = image.load()
        encodedImageMap = encodedImage.load()

        upperR, upperG, upperB = 0, 0, 0
        lowerR, lowerG, lowerB = 0, 0, 0

        for col in range(image.size[1]):
            for row in range(image.size[0]):
                lowerR = lowerR + (imageMap[row, col][0] - encodedImageMap[row, col][0])**2
                lowerG = lowerG + (imageMap[row, col][1] - encodedImageMap[row, col][1])**2
                lowerB = lowerB + (imageMap[row, col][2] - encodedImageMap[row, col][2])**2

                upperR = upperR + imageMap[row, col][0]**2
                upperG = upperG + imageMap[row, col][1]**2
                upperB = upperB + imageMap[row, col][2]**2
        
        r, g, b = upperR / lowerR, upperG / lowerG, upperB / lowerB

        return (r, g, b)
    
    def psnr(image, encodedImage):

        r, g, b = 0, 0, 0

        imageMap = image.load()
        encodedImageMap = encodedImage.load()

        upperR, upperG, upperB = 0, 0, 0
        lowerR, lowerG, lowerB = 0, 0, 0

        for col in range(image.size[1]):
            for row in range(image.size[0]):
                upperR = max(upperR, imageMap[row, col][0]**2)
                upperG = max(upperG, imageMap[row, col][1]**2)
                upperB = max(upperB, imageMap[row, col][2]**2)

                lowerR = lowerR + (imageMap[row, col][0] - encodedImageMap[row, col][0])**2
                lowerG = lowerG + (imageMap[row, col][1] - encodedImageMap[row, col][1])**2
                lowerB = lowerB + (imageMap[row, col][2] - encodedImageMap[row, col][2])**2
        
        r, g, b = image.size[0] * image.size[1] * upperR / lowerR, image.size[0] * image.size[1] * upperG / lowerG, image.size[0] * image.size[1] * upperB / lowerB
        
        return (r, g, b)
    
    def uqi(image, encodedImage):

        r, g, b = 0, 0, 0

        imageMap = image.load()
        encodedImageMap = encodedImage.load()

        upperR, upperG, upperB = 0, 0, 0

        for col in range(image.size[1]):
            for row in range(image.size[0]):
                upperR += imageMap[row, col][0]
                upperG += imageMap[row, col][1]
                upperB += imageMap[row, col][2]
        
        avgR, avgG, avgB = upperR / (image.size[0] * image.size[1]), upperG / (image.size[0] * image.size[1]), upperB / (image.size[0] * image.size[1])

        upperR, upperG, upperB = 0, 0, 0

        for col in range(image.size[1]):
            for row in range(image.size[0]):
                upperR += encodedImageMap[row, col][0]
                upperG += encodedImageMap[row, col][1]
                upperB += encodedImageMap[row, col][2]
        
        avgnewR, avgnewG, avgnewB = upperR / (image.size[0] * image.size[1]), upperG / (image.size[0] * image.size[1]), upperB / (image.size[0] * image.size[1])

        upperR, upperG, upperB = 0, 0, 0

        for col in range(image.size[1]):
            for row in range(image.size[0]):
                upperR += (imageMap[row, col][0] - avgR)**2
                upperG += (imageMap[row, col][1] - avgG)**2
                upperB += (imageMap[row, col][2] - avgB)**2
        
        dispR, dispG, dispB = upperR / (image.size[0] * image.size[1]), upperG / (image.size[0] * image.size[1]), upperB / (image.size[0] * image.size[1])

        upperR, upperG, upperB = 0, 0, 0

        for col in range(image.size[1]):
            for row in range(image.size[0]):
                upperR += (encodedImageMap[row, col][0] - avgR)**2
                upperG += (encodedImageMap[row, col][1] - avgG)**2
                upperB += (encodedImageMap[row, col][2] - avgB)**2
        
        dispnewR, dispnewG, dispnewB = upperR / (image.size[0] * image.size[1]), upperG / (image.size[0] * image.size[1]), upperB / (image.size[0] * image.size[1])        

        upperR, upperG, upperB = 0, 0, 0

        for col in range(image.size[1]):
            for row in range(image.size[0]):
                upperR += ((imageMap[row, col][0] - avgR)*(encodedImageMap[row, col][0] - avgnewR))
                upperG += ((imageMap[row, col][1] - avgG)*(encodedImageMap[row, col][1] - avgnewG))
                upperB += ((imageMap[row, col][2] - avgB)*(encodedImageMap[row, col][2] - avgnewB))
        
        corfuncR, corfuncG, corfuncB = upperR / (image.size[0] * image.size[1]), upperG / (image.size[0] * image.size[1]), upperB / (image.size[0] * image.size[1])        

        upperR, upperG, upperB = 0, 0, 0
        lowerR, lowerG, lowerB = 0, 0, 0

        for col in range(image.size[1]):
            for row in range(image.size[0]):
                upperR += 4*corfuncR*avgR*avgnewR
                upperG += 4*corfuncG*avgG*avgnewG
                upperB += 4*corfuncB*avgB*avgnewB

                lowerR += ((dispR**2 + dispnewR**2)*(avgR**2 + avgnewR**2))
                lowerG += ((dispG**2 + dispnewG**2)*(avgG**2 + avgnewG**2))
                lowerB += ((dispB**2 + dispnewB**2)*(avgB**2 + avgnewB**2))
        
        r, g, b = upperR / lowerR, upperG / lowerG, upperB / lowerB

        return (r, g, b)