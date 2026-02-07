import circleshape
import constants_anotherthing
import pygame
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants_anotherthing.PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants_anotherthing.LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += constants_anotherthing.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown > 0:
                return
            self.cooldown = constants_anotherthing.PLAYER_SHOOT_COOLDOWN_SECONDS
            self.shoot()

    def move(self, dt):
        unit = pygame.Vector2(0, 1).rotate(self.rotation) * constants_anotherthing.PLAYER_SPEED * dt
        self.position += unit

    def shoot(self):
        player_shot = shot.Shot(self.position.x, self.position.y, constants_anotherthing.SHOT_RADIUS)
        player_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        player_shot.velocity *= constants_anotherthing.PLAYER_SHOOT_SPEED
        
