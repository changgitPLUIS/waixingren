import pygame
class Feichuan:
    '''管理飞船的类'''
    def __init__(self,game):
        '''初始化飞船并设置初始位置'''
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #对于每艘新飞船，都将其放在屏幕中央
        self.rect.center = self.screen_rect.center

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)