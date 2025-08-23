import pygame
import sys

pygame.init()
try:
    pygame.mixer.music.load('ex0021.mp3')  # Certifique-se que o arquivo está na mesma pasta
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    print('Fim da música')
    sys.exit(1)
finally:
    pygame.quit()