# Dibujando un circulo en color Azul
# Importamos e inicializamos las librerias
import pygame
pygame.init()
#redimension de pantalla
ancho=500
alto=500
# pintamos la ventana
ventana = pygame.display.set_mode([ancho, alto])
# iniciando nuestro juego
juego = True
while juego:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego = False
    # fondo blanco
    ventana.fill((255, 255, 255))
    # pintamos un circulo en color azul al centro de la ventana del juego
    pygame.draw.circle(ventana, (0, 0, 255), (250, 250), 75)

    # Actualice la superficie de visualización completa a la pantalla
    pygame.display.flip()
# Hemos terminado y finalizamos.
pygame.quit()