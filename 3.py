import pygame as pg
import sys , random, time

pg.init()
pg.mixer.init()

screen_size = (600, 400)
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("cool game")
score = 0
font = pg.font.Font("Karma Future.otf", 32)

winSound = pg.mixer.Sound("outwin.wav")
loseSound = pg.mixer.Sound("outlose.wav")
collectSound = pg.mixer.Sound("outcollect.wav")

ck = random.randint(1,screen_size[0])

icon = pg.image.load("sans.png")
pg.display.set_icon(icon)

clock = pg.time.Clock()
bg = pg.image.load("bg.png").convert()
bg = pg.transform.scale(bg, screen_size)  # Scale the background image

Pai = pg.image.load("trap.png").convert_alpha()
Pai = pg.transform.scale(Pai, (100, 100))  # Scale the Pai image
Pai_rect = Pai.get_rect(top=300, left=250)  # Set initial position

humans = pg.image.load("human.png").convert_alpha()
humans = pg.transform.scale(humans , (40 , 40))
humans = pg.transform.rotate(humans , 20.4)
human = humans.get_rect(top=3, left=random.randrange(screen_size[0]))



def show_score():
    global font
    winSound.play
    txt = font.render(f"score:{score}" , False , "black")
    screen.blit(txt, (screen_size[0] / 2 - 50 , 20))
def game_over():
    global font
    txt = font.render("game over" ,False , "white")
    loseSound.play()
    screen.blit(txt , (screen_size [0] / 2 - 50 , screen_size [1] / 2 - 50))
   
    pg.display.flip()
    time.sleep(2)
def won():
    global font
    txt = font.render("You Win !" ,False , "white")
    screen.blit(txt , (screen_size [0] / 2 - 50 , screen_size [1] / 2 - 50))
    
    pg.display.flip()
    time.sleep(2)
while True:
    
    
    screen.blit(bg, (0, 0))  # Draw background
    
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()  # Get pressed keys
    if keys[pg.K_LEFT]:
        Pai_rect.x -= 5  # Update Pai's position based on key presses
    elif keys[pg.K_RIGHT]:
        Pai_rect.x += 5
    for i in range(10):
        screen.blit(humans , human)
    human.y += 4
    
    screen.blit(Pai, Pai_rect)  # Draw Pai

    if Pai_rect.colliderect(human):
        for i in range(random.randrange(0 , 10)):
            human.top = 3
            human.x += ck + random.randrange(0,100) *2
            if human.x >= screen_size[0]:
                human.x = random.randrange(0 , 300)
                
            elif human.x <= 0:
                human.x = 200 
            elif human.x == 200:
                human.x *= 3
        score += 1
        collectSound.play()
    show_score()
    if score >= 7 :
        won()
        sys.exit()
    elif human.y >= screen_size[1]:
        game_over()
        sys.exit()
    clock.tick(60)  # Limit FPS
    pg.display.update()  # Update display

    pg.display.update()  # Update display
    
