from PIL import Image

testImage = "/Users/anshramanath/desktop/adventureofalifetime.jpg"
asciiChars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resizeImage(image, newWidth = 100):
    width, height = image.size
    ratio = height/width
    
    newHeight = int(newWidth * ratio)

    newImage = image.resize((newWidth, newHeight))
    return newImage

def makeGray(image):
    grayImage = image.convert("L")
    return grayImage

def makeAscii(image):
    pixels = image.getdata()
    characters = "".join([asciiChars[pixel//25] for pixel in pixels])
    return characters

def main(newWidth = 100):
    newImageData = makeAscii(makeGray(resizeImage(Image.open(testImage))))

    pixelCount = len(newImageData)  
    asciiImage = "\n".join([newImageData[index:(index + newWidth)] for index in range(0, pixelCount, newWidth)])
    
    with open("aoalt.txt", "w") as f:
        f.write(asciiImage)

main()