# Roshni Surpur
# Octiber 25, 2018
# Ryan helped me figure out the HSV colorsys in class
# also i got help from https://www.atopon.org/mandel/#
# http://www.shodor.org/interactivate/activities/JuliaSets/ for finding ranges
# that was available on Octiber 23 2018




from PIL import Image
import math
import colorsys
# xa,xb=-0.1324,-0.0706
# ya,yb=0.9185,0.99026
# xa,xb=0.2293,0.2405
# ya,yb=0.5418,0.5533
xa,xb=-0.0858,-0.08455
ya,yb=0.8743,0.8755
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
        # r=0
        # g=(i**10)%256
        # b=i%256
        # image.putpixel((x,y),(r,g,b))
        h=math.exp(i)
        s=i%100%256
        v=i%500
        # h=(i%256)/34*i
        # s=i%50*i
        # v=i*5
        h=h/255
        s=s/100
        v=v/100
        # r=i%256
        # g=(i**10)%200
        # b=i%256
        r,g,b=colorsys.hsv_to_rgb(h, s, v)
        r=int(r*255)
        g=int(g*255)
        b=int(b*255)
        image.putpixel((x,y),(r,g,b))
image.show()
#---------------------------------------------------------------------------------
xa,xb=-0.0858,-0.08455
ya,yb=0.8743,0.8755
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
        # r=0
        # g=(i**10)%256
        # b=i%256
        # image.putpixel((x,y),(r,g,b))
        h=math.log(i)
        s=i%100%256
        v=i%500
        # h=(i%256)/34*i
        # s=i%50*i
        # v=i*5
        h=h/255
        s=s/100
        v=v/100
        # r=i%256
        # g=(i**10)%200
        # b=i%256
        r,g,b=colorsys.hsv_to_rgb(h, s, v)
        r=int(r*255)
        g=int(g*255)
        b=int(b*255)
        image.putpixel((x,y),(r,g,b))
image.show()
#---------------------------------------------------------------------------------

xa,xb=-0.09607,-0.07808
ya,yb=0.8602,0.87819
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
        # r=0
        # g=(i**10)%256
        # b=i%256
        # image.putpixel((x,y),(r,g,b))
        h=math.log(i)
        s=i%100%256
        v=i%500
        # h=(i%256)/34*i
        # s=i%50*i
        # v=i*5
        h=h/255
        s=s/100
        v=v/100
        # r=i%256
        # g=(i**10)%200
        # b=i%256
        r,g,b=colorsys.hsv_to_rgb(h, s, v)
        r=int(r*255)
        g=int(g*255)
        b=int(b*255)
        image.putpixel((x,y),(r,g,b))
image.show()
#---------------------------------------------------------------------------------

xa,xb=-0.09607,-0.07808
ya,yb=0.8602,0.87819
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
        # r=0
        # g=(i**10)%256
        # b=i%256
        # image.putpixel((x,y),(r,g,b))
        h=math.exp(i)
        s=i%100%256
        v=i%500
        # h=(i%256)/34*i
        # s=i%50*i
        # v=i*5
        h=h/255
        s=s/100
        v=v/100
        # r=i%256
        # g=(i**10)%200
        # b=i%256
        r,g,b=colorsys.hsv_to_rgb(h, s, v)
        r=int(r*255)
        g=int(g*255)
        b=int(b*255)
        image.putpixel((x,y),(r,g,b))
image.show()
#---------------------------------------------------------------------------------
xa,xb=-1.329783151414221,-1.1113089632498063
ya,yb=0.110768344075463565,0.239282572407472


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
        z=complex(cx,cy) #makes c a complex number, makes computations easier
        c=complex(-.8,0.156)
        # c=complex(-.35,-.65)
        # c=complex(.4,.225)
        # c=complex(.4,.0325)
        # c=complex(.4,.325)
        for i in range(maxIt):
            if abs(z)>=2:
                break
            z=z**2+c
        h=math.exp(i)
        s=i%100%256
        v=i%500
        # h=(i%256)/34*i
        # s=i%50*i
        # v=i*5
        h=h/255
        s=s/100
        v=v/100
        # r=i%256
        # g=(i**10)%200
        # b=i%256
        r,g,b=colorsys.hsv_to_rgb(h, s, v)
        r=int(r*255)
        g=int(g*255)
        b=int(b*255)
        image.putpixel((x,y),(r,g,b))
image.show()
#---------------------------------------------------------------------------------
xa,xb=-1.046840976540736,0.07785474738116704
ya,yb=-0.5138437621887803,0.14774195776528032

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
        z=complex(cx,cy) #makes c a complex number, makes computations easier
        c=complex(-.8,0.156)
        # c=complex(-.35,-.65)
        # c=complex(.4,.225)
        # c=complex(.4,.0325)
        # c=complex(.4,.325)
        for i in range(maxIt):
            if abs(z)>=2:
                break
            z=z**2+c
        h=math.exp(i)
        s=i%100%256
        v=i%500
        # h=(i%256)/34*i
        # s=i%50*i
        # v=i*5
        h=h/255
        s=s/100
        v=v/100
        # r=i%256
        # g=(i**10)%200
        # b=i%256
        r,g,b=colorsys.hsv_to_rgb(h, s, v)
        r=int(r*255)
        g=int(g*255)
        b=int(b*255)
        image.putpixel((x,y),(r,g,b))
image.show()
