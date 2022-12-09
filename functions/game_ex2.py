import pgzrun

Height= 600
Width = 800

p = Actor('ironman',center=(Width//2,Height//2))

title = "IRON-MAN GAME"

def draw():
    screen.fill('white')
    screen.draw.text(title,center=(Width//2,30),fontsize=60,color='black',align='center',shadow=(.2,1),scolor="red")
    p.draw()

def p_move():
    '''function to move player'''
    if keyboard.left:
        p.x -= 3
        p.angle = 10
    elif keyboard.right:
        p.x += 3
        p.angle = -10
    elif keyboard.up:
        p.y -= 3
    elif keyboard.down:
        p.y += 3
    else:
        p.angle = 0

def handle_boundary():
    if p.x > Width:
        p.x = 0
    if p.x < 0:
        p.x = Width
    if p.y > Height:
        p.y = 0
    if p.y < 0:
        p.y = Height

def update():
    p_move() #function call
    handle_boundary() #function call
    print(p.x,p.y)
    print(p.x,p.y,p.angle)

pgzrun.go()

