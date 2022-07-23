#204 GPIO Music Box
#Date: 2022-07-22
#Owner: X.Tang
#Version: 1.0

import pygame
from gpiozero import Button

pygame.init()

drum = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav")
cymbal = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cymbal_hard.wav")
snare = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_snare_hard.wav")
bell = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cowbell.wav")

btn_drum = Button(4)
btn_cymbal = Button(17)
btn_snare= Button(27)
btn_bell = Button(10)

btn_drum.when_pressed = drum.play
btn_cymbal.when_pressed = cymbal.play
btn_snare.when_pressed = snare.play
btn_bell.when_pressed = bell.play
