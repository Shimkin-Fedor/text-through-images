from PIL import Image
path = input("Enter the path to the image: \n")
im = Image.open(path)
px = im.load()
diff = 0
color = r, g, b = 0, 0, 0
#g - код ASCII; r * b - расстояние до следующего значимого пикселя
x, y = 0, 0
s = ""

while x <= im.size[0]:
    (r, g, b) = im.getpixel((x, y))
    diff = r*b//2 + 283
    if g == 0:
        break
    
    s += chr(g)

    y += diff % im.size[1]
    x += diff // im.size[1]
    if y >= im.size[1]:
        y -= im.size[1]
        x += 1
print("Decoded message: ")
print(s)
