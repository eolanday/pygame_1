import circleshape
import pygame
import constants_anotherthing
import random
from logger import log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface = surface, color = "white", center=self.position, radius=self.radius, width=constants_anotherthing.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants_anotherthing.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.randint(20, 50)
        v1 = self.velocity.rotate(rand_angle)
        v2 = self.velocity.rotate(-1 * rand_angle)
        small_radius = self.radius - constants_anotherthing.ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, small_radius)
        a1.velocity = v1
        a2 = Asteroid(self.position.x, self.position.y, small_radius)
        a2.velocity = v2

