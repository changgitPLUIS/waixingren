import pygame
import random
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """ 表示单滴雨点的类 """

    def __init__(self, ai_game):
        """ 初始化雨滴并设置其起始位置 """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/yudi.bmp')
        self.image = pygame.transform.scale(self.image,(40,40.5))
        # rect_mul = random.randint(10, 20)
        # self.image = pygame.transform.smoothscale(self.image, (rect_mul, rect_mul * 1.5))
        self.rect = self.image.get_rect()

        # 每滴雨点最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储雨点的精确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """ 向下移动雨滴 """
        raindrop_speed_mul = 0.5
        self.y += self.settings.raindrop_speed * raindrop_speed_mul
        self.rect.y = self.y