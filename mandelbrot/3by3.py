from PIL import Image
imgx=512
imgy=512
y=0
image=Image.new("RGB",(imgx,imgy)) #specifying color, width, height
while y<imgy:
    for x in range(0,imgx):

        image.putpixel((x,y),(255,0,0))
        x=x+1
image.save("3by3.png","PNG")#name, type of file
