import circleshape
import pygame
import constants_anotherthing

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
    
    def draw(self, surface):
        pygame.draw.circle(surface = surface, color = "white", center=self.position, radius=self.radius, width=constants_anotherthing.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
