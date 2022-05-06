import pygame
pygame.init()
ancho=640
alto=480
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("juego 2")
# Crea el objeto pelota
ball = pygame.image.load("image/bolita.jpg")

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    
    ventana.fill((252, 243, 207))
    # Dibujo la pelota
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()