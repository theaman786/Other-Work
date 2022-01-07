loop = True
def estimateTextFileSize(bits,characters):
    textFileSize = bits * characters
    return textFileSize
def estimatePictureFileSize(Width,Height,colourDepth):
    pictureFileSize = colourDepth*Width*Height
    return pictureFileSize
def estimateSoundFileSize(sampleRate,duration,bitDepth,channels):
    soundFileSize = sampleRate*duration*bitDepth*channels
    return soundFileSize
loop = True
while loop == True:
    try:
        fileType = int(input("Enter 0 for Text File, 1 for Picture File,"
                     "2 for Sound File: "))
    except:
        print("Invalid input, please enter a number.")
    if fileType < 0 or fileType > 2:
        print("Please enter a number between 0 and 3.")
    else:
        loop = False
if fileType == 0:
    loop = True
    while loop == True:
        try:
            bits = int(input("Enter the number of bits per character: "))
            characters = int(input("Enter the number of characters: "))
        except:
            print("Invalid input, please enter a number.")
        if fileType < 0:
            print("Please enter a number above 0 ")
        else:
            loop = False
    textFileSize = estimateTextFileSize(bits,characters)
    print("The Text File Size is" ,textFileSize)
elif fileType == 1:
    loop = True
    while loop == True:
        try:
            Width = int(input("Enter the width of the picture: "))
            Height = int(input("Enter the height of the picture: "))
            colourDepth = int(input("Enter the colour depth of the picture: "))
        except:
            print("Invalid input, please enter a number.")
        if fileType < 0:
            print("Enter a number above 0.")
        else:
            loop = False
    pictureFileSize = estimatePictureFileSize(Width,Height,colourDepth)
    print("The Picture File Size is",pictureFileSize)
elif fileType == 2:
    loop = True
    while loop == True:
        try:
            sampleRate = int(input("Enter the Sample rate of the sound: "))
            duration = int(input("Enter the duration of the sound in seconds: "))
            bitDepth = int(input("Enter the bit depth of the sound: "))
            channels = int(input("Enter the number of channels of the sound: "))
        except:
            print("Invalid input, please enter a number.")
        if fileType < 0:
            print("Enter numbers above 0.")
        else:
            loop = False
    soundFileSize = estimateSoundFileSize(sampleRate,duration,bitDepth,channels)
    print("The Sound File Size is" ,soundFileSize)
