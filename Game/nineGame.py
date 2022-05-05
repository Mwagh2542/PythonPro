import pyglet  
window = pyglet.window.Window()  
lable = pyglet.text.Label('Hello Atharva Gaming World', font_name='Times New Roman', font_size=36,  
                          x= window.width//2,y=window.height//2,anchor_x='center', anchor_y='center')  
@window.event  
def on_draw():  
    window.clear()  
    lable.draw()  
pyglet.app.run()
"""
Pyglet
    Python provide another game library named pyglet which is cross-platform windowing and multimedia library for Python. 
    It is used to developing games and other visually rich applications. It supports user interface event handling, windowing, 
    OpenGL graphics, loading images and videos, and playing sounds and music.

Few features of pyglet are the following:
    No external installation requirements or dependencies.
    Take benefit of multiple windows and multi-monitor.
    It can load images, sound, music, and video in any format.
    Pyglet is provided under the BSD open-source license.
    It supports both Python 2 and 3 

Installation of pyglet is simple; it can be installed by typing the following command
pip install pyglet
"""