class Apple:
    
    def __init__(self, pos):
        self.pos = pos
        print('New apple created at: ', self.pos)
    
    def show(self):
        fill(255, 150, 150) # RGB Red
        circle(self.pos.x, self.pos.y, 20)
