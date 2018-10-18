from PIL import Image
import math
imgx=3
imgy=3
num=2 #the number it should not exceed
iterations=3
pixels=[]
image=Image.new("RGB",(imgx,imgy)) #specifying color, width, height
for i in range(iterations):
    for x in range(imgx):
        for y in range(imgy):

            z=(0,0)
            c=(x,y)
            znew=c+z
            checkz=int(math.fabs(math.sqrt(x^2+y^2)))

            secondz=(0,checkz)
            secondcheckz=math.fabs(math.sqrt(0+checkz^2))
            if checkz>=num:
                print("Escaped")
                image.putpixel((x,y),(255,0,0)) #if escaped make pixel red
            elif secondcheckz>=num:
                print("Escaped on 2nd try")
                image.putpixel((x,y),(0,255,0)) #if escaped make pixel red
            else:
                print("did not escape")
                image.putpixel((x,y),(0,0,255)) #if escaped make pixel red
    i=i+1
image.save("mandelbrot.png","PNG")#name, type of file
