from PIL import Image
path = input("Enter the path to the image: \n")
s = input("Enter your message: \n")
im = Image.open(path)
px = im.load()
diff = 0
r = 0
g = 0
b = 0
#g - код ASCII; r * b - расстояние до следующего значимого пикселя
x = 0
y = 0

i = 0

while i < len(s) and x <= im.size[0]:
    (r, g, b) = im.getpixel((x, y))
    g = ord(s[i])
    
    diff = r*b//2 + 283
    px[x, y] = (r, g, b)
    
    y += diff % im.size[1]
    x += diff // im.size[1]
    if y > im.size[1]:
        y -= im.size[1]
        x += 1
    i += 1

if x <= im.size[0]:
    (r, g, b) = im.getpixel((x, y))
    px[x, y] = (r, 0, b)

im.save(path)
print("Message successfully encoded!")
