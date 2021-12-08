import random

import pygame
from pygame.math import Vector2

import core


class balle:
    def __init__(self,largeur=400,hauteur=400):
        self.position = Vector2(400,200)
        self.taille = 10
        self.couleur = (255,0,0)
        self.vel = Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
        self.acc = Vector2()
        self.maxAcc = 300
        self.maxVel = 4
        self.force = 0
