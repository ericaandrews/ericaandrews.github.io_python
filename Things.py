#This program creates a "dancing" character with the use of definition functions. 
#The character is given a set of assigned movements and a name
#Once the characters name is called, the set of assigned movements is displayed. 

class things():
    pass
class animate(things):
    pass
class animals(animate):
    pass
class mammals(animals):
    pass
class giraffes(mammals):
    def left_foot_forward(self):
        print('left foot forward')
    def left_foot_backward(self):
        print('left foot backward')
    def right_foot_forward(self):
        print('right foot forward')
    def right_foot_backward(self):
        print('right foot backward')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_forward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_backward()

reginald = giraffes()
reginald.dance()
