from turtle import *
color('magenta')
while True:
    left(200)
    forward(300)
    if abs(pos()) < 1:
        break
