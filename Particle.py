import sys, random, pygame
from pygame import *

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

x1, y1, x2, y2 = 120, 260, 120, 120
rect_list = [[x1, y1], [x2, y2]]

def circle_surface(radius, color):
    surface = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surface, color, (radius, radius), radius)
    return surface

# [loc, velocity, timer]
particles = []

mode = 1

while True:
    screen.fill((0,0,0))
    mx, my = pygame.mouse.get_pos()
    if mode == 1:
        particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -5], random.randint(6, 11)])
        pygame.draw.rect(screen, (25, 25, 125), pygame.Rect(mx-8, my, 16, 100))
        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            pygame.draw.circle(screen, (0, 0, 0), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

            radius = particle[2] * 1.5
            screen.blit(circle_surface(radius, (120, 20, 60)), (int(particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGB_ADD)

            if particle[2] <= 8:
                particles.remove(particle)
        
    elif mode == -1:
        pygame.draw.rect(screen, (125, 25, 125), pygame.Rect(x1,y1, 160, 30))
        particles.append([[mx, my], [random.randint(0, 42) / 6 - 3.5, random.randint(0, 42) / 6 - 3.5], random.randint(4, 11)])
        for particle in particles:
            particle[0][0] += particle[1][0]
            if (x1-10 < particle[0][0] < x1+170) and (y1-10 < particle[0][1] <y1+40):
                particle[1][1] = -0.85 * particle[1][1]
                particle[0][1] += particle[1][1] * 2
            particle[0][1] += particle[1][1]
            particle[2] -= 0.035
            particle[1][1] += 0.15
            radius = particle[2] * 0.5
            screen.blit(circle_surface(radius, (120, 20, 60)), (int(particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGB_ADD)
            if particle[2] <= 0:
                particles.remove(particle)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if pygame.key.get_pressed()[pygame.K_k]:
        mode = -mode

    pygame.display.update()
    mainClock.tick(60)