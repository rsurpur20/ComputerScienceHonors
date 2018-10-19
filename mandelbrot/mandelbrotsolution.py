from PIL import Image

xa,xb=-2.0,2.0
ya,yb=-2.0,2.0

imgx=512
imgy=512
maxIt=256 #max amount of iterations
image=Image.new("RGB",(imgx,imgy)) #specifying color, width, height
for y in range(imgy):
    # will calculate c value:
    cy= y*(yb-ya)/(imgy-1)+ya
    for x in range(imgx):
        # will calculate c value:
        cx= x*(xb-xa)/(imgx-1)+xa
        c=complex(cx,cy) #makes c a complex number, makes computations easier
        z=0
        for i in range(maxIt):
            if abs(z)>=2:
                break
            z=z**2+c
        r=0
        g=(i**20)%256
        b=i
        image.putpixel((x,y),(r,g,b))
image.show()
