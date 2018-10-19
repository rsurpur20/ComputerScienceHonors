from PIL import Image

xa,xb=-0.1324,-0.0706
ya,yb=0.9185,0.99026
# xa,xb=0.2293,0.2405
# ya,yb=0.5418,0.5533
# xa,xb=-0.0858,-0.08455
# ya,yb=0.8743,0.8755
# xa,xb=-0.09607,-0.07808
# ya,yb=0.8602,0.87819


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
        g=(i**10)%256
        b=i%256
        image.putpixel((x,y),(r,g,b))
image.show()
