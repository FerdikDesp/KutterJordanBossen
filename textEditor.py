class TextEditor:

    def toBinary(text):
        binarytext = ""
        for symbol in text:
            binarytext = binarytext + format(ord(text), "08b")
        binarytext += "00000000"
        return binarytext

    def toString(binarytext):
        text = ""
        for byte in range(0, len(text) - 8, 8):
            text = text + chr(int(text[byte:byte+8], 2))
        return text