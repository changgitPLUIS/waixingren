import random
import sys
import pygame
from random import randint
from rainsetting import Settings
from rain import Raindrop


class Rainsky:
    """ 管理游戏资源和行为的类 """

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()
        self.settings = Settings()

        # 创建一个显示窗口，并设置窗口尺寸
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Raining Day")
        self.rains = pygame.sprite.Group()
        self._create_rains()

    def run_game(self):
        """ 开始游戏的主循环 """
        while True:
            self._check_events()
            self._update_rains()
            self._update_screen()

    def _update_rains(self):
        """ 更新细雨中所有雨滴的位置 """
        self._check_rains_bottom()
        self.rains.update()

    def _check_events(self):
        """ 响应按键和鼠标事件 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_rains(self):
        """ 创建细雨 """
        # 创建一滴雨点并计算一行可容纳多少滴雨点
        rain = Raindrop(self)
        rain_width, rain_height = rain.rect.size
        number_rains_x = self.settings.screen_width // (8 * rain_width)

        # 计算屏幕可容纳多少行雨滴
        number_rows = self.settings.screen_height // (8 * rain_height)

        # 创建雨滴行列
        for row_number in range(number_rows):
            for rain_number in range(number_rains_x):
                self._create_rain()

    def _create_rain(self):
        # 创建一滴雨点并将其加入到当前行
        rain = Raindrop(self)
        screen_rect = self.screen.get_rect()
        rain.rect.x = random.randint(0, screen_rect.right)
        rain.y = random.randint(0, 300)
        rain.rect.y = rain.y
        self.rains.add(rain)

    def _check_rains_bottom(self):
        """ 检查是否有雨滴到达了屏幕底端,并做出响应 """
        screen_rect = self.screen.get_rect()
        for rain in self.rains.copy():
            if rain.rect.bottom >= screen_rect.bottom:
                self.rains.remove(rain)
                self._create_rain()

    def _update_screen(self):
        """ 更新屏幕上的图像，并切换到新屏幕 """
        self.screen.fill(self.settings.bg_color)
        self.rains.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = Rainsky()
    ai.run_game()