
class Dot:
    
    
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        
    
    def draw_dot(self):
        fill(255)
        stroke(255)
        ellipse(self.xPos, self.yPos, 1, 1)


width = 1200
height = 800
manual = 0
dot_list = []
num_dots = 3

def roll_dice(sides):
    return int(random(sides))

def new_dot(num_dots, dot_list):
    target_dot = dot_list[roll_dice(num_dots)]
    return dot_list.append(Dot((dot_list[-1].xPos +  target_dot.xPos)/2 , (dot_list[-1].yPos +  target_dot.yPos)/2))

'''    
def init_dots(num_dots):
    for dots in range(num_dots):
        dot_list[dots] = Dot(dots/(num_dots+1), 
'''    

                        
def setup():
    size(width, height)
    background(0)
    dot_list.append(Dot(width/2, height/4))
    dot_list.append(Dot(width/4, 3*height /4))
    dot_list.append(Dot(3*width/4, 3*height/4))
    dot_list.append(Dot(random(width), random(height)))
    
            

def mouseClicked():
    new_dot(num_dots, dot_list)
         
def draw():
    if keyPressed and key == " ":
        global manual
        manual = 1
    for i in range(len(dot_list)):
        dot_list[i].draw_dot()
    if manual:
        new_dot(num_dots, dot_list)
        
    
