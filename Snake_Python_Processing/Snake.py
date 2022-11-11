

class Snake:
    
    def __init__(self, pos, vel=PVector(0,0)):
        self.pos = pos
        self.vel = vel
        self.body = [pos] #stores all segments positions
        self.segment_width = 25
    
    
    def show(self):
        fill(150,255,150) #RGB Green
        for i in range(len(self.body)):
            square(self.body[i].x, self.body[i].y, self.segment_width)
    
    
    def move(self, vel_factor):
        # first moveh head = body[0]
        new_head_pos = self.body[0] + self.vel * vel_factor * self.segment_width
        self.body.insert(0, new_head_pos)
        # delete the last known segment position of the body 
        self.body.pop(-1)
        
    
    def move_up(self):
        if self.vel.y != 1:
            # avoid snake turn 180 up if its going down
            self.vel = PVector(0, -1)
   
    def move_down(self):
        if self.vel.y != -1:
            self.vel = PVector(0, 1)
            
    def move_left(self):
        if self.vel.x != 1:
            self.vel = PVector(-1, 0)
            
    def move_right(self):
        if self.vel.x != -1:
            self.vel = PVector(1, 0) 
            
    
    def detect_wall(self, window_size):
        # avoid snake disappear into the bytes infinite :D
        # 5 is a buffer to detect the limits of the screen earlier
        for i in range(len(self.body)):
            if self.body[i].x >= window_size.x - 5 * self.vel.x:
                # approaching right side
                # so reset head x coordinate to left side
                self.body[i].x = 0
            elif self.body[i].x < 0 + 5 * -self.vel.x:
                self.body[i].x = window_size.x
            if self.body[i].y >= window_size.y - 5 * self.vel.y:
                # approaching top side
                # so reset head y coordinate to bottom side
                self.body[i].y = 0
            elif self.body[i].y < 0 + 5 * -self.vel.y:
                self.body[i].y = window_size.y
    
    def eat_apple(self, apple):
        # test if its close
        if abs(self.body[0].x + self.segment_width/2 - apple.pos.x) <= self.segment_width and abs(self.body[0].y + self.segment_width/2 - apple.pos.y) <= self.segment_width:
            self.add_segment()
            return True
        return False
    
    def add_segment(self):
        # just duplicate the last segment in the body [] and append to the end
        self.body.append(self.body[-1])
        
    
    
    
    
    
