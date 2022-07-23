#204 GPIO Music Box
#Date: 2022-07-22
#Owner: X.Tang
#Version: 1.0

import pygame
from gpiozero import Button

pygame.init()

drum = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav")

btn_drum = Button(17)

btn_drum.when_pressed = drum.play


# run drum.play() in the Interactive shell
