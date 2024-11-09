import pgzrun

WIDTH = 500
HEIGHT = 500

def draw():
    screen.fill("pink")
    r=Rect((220,240),(220,200))
    screen.draw.filled_rect(r,"blue")

pgzrun.go()