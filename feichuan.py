import pygame
class Feichuan:
    '''管理飞船的类'''
    def __init__(self,game):
        '''初始化飞船并设置初始位置'''
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/rocket.bmp")
        self.image = pygame.transform.scale(self.image, (40, 60)) #改变飞船大小
        self.rect = self.image.get_rect()

        #对于每艘新飞船，都将其放在屏幕中央
        self.rect.center = self.screen_rect.center

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动标志来调整飞船位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
        elif self.moving_up and self.rect.top > 0:
            self.rect.y -= 1

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)