import pygame
# make musicplayer :)
pygame.init()
pygame.display.set_mode((200, 100))
pygame.mixer.music.load('../../Tracks/Numb_Little_Bug.mp3')
pygame.mixer.music.play(0)

while pygame.mixer.music.get_busy():
    pygame.event.wait()
