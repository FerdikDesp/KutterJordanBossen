from seed import Seed
from textEditor import TextEditor

class ImageEditor:

    def encode(image, text, seed):

        binarytext = TextEditor.toBinary(text)
        pixels = Seed.generate(text, seed)

        