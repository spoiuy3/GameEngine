import pygame
from Matrix_Func import *
from OpenGL.GL import *

class Cube:
    def __init__(self):
        self.vertices = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
                                  (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])
        self.faces = [0, 1, 2, 3, 4, 5, 6, 7, 0, 4, 5, 1, 2, 3, 7, 6, 1, 2, 6, 5, 0, 3, 7, 4]
        self.colors = [[1,0,0],[1,0,0],[1,0,1],[1,0,1],[0,1,0],[0,1,0],
          [0,0,1],[0,0,1],[0,1,1],[0,1,1],[1,1,1],[1,1,1]]
    def draw(self):
        i=0
        for t in range(0, len(self.faces), 4):
            glBegin(GL_POLYGON)
            glColor3fv(self.colors[i])
            glVertex3fv(tuple(self.vertices[self.faces[t]][:-1]))
            glVertex3fv(tuple(self.vertices[self.faces[t + 1]][:-1]))
            glVertex3fv(tuple(self.vertices[self.faces[t + 2]][:-1]))
            glVertex3fv(tuple(self.vertices[self.faces[t + 3]][:-1]))
            glEnd()
            i+=1
    
    def translate(self, pos):
        self.vertices = self.vertices @ translate_xyz(pos)

    def scale_x(self, scale_to):
        self.vertices = self.vertices @ scale_x(1-scale_to)
    
    def scale_y(self, scale_to):
        self.vertices = self.vertices @ scale_y(1-scale_to)
    
    def scale_z(self, scale_to):
        self.vertices = self.vertices @ scale_z(1-scale_to)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)
        
    def find(self):
        self.maxV = list(self.vertices[0])
        self.minV = list(self.vertices[0])
        for vertice in self.vertices:
            x, y, z, w = vertice
            if x>self.maxV[0]:
                self.maxV[0] = x
            if y>self.maxV[1]:
                self.maxV[1] = y
            if z>self.maxV[2]:
                self.maxV[2] = z
            if x<self.minV[0]:
                self.minV[0] = x
            if y<self.minV[1]:
                self.minV[1] = y
            if z<self.minV[2]:
                self.minV[2] = z
        return self.maxV, self.minV
    
    def calculate_bounding_box(self):
        max_v, min_v = self.find()
        self.bounding_box = {
            'max_x': max_v[0], 'min_x': min_v[0],
            'max_y': max_v[1], 'min_y': min_v[1],
            'max_z': max_v[2], 'min_z': min_v[2]
        }

    def check_collision_with_box(self, other_cube):
        self.calculate_bounding_box()
        other_cube.calculate_bounding_box()

        # 두 Bounding Box 간의 충돌 감지
        if (
            self.bounding_box['max_x'] > other_cube.bounding_box['min_x'] and
            self.bounding_box['min_x'] < other_cube.bounding_box['max_x'] and
            self.bounding_box['max_y'] > other_cube.bounding_box['min_y'] and
            self.bounding_box['min_y'] < other_cube.bounding_box['max_y'] and
            self.bounding_box['max_z'] > other_cube.bounding_box['min_z'] and
            self.bounding_box['min_z'] < other_cube.bounding_box['max_z']
        ):
            return True
        else:
            return False
    
    def mid(self):
        return np.mean(self.vertices[:, :-1], axis=0)
    def control(self):
        key = pygame.key.get_pressed()
        mousePress = pygame.mouse.get_pressed()
        if key[pygame.K_a] and mousePress == (1, 0, 0):
            self.translate((0.05, 0, 0))
        if key[pygame.K_d] and mousePress == (1, 0, 0):
            self.translate((-0.05, 0, 0))
        if key[pygame.K_w] and mousePress == (1, 0, 0):
            self.translate((0, 0.05, 0))
        if key[pygame.K_s] and mousePress == (1, 0, 0):
            self.translate((0, -0.05, 0))
        if key[pygame.K_q] and mousePress == (1, 0, 0):
            self.translate((0, 0, 0.05))
        if key[pygame.K_e] and mousePress == (1, 0, 0):
            self.translate((0, 0, -0.05))
        if key[pygame.K_a] and mousePress == (0, 0, 1):
            self.rotate_y(-0.05)
        if key[pygame.K_d] and mousePress == (0, 0, 1):
            self.rotate_y(0.05)
        if key[pygame.K_w] and mousePress == (0, 0, 1):
            self.rotate_x(-0.05)
        if key[pygame.K_s] and mousePress == (0, 0, 1):
            self.rotate_x(0.05)
        if key[pygame.K_q] and mousePress == (0, 0, 1):
            self.rotate_z(0.05)
        if key[pygame.K_e] and mousePress == (0, 0, 1):
            self.rotate_z(-0.05)
        if key[pygame.K_a] and mousePress[1]:
            self.scale_x(0.05)
        if key[pygame.K_d] and mousePress[1]:
            self.scale_x(-0.05)
        if key[pygame.K_w] and mousePress[1]:
            self.scale_y(-0.05)
        if key[pygame.K_s] and mousePress[1]:
            self.scale_y(0.05)
        if key[pygame.K_q] and mousePress[1]:
            self.scale_z(0.05)
        if key[pygame.K_e] and mousePress[1]:
            self.scale_z(-0.05)
        if key[pygame.K_a] and mousePress == (0, 0, 0):
            self.translate((-0.1, 0, 0))
        if key[pygame.K_d] and mousePress == (0, 0, 0):
            self.translate((0.1, 0, 0))
        if key[pygame.K_w] and mousePress == (0, 0, 0):
            self.translate((0, -0.1, 0))
        if key[pygame.K_s] and mousePress == (0, 0, 0):
            self.translate((0, 0.1, 0))
        if key[pygame.K_q] and mousePress == (0, 0, 0):
            self.translate((0, 0, -0.1))
        if key[pygame.K_e] and mousePress == (0, 0, 0):
            self.translate((0, 0, 0.1))
        if key[pygame.K_UP] and mousePress == (0, 0, 0):
            self.rotate_x(0.005)
        if key[pygame.K_DOWN] and mousePress == (0, 0, 0):
            self.rotate_x(-0.005)
        if key[pygame.K_LEFT] and mousePress == (0, 0, 0):
            self.rotate_z(0.005)
        if key[pygame.K_RIGHT] and mousePress == (0, 0, 0):
            self.rotate_z(-0.005)