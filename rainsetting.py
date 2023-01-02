class Settings:
    """ 存储游戏中所有设置的类 """

    def __init__(self):
        """ 初始化游戏的设置 """
        # 屏幕设置
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (250, 250, 250)

        # 雨滴下落速度设置
        self.raindrop_speed = 1