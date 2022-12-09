import pgzrun
from random import randint

HEIGHT= 600
WIDTH = 1200

p = Actor('ironman',center=(WIDTH//2,HEIGHT//2))
c = Actor('cookie',(randint(0,WIDTH),randint(0,HEIGHT)))
title = "IRON-MAN GAME"
score = 0
music.play('drake')

def draw():
    screen.fill("white")
    screen.blit("bg",(0,0))
    screen.draw.text(title,center=(WIDTH//2,30),fontsize=60,color='black',align='center',shadow=(.2,1),scolor="red")
    screen.draw.text(f'score: {score}',(10,10),fontsize=50,color='white')
    p.draw()
    c.draw()
    

def p_move():
    if keyboard.right and p.right < WIDTH:
        p.x +=3 
        p.angle = -10
    elif keyboard.left and p.left > 0:
        p.x -= 3
        p.angle = 10
    else:
        p.angle = 0
    if keyboard.up and p.top > 0:
        p.y -= 3
    if keyboard.down and p.bottom < HEIGHT:
        p.y += 3

def update():
    global score         # tells python, that we want to chamge the value of the global variable score
    p_move()             #function call
    if p.colliderect(c):
        score += 1
        c.pos = (randint(0,WIDTH),randint(0,HEIGHT))
        sounds.sui.play()
   
    print(p.x,p.y,p.angle)

pgzrun.go()

