from PIL import Image
imgx=512 #width
imgy=512 #height

image=Image.new("RGB",(imgx,imgy)) #specifying color, width, height
# image.putpixel((0,0),(0,50,200)) #makes the top left pizel, that specific RGB value. location, rgb value
i=0
e=0
for i in range(0,imgx):
    for e in range(0,imgy):
        image.putpixel((i,e),(0,50,200))
        e=e+1
    i=i+1

image.save("demo_img2.png","PNG")#name, type of file
