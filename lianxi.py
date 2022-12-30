import sys
from feichuan import Feichuan
import pygame
from lianxisettings import Settings
pygame.init()
class Bluesky:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        pygame.display.set_caption("怡雪~")
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.feichuan = Feichuan(self)
        self.bg_color = self.settings.bg_color

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._check_events()
            self._update_screen()
            self.feichuan.update()



    def _update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        self.screen.fill(self.bg_color)

        self.feichuan.blitme()
        pygame.display.flip()

    def _check_keydown_events(self,event):
        '''响应按键'''
        if event.key == pygame.K_RIGHT:
            self.feichuan.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.feichuan.moving_left = True

        elif event.key == pygame.K_UP:
            self.feichuan.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.feichuan.moving_down = True

    def _check_keyup_events(self,event):
        '''响应松开'''
        if event.key == pygame.K_RIGHT:
            self.feichuan.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.feichuan.moving_left = False
        elif event.key == pygame.K_UP:
            self.feichuan.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.feichuan.moving_down = False

    def _check_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                # print(event.key) 出来的是对应的ASCII码
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)



if __name__ == '__main__':
    ai = Bluesky()
    ai.run_game()