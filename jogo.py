import pygame as pg

pg.init()
pg.display.set_caption('Muda cor')
screen = pg.display.set_mode((300, 300))


done = False
x = 20
y = 20
clock = pg.time.Clock()

font = pg.font.Font('freesansbold.ttf', 16) 
text = font.render('Passe a linha para mudar de cor', True, (255, 255, 255) , (0, 0, 0) ) 
textRect = text.get_rect()  
textRect.center = (150 , 130 ) 

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    pressed = pg.key.get_pressed()


    if pressed[pg.K_UP]:
        y -= 3
    if pressed[pg.K_DOWN]:
        y += 3
    if pressed[pg.K_LEFT]:
        x -= 3
    if pressed[pg.K_RIGHT]:
        x += 3

    if y > 155:
        color = (255, 100, 0)
    else:
        color = (0, 128, 255)

    if y < 0:
        y = 0
    if y > 270:
        y = 270

    if x < 0:
        x = 0
    if x > 270:
        x = 270

    screen.fill((0, 0, 0))
    
    screen.blit(text, textRect) 

    pg.draw.rect(screen, (255, 0, 0), pg.Rect(0, 150, 300, 10))

    pg.draw.rect(screen, color, pg.Rect(x, y, 40, 40))

    pg.display.flip()
    clock.tick(60)




"""     if pressed[pg.K_a]:
        is_blue = not is_blue """