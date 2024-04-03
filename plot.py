class Plot:

    def errorProbabilities(lambdas, sigma, encodedText, imageSRC, encodedImageSRC):
        from imageEditor import ImageEditor
        from textEditor import TextEditor
        from PIL import Image

        lst = []

        for lyambda in lambdas:
            print(lyambda)
            image = Image.open(imageSRC)
            encodedImage, pixels = ImageEditor.encode(image, encodedText, lyambda)
            encodedImage = Image.open(encodedImageSRC)
            decodedText = ImageEditor.decode(encodedImage, pixels, sigma)
            encodedText = TextEditor.toBinary(encodedText)

            errors = 0
            for i in range(len(encodedText)):
                if encodedText[i] != decodedText[i]:
                    errors += 1
            
            errors /= len(encodedText)

            lst.append(errors)

        return lst    

    def plot(lambdas, errorProbabilities):
        import matplotlib.pyplot as plt

        plt.plot(lambdas, errorProbabilities) 
        
        plt.title("Dependence of error probabilities on the energy of the embedded channel") 

        plt.ylabel("Error probabilities") 
        plt.xlabel("Lambdas") 
        plt.show()