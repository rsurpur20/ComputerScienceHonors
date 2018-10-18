import random
from PIL import Image

def draw_snake():
	y = 0#start at top
	x = random.randrange(512)
    #random colors:
	r = random.randrange(256)
	g = random.randrange(256)
	b = random.randrange(256)

	while True:
		if x < 0 or x >= imgx or y >= imgy:  #if off the board
			break

		image.putpixel((x,y),(r,g,b))

		rr = random.random();
        # changing these values will make the picture diagonal
		if rr < .2:
			x+=1#right
		elif rr < .4:
			x-=1#left
		else:
			y+=1;

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx, imgy))

for i in range(100):
	draw_snake()

image.save("snakes_image.png", "PNG")


# from PIL import Image
# import random
# imgx=512 #width
# imgy=512 #height
# image=Image.new("RGB",(imgx,imgy)) #specifying color, width, height
#
#
# x=random.randint(0,imgx)
# # draw a vertical line
# randcolor=random.randint(0,255)
# a=random.randrange(-1,2)
# while x+a<imgx:
#     for y in range(0,imgy):
#
#         image.putpixel((x+a,y),(randcolor,0,0))
#         y=y+1
#
#
# image.save("strings.png","PNG")#name, type of file
