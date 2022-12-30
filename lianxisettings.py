class Settings:
    '''存储游戏所有设置的类'''

    def __init__(self):
        '''初始化游戏的类'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 8
        self.bullet_height = 3
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3