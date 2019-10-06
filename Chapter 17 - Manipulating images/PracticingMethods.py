from PIL import Image

'''
this file contains several basic practices to understand the functionality of the pillow library
'''

# just loading the which will be working
catImage = Image.open('zophie.png')

# ******************************************************
# Cropping
# ******************************************************
croppedImage = catImage.crop((335, 345, 565, 560))
croppedImage.save('cropped.png')

# ******************************************************
# Copying and Pasting images
# ******************************************************
catCopyImage = catImage.copy()
faceImage = catImage.crop((335, 345, 565, 560))
print(faceImage.size)
catCopyImage.paste(faceImage, (0,0))
catCopyImage.paste(faceImage, (400, 500))
catCopyImage.save('pasted.png')

# ******************************************************
# creating a mosaic or tiling the cat image with little face
# I'm copying object variables declared before, can avoid it, yes but it just to enhance reading and don't scroll above
# ******************************************************
catImageWidth, catImageHeight = catImage.size
faceImage = catImage.crop((335, 345, 565, 560))
faceImWidth, faceImHeight = faceImage.size
catCopyTwo = catImage.copy()

for left in range(0, catImageWidth, faceImHeight):
    for top in range(0, catImageHeight, faceImWidth):
        print("left: {}, top: {} ".format(left, top))
        catCopyTwo.paste(faceImage, (left, top))

catCopyTwo.save('Tiled.png')

# ******************************************************
# Resizing image
# ******************************************************
width, height = catImage.size
quartersizedIm = catImage.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('quartersized.png')
svelteIm = catImage.resize((width, height + 300))
svelteIm.save('svelte.png')

# ******************************************************
# Rotating and Flipping Images
# ******************************************************

catImage.rotate(90).save('rotated90.png')
catImage.rotate(180).save('rotated180.png')
catImage.rotate(270).save('rotated270.png')

# The rotate() method has an optional expand keyword argument that can be set to True to enlarge the dimensions of the image to fit the entire rotated new image
catImage.rotate(6).save('rotated6.png')
catImage.rotate(6, expand=True).save('rotated6_expanded.png')

# Transpose method

catImage.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catImage.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

# Changing Individual Pixels

im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))
for x in range(100):
     for y in range(50):
         im.putpixel((x, y), (210, 210, 210))

from PIL import ImageColor
for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
print(im.getpixel((0, 0)))
print(im.getpixel((0, 50)))
im.save('putPixel.png')