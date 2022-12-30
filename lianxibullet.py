import pygame
from pygame.sprite import Sprite
class LianxiBullet(Sprite):
    '''管理飞船和发射子弹的类'''

    def __init__(self,game):
        '''在飞船当前位置创建一个子弹对象'''
        super().__init__()
        self.screen= game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

    #在(0,0)创建一个表示子弹的矩形，再设置正确位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)

        self.rect.midright = game.feichuan.rect.midright

        #存储用小数表示的子弹位置
        self.x = float(self.rect.x)

    def update(self):
        '''向右移动子弹'''
        self.x += self.settings.bullet_speed
        #更新表示子弹的rect位置
        self.rect.x = self.x

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)