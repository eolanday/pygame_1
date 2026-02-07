import pygame
import player_somethingelse
import shot
from constants_anotherthing import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player_somethingelse.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, drawable, updatable)

    player = player_somethingelse.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if a.collides_with(s):
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000.0


if __name__ == "__main__":
    main()
