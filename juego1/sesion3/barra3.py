import pygame
pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 3")

pelota = pygame.image.load("image/bolita.jpg")
pelotarect = pelota.get_rect()
speed = [4,4]

pelotarect.move_ip(0,0)
# Crea el objeto barra, y obtengo su rectángulo
barra = pygame.image.load("image/barra.png")
barrarect = barra.get_rect()
# Pongo el barra en la parte inferior de la pantalla
barrarect.move_ip(240,450)
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        barrarect = barrarect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        barrarect = barrarect.move(3,0)
     ##Compruebo si hay colisión
    if barrarect.colliderect(pelotarect):
        speed[1] = -speed[1]
 
    pelotarect = pelotarect.move(speed)
    if pelotarect.left < 0 or pelotarect.right > ventana.get_width():
        speed[0] = -speed[0]
    if pelotarect.top < 0 or pelotarect.bottom > ventana.get_height():
        speed[1] = -speed[1]
    ventana.fill((252, 243, 207))
    ventana.blit(pelota, pelotarect)
    # Dibujo la barra
    ventana.blit(barra, barrarect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()