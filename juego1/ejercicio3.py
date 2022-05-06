import pygame
# Inicialización de Pygame
pygame.init()
#tamaño de la ventana en ancho y alto (x,y)
ancho=640
alto=480
# Inicialización de la superficie de dibujo
ventana = pygame.display.set_mode((ancho,alto))
# Bucle principal del juego
jugando = True
while jugando:
    # Comprobamos los eventos
    #Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente
    ventana.fill((255, 255, 255))
    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()
    
pygame.quit()