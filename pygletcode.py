# Roshni and Ryan
# On my Honor
# Jan 30, 2019
# Resources:
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/py-modindex.html
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/
# https://stackoverflow.com/questions/35044298/difference-between-pyglet-and-pygame-in-simple-words/35044344#35044344

import pyglet
from pyglet.window import key
from pyglet.window import mouse


# The Window Module
# ------------------------------------------------------------------------------------------------
window = pyglet.window.Window(500, 500) #x, y
#the .window.Window function displays a window on the user’s screen with the x, and y parameters given

# Basics of Importing Text
# ------------------------------------------------------------------------------------------------

label = pyglet.text.Label('The Pyglet Library',
                          font_name='Calibra',
                          font_size=36,
                          x=250, y=window.height-50,
                          anchor_x='center', anchor_y='center')

#you can adjust aspects of the text such as font, font size, width and height of the text, and the location of the text on the screen. as far as the syntax,
# each attribute is just separated by a comma
# more character styles can be found here:https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/text.html


# Basics of Keyboard Events
# ------------------------------------------------------------------------------------------------

@window.event
def on_key_press(symbol, modifiers): #built in function - when key is pressed:
    print('A key was pressed')


# More Specific Exampls of Keyboard Events
# ------------------------------------------------------------------------------------------------

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')


# Basics of Mouse Events
# ------------------------------------------------------------------------------------------------

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')


window.push_handlers(pyglet.window.event.WindowEventLogger()) #shows the event names and parameters


# Basics of Playing Sounds and Music
# ------------------------------------------------------------------------------------------------
# using the resource.media module is for longer sounds such as music
music = pyglet.resource.media('Happier.wav')

#This is more for sound effects that will last only a few seconds -
# the difference in code allows for a more precise timing of the sounds - also allows for repeated so they don’t have to be recoded
sound = pyglet.resource.media('rollover5.wav', streaming=False)

#NOTE: MP3 and other compressed audio formats require AVbin to be installed (
# this is the default for the Windows and Mac OS X installers). Uncompressed WAV files can be played without AVbin.

# Sprites
# ------------------------------------------------------------------------------------------------
ball_image = pyglet.image.load('images.png')
ball = pyglet.sprite.Sprite(ball_image, x=window.height-400, y=window.height-450)


# Displaying all of the events
# ------------------------------------------------------------------------------------------------
music.play() #it is better to put this command before the on_draw function because it will play simultaneously to the other events( i.e mouse and keyboard events)
@window.event #this event helps refresh the window if there are changes within it
#this usually goes before an event, and the 'window' in this case should be the same variable name as your window. in this code, the variable name of the window is 'window'
def on_draw():
#this on_draw event is for re-drawing all of the elements in your code.
# The reason to re-draw these elements is because when code is first run, the elements are drawn quickly then erased.
# There are other events under the window module such as redrawing only a portion of the window, or activating/deactivating the window.
# More events and more information can be found here: https://pyglet.readthedocs.io/en/pyglet-1.2-maintenance/api/pyglet/window/pyglet.window.Window.html
    # window.clear()
    # window.clear()

    label.draw()
    ball.draw()
pyglet.app.run()#this command should always be at the end of your code because it runs your code
# ------------------------------------------------------------------------------------------------
