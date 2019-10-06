from PIL import Image

catItm = Image.open('zophie.png')
print(catItm.size)

width, height = catItm.size
print(width)
print(height)
print(catItm.filename)
print(catItm.format)
print(catItm.format_description)