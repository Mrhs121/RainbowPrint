# 0	终端默认设置
# 1	高亮显示
# 4	使用下划线
# 5	闪烁
# 7	反白显示
# 8	不可见

from enum import Enum, unique

@unique
class TextColor(Enum):
    BlACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

@unique
class BackgroundColor(Enum):
    BlACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47

@unique
class DisplayMode(Enum):
    TERMINAL_DEFAULT_SETTINGS = 0
    HIGHLIGHT = 1
    USE_UNDERLINE = 4
    BLINK = 5
    BACKWHITE_DISPLAY = 7
    INVISIBLE = 8

base_str = '\033[{};{};{}m{}\033[0m'

def rainbow_print(data,display_mode=DisplayMode.HIGHLIGHT, text_color=TextColor.YELLOW, background=BackgroundColor.BLUE):
    """
    Output color text in the terminal

    Args:
        data: Text that needs to be printed.
        display_mode:
        text_color: the color of text.
        background: the color of background.
    """
    print(base_str.format(display_mode.value, text_color.value, background.value, data))


def rainbow_info(data):
    rainbow_print(data, DisplayMode.TERMINAL_DEFAULT_SETTINGS,
            TextColor.WHITE,
            BackgroundColor.GREEN
            )


def rainbow_error(data):
    rainbow_print(data, DisplayMode.TERMINAL_DEFAULT_SETTINGS,
            TextColor.YELLOW,
            BackgroundColor.RED
            )

def rainbow_debug(data):
    rainbow_print(data, DisplayMode.TERMINAL_DEFAULT_SETTINGS,
            TextColor.YELLOW,
            BackgroundColor.BLUE
            )

def rainbow():
    t = [i for i in range(30,38)]
    b = [i for i in range(40,48)]
    for tc in t:
        for bc in b:
            print('\033[1;{};{}m{} [textcolor:{}, background:{}]\033[0m'.format(tc,bc,'RainBow',TextColor(tc).name,BackgroundColor(bc).name))

def help():
    dispaly_mode ='''
     0	终端默认设置
     1	高亮显示
     4	使用下划线
     5	闪烁
     7	反白显示
     8	不可见
    '''
    print(dispaly_mode)
