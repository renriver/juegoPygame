import pygame
pygame.init()
ancho=640
alto=480
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("juego 2")
# Crea el objeto pelota
pelota = pygame.image.load("image/bolita.jpg")

# Obtengo el rectángulo del objeto anterior
pelotarect = pelota.get_rect()
# Inicializo los valores con los que se van a mover la pelota
speed = [4,4]
# Pongo la pelota en el origen de coordenadas
pelotarect.move_ip(0,0)
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Muevo la pelota
    pelotarect = pelotarect.move(speed)
    # Compruebo si la pelota llega a los límites de la ventana
    #if pelotarect.right > ventana.get_width():
    if pelotarect.left < 0 or pelotarect.right > ventana.get_width():
        speed[0] = -speed[0]
    #if pelotarect.bottom > ventana.get_height():        
    if pelotarect.top < 0 or pelotarect.bottom > ventana.get_height():
        speed[1] = -speed[1]
    
    ventana.fill((252, 243, 207))
    # Dibujo la pelota
    ventana.blit(pelota, pelotarect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()