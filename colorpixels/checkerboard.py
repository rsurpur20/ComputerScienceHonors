from PIL import Image
import random
imgx=512 #width
imgy=512 #height

image=Image.new("RGB",(imgx,imgy)) #specifying color, width, height
# image.putpixel((0,0),(0,50,200)) #makes the top left pizel, that specific RGB value. location, rgb value
i=0
e=0
# for i in range(0,imgx):
#     for e in range(0,imgy):
#         image.putpixel((i,e),(0,0,0))
#         e=e+1
#     i=i+1

# stripes:
numrows=6
width=int(imgx/numrows)
height=int(imgy/numrows)
t=0
x=0
y=0
while x<imgx:
    for y in range(0,imgy):
        # for t in range(0, imgx):
        # for x in range(0, imgx*numrows):
        if y%100 < 50 and x%100 < 50 :
            r = 255
        elif y%100 > 50 and x%100 > 50:
            r = 255
        else:
            r = 0
        # if (x%100 < 50) :
        #     r = 255
        # else:
        #     r = 0
        image.putpixel((x,y),(r,0,0))
        y=y+1
    x=x+1
# while y<imgy:
#     for x in range(0,imgx):
#         # for t in range(0, imgx):
#         # for x in range(0, imgx*numrows):
#         image.putpixel((x,y),(255,0,0))
#         x=x+1
#     y=y+height

        # x=x+50

        # t=50+width
# #
# for z in range(numrows+1):
#
#     width=int(imgx/numrows)
#     height=int(imgy/numrows)
#     for d in range(width):
#         for f in range(height):
#             image.putpixel((f,d),(255,0,0))
#         d=d+1
#         f=f+1
#     z=z+1


    # image.putpixel((f*z,d*z),(255,0,0))
# randx=random.randint(0,imgx)
# randy=random.randint(0,imgy)
# randcolor=random.randint(0,255)
# for a in range(imgy):
#     for b in range(randx,randx+10):
#         image.putpixel((i,e),(randcolor, randcolor,randcolor))
image.save("checker.png","PNG")#name, type of file
