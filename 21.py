import pygame

pygame.init()
pygame.mixer.music.load('C:\App\ETEC ESTUDOS\old-fashioned-telephone-ringing-sound.mp3')
pygame.mixer.music.play()
pygame.event.wait()