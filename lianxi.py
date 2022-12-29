import sys
from feichuan import Feichuan
import pygame
class Bluesky:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("怡雪~")
        self.bg_color = (230,230,230)
        self.feichuan = Feichuan(self)

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.feichuan.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    ai = Bluesky()
    ai.run_game()