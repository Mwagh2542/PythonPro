import pygame  
pygame.init()  
# sets the window title  
pygame.display.set_caption(u'Keyboard events')  
# sets the window size  
pygame.display.set_mode((400, 400))

while True:  
    # gets a single event from the event queue  
    event = pygame.event.wait()  
    class Employee:
        def __init__(self,fname,lname,salary):  
            self.fname=fname
            self.lname=lname
            self.salary=salary

            # Initializing the object
            harry = Employee("harry","jackson",4400)
            rohan = Employee("rohan","das",4400)


            print(harry.fname,rohan.fname)