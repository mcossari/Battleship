import pygame
pygame.init()


def splash():
    splash_sound = pygame.mixer.Sound('water-splash.mp3')
    splash_sound.play()

def explode():
    explode_sound = pygame.mixer.Sound('explosion.mp3')
    explode_sound.play()

def win():
    win_sound = pygame.mixer.Sound('win.mp3')
    win_sound.play()