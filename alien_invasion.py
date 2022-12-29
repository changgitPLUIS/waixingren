import sys
import pygame

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        self.screen = pygame.display.set_mode((800,600)) #创建一个游戏窗口，宽1200，高800像素
        pygame.display.set_caption("Alien Invasion") #设置当前窗口标题
        self.bg_color = (230,230,230)

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            for event in pygame.event.get(): #代码将会创建当前等待处理的事件的一个列表，然后使用for循环来遍历里面的事件
                if event.type == pygame.QUIT:
                    sys.exit()

            #每次循环时都重绘屏幕
            self.screen.fill(self.bg_color)

            #让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == "__main__":
    """创建游戏实例并运行游戏"""
    ai = AlienInvasion()
    ai.run_game()