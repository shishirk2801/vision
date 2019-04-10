
file = '/home/dexter/Desktop/letsgo.mp3'
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()
