import pgzrun

WIDTH = 1200
HEIGHT =600

scr = 0

def gamescr(bgcolor,title,info="Play the Game"):
     screen.fill(bgcolor)
     screen.draw.text(title,center= (WIDTH/2,HEIGHT/2),fontsize=100,color='white',align='center')
     screen.draw.text(info,center=(WIDTH/2,HEIGHT/2+100),fontsize=50,color='white',align='center')




def draw():
    if scr==0:
        gamescr('black','Amazing GAME','Press space to Start')
    elif scr == 1:
        gamescr('green','Game is Running','Press esc to End')
    elif scr==2:
        gamescr("purple",'GAME OVER','Press enter to Restart')

def update():
    global scr
    if keyboard.space and scr == 0:
        scr=1
    elif keyboard.escape and scr == 1:
        scr=2
    if keyboard.RETURN and scr == 2:  #RETURN means enter button
        scr=0

pgzrun.go()