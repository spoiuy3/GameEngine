import pygame
from Object3D import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
pygame.init()
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Suyeon's GameEngine")
done = False

glMatrixMode(GL_PROJECTION)
gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -3.0)
glEnable(GL_DEPTH_TEST)

cubeId = 0
cubes = []

'''
def checkCol(a, b):
    mid_a = a.mid()
    mid_b = b.mid()
    distance = np.linalg.norm(mid_a - mid_b)
    return distance < 1.0
'''

gluLookAt(0, 0, 0, 0, 0.5, 0.5, 0, 1, 0)
n = 1
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
        if pygame.key.get_pressed()[pygame.K_LSHIFT] and len(cubes)<2:
            cube = Cube()
            cubes.append(cube)
        if pygame.key.get_pressed()[pygame.K_1]:
            cubeId = 0
        if pygame.key.get_pressed()[pygame.K_2]:
            cubeId = 1
    mousePress = pygame.mouse.get_pressed()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    for cube in cubes:
        cube.draw()
    if len(cubes) > 0 and mousePress != (0, 0, 0):
        cubes[cubeId].control()
    if len(cubes) == 2 and mousePress == (0, 0, 0):
        cubes[0].control()
        cubes[1].control()
    
    # collision detection
    if len(cubes) == 2:
        if cubes[0].check_collision_with_box(cubes[1]):
            for cube in cubes:
                cube.colors = [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
            [0,0,1],[0,0,1],[0,1,1],[0,1,1],[1,1,1],[1,1,1]]
        else:
            for cube in cubes:
                cube.colors = [[1,0,0],[1,0,0],[1,0,1],[1,0,1],[0,1,0],[0,1,0],
          [0,0,1],[0,0,1],[0,1,1],[0,1,1],[1,1,1],[1,1,1]]
        
    pygame.display.flip()
    pygame.time.wait(50)
pygame.quit()