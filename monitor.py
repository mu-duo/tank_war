'''
本模块用于实时监控变量/对象的数值
使用方法：
        m = monitor.Monitor(size = (x,y))
        m.add(obj)          #可多次加入对象
        m.start()
        m.close()          #调用后关闭监视器（或者手动关闭）
'''
import pygame
import threading

# 关键字颜色
KEY_COLOR = (255, 255, 255)
# 数值颜色
VALUE_COLOR = (0, 255, 255)
# 分隔符的选择和颜色
SEPARATOR = '='
SEPARATOR_COLOR = (255, 0, 0)
# 字体大小
FONT_SIZE = 50
# 字体
FONT = 'SimHei'


def get_name(obj, namespace):
    '''
    无作用，待扩展
    :param obj:
    :param namespace:
    :return:
    '''
    for name in namespace:
        if namespace[name] is obj:
            return name


def to_dict(obj):
    '''
    将对象转化为键值映射的字典
    :param obj:
    :return:
    '''
    if isinstance(obj, str):
        return {'str': obj}
    elif isinstance(obj, int):
        return {'int': str(obj)}
    elif isinstance(obj, float):
        return {'float': str(obj)}
    elif isinstance(obj, list):
        return {'list': obj}
    elif isinstance(obj, tuple):
        return {'tuple': obj}
    else:
        try:
            return obj.__dict__
        except AttributeError:
            return {'value': '该对象无数据'}


class Monitor(object):
    '''
    监视器类的定义
    '''
    def __init__(self, size=(600, 800), buffer=[]):
        '''
        初始化
        :param size: 屏幕尺寸
        :param buffer: 缓冲区
        '''
        self.size = size
        self.buffer = buffer
        self.end = False
        self.p = threading.Thread(target=Monitor.run, args=[self, ])

    def add(self, the_object, name=None):
        '''
        添加需要监听的对象
        :param the_object: 监听的对象
        :param name:       给对象的命名
        :return:           NULL
        '''
        if not name:
            name = '未命名'
        self.buffer.append((the_object, name))

    @staticmethod
    def key_in():
        '''
        监测是否手动关闭了监测器
        :return:          NULL
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    @staticmethod
    def set_font(user_font):
        '''
        设置自定义的字体
        :param user_font:  用户自定义的字体名称（str型）
        :return:                    NULL
        '''
        global FONT
        FONT = user_font

    def start(self):
        '''
        显示监测器窗口
        :return:     NULL
        '''
        self.p.start()

    def close(self):
        '''
        关闭监测器（可手动关闭）
        :return:     NULL
        '''
        self.end = True

    @staticmethod
    def run(m):
        '''
        运行监测器
        :param m:
        :return:
        '''
        pygame.init()
        screen = pygame.display.set_mode(m.size, pygame.RESIZABLE)
        pygame.display.set_caption('Dark Eye(监视器)')

        x, y = 0, 0

        if not pygame.font.match_font(FONT):
            print('监视器未找到字体\'SimHei\'，启用默认字体（无法正常显示中文），可以通过monitor.set_font(font)改变字体')
        font = pygame.font.SysFont(FONT, FONT_SIZE)
        while not m.end:
            screen.fill((0, 0, 0))
            for obj in m.buffer:
                screen.blit(font.render(obj[1], False, KEY_COLOR), (x+150, y))
                y += font.get_height()
                obj_dict = to_dict(obj[0])
                for key_word in obj_dict:
                    screen.blit(font.render(key_word, False, KEY_COLOR), (x, y))
                    try:
                        screen.blit(font.render(str(obj_dict[key_word]), False, VALUE_COLOR), (x + 300, y))
                    except pygame.error:
                        screen.blit(font.render('无法显示', False, VALUE_COLOR), (x + 300, y))
                    y += font.get_height()
                    x = 0
                screen.blit(font.render(SEPARATOR * 100, False, SEPARATOR_COLOR), (x, y))
                y += font.get_height()
            Monitor.key_in()
            x, y = 0, 0
            pygame.display.update()


if __name__ == '__main__':
    m = Monitor()
    m.add(m)
    m.start()
    print(m.__dict__)
