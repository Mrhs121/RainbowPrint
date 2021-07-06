# 0	终端默认设置
# 1	高亮显示
# 4	使用下划线
# 5	闪烁
# 7	反白显示
# 8	不可见

from enum import Enum, unique
from datetime import datetime


@unique
class TextColor(Enum):
    Default = 0
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
    Default = 0
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


def rainbow_print(data, display_mode=DisplayMode.HIGHLIGHT, text_color=TextColor.YELLOW,
                  background=BackgroundColor.BLUE):
    """
    Output color text in the terminal

    Args:
        data: Text that needs to be printed.
        display_mode:
        text_color: the color of text.
        background: the color of background.
    """
    print(base_str.format(display_mode.value, text_color.value, background.value, data))

def rainbow(data, display_mode=DisplayMode.TERMINAL_DEFAULT_SETTINGS, text_color=TextColor.WHITE,
                  background=BackgroundColor.RED):
    return base_str.format(display_mode.value, text_color.value, background.value, data)

def rich(data, display_mode=DisplayMode.HIGHLIGHT, text_color=TextColor.BlACK,
         background=BackgroundColor.BLUE):
    return base_str.format(display_mode.value, text_color.value, background.value, data)


def get_time():
    return '[{}]'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])


def info(*string_data):
    print(get_time(),
          base_str.format(DisplayMode.HIGHLIGHT.value, TextColor.WHITE.value, BackgroundColor.GREEN.value, ' INFO  '),
          green(*string_data))


def error(*string_data):
    print(get_time(),
          base_str.format(DisplayMode.HIGHLIGHT.value, TextColor.WHITE.value, BackgroundColor.RED.value, ' ERROR '),
          red(*string_data))


def debug(*string_data):
    print(get_time(),
          base_str.format(DisplayMode.HIGHLIGHT.value, TextColor.WHITE.value, BackgroundColor.MAGENTA.value, ' DEBUG '),
          magenta(*string_data))


def generate_color(*datas, color):
    base_str = '\033[{}m{}\033[0m'
    res = ''
    for index, arg in enumerate(datas):
        res += base_str.format(color, arg)
        if index < len(datas) - 1:
            res += ' '
    return res


def red(*datas):
    return generate_color(*datas, color=TextColor.RED.value)


def black(*datas):
    return generate_color(*datas, color=TextColor.BlACK.value)


def green(*datas):
    return generate_color(*datas, color=TextColor.GREEN.value)


def yellow(*datas):
    return generate_color(*datas, color=TextColor.YELLOW.value)


def blue(*datas):
    return generate_color(*datas, color=TextColor.BLUE.value)


def magenta(*datas):
    return generate_color(*datas, color=TextColor.MAGENTA.value)


def cyan(*datas):
    return generate_color(*datas, color=TextColor.CYAN.value)


def white(*datas):
    return generate_color(*datas, color=TextColor.WHITE.value)


def default(*datas):
    return generate_color(*datas, color=TextColor.Default.value)


def print_rainbow():
    t = [i for i in range(30, 38)]
    b = [i for i in range(40, 48)]
    for tc in t:
        for bc in b:
            print('\033[1;{};{}m{} [textcolor:{}, background:{}]\033[0m'.format(tc, bc, 'RainBow', TextColor(tc).name,
                                                                                BackgroundColor(bc).name))


@unique
class Table_Theme(Enum):
    DEFAULT = (default, default)
    BLUE = (blue, default)
    GREEN = (green, default)
    RED_BLACK = (red, black)
    RED_WHITE = (red, white)
    GREEN_WHITE = (green, white)
    WHITE_RED = (default, red)
    BLUE_YELLOW = (blue, yellow)

@unique
class Alignment(Enum):
    LEFT = 1
    RIGHT = 2
    MID = 3

class BorderStyle(Enum):
    DEFAULT = {'start': '╔', 'split_line_start': '╠', 'end': '╗', 'split_line_end': '╣', 'end_line_start': '╚',
               'end_line_end': '╝', 'mid': '╦', 'split_line_mid': '╬', 'end_line_mid': '╩', 'row_line': '═',
               'clo_line': '║'}
    SINGLE_LINE = {'start': '┌', 'split_line_start': '├', 'end': '┐', 'split_line_end': '┤', 'end_line_start': '└',
                   'end_line_end': '┘', 'mid': '┬', 'split_line_mid': '┼', 'end_line_mid': '┴', 'row_line': '─',
                   'clo_line': '│'}
    ROUND = {'start': '╭', 'split_line_start': '├', 'end': '╮', 'split_line_end': '┤', 'end_line_start': '╰',
                   'end_line_end': '╯', 'mid': '┬', 'split_line_mid': '┼', 'end_line_mid': '┴', 'row_line': '─',
                   'clo_line': '│'}

def print_table(table, title, theme=Table_Theme.GREEN, border_style=BorderStyle.DEFAULT, rich_mode=False, hilight=[],alignment=Alignment.LEFT):
    if hilight != []:
        assert max(hilight) < len(title), "hilight index must < the len of row"
    cloum_max = []
    border_style = border_style.value
    for cloum in range(0, len(table[0])):
        max_len = max([len(str(data[cloum])) for data in table])
        cloum_max.append(max_len)

    def print_spilt_line(start='|', end='╣', line='-', mid='═', row_color=default):
        print()
        print(row_color(start), end='')
        for index, str_len in enumerate(cloum_max):
            if index != len(cloum_max) - 1:
                print(row_color(line * (str_len + 3) + mid), end='')
            else:
                print(row_color(line * (str_len + 3) + end), end='')
        print()
    import math
    def print_row(row, row_color, rich_mode=False, is_title=False, hilight=[],border_style = BorderStyle.DEFAULT.value,alignment=Alignment.LEFT):
        for index, data in enumerate(row):
            str_len = cloum_max[index]
            data_len = len(str(data))
            space = ' ' * (str_len - data_len)
            if index in hilight and not is_title:
                # data = red(data)
                data = rainbow(data)
            # if rich_mode and index != len(row) - 1:
            #     print(rich(' ' + str(data) + space + '  ') + border_style['clo_line'], end='')
            # elif rich_mode and index == len(row) - 1:
            #     print(rich(' ' + str(data) + space + '  ') + border_style['clo_line'], end='')
            # else:
                # if is_title:
            if alignment == Alignment.LEFT:
                print(row_color(' ' + str(data) + space + '  '+border_style['clo_line']), end='')
            elif alignment == Alignment.RIGHT:
                print(row_color('  '+space + str(data) + ' ' +border_style['clo_line']), end='')
            else:
                left_spce = ' ' * math.ceil((str_len - data_len)/2)
                right_space = ' ' * math.floor((str_len - data_len)/2)
                print(row_color(' ' + left_spce + str(data) + right_space + '  ' + border_style['clo_line']), end='')
                # else:
                #     print(row_color(' ' + str(data) + ' ' * (str_len - len(str(data)))) + '  |', end='')

    # print_spilt_line(start='╔', line='═', end='╗', mid='╦', row_color=theme.value[0])
    print_spilt_line(start=border_style['start'], line=border_style['row_line'], end=border_style['end'],
                     mid=border_style['mid'], row_color=theme.value[0])
    for index, row in enumerate(table):
        if index == 0:
            print(theme.value[0](border_style['clo_line']), end='')
            print_row(row, theme.value[0], rich_mode, is_title=True,border_style=border_style,alignment=alignment)
            print_spilt_line(start=border_style['split_line_start'], mid=border_style['split_line_mid'],
                             line=border_style['row_line'], end=border_style['split_line_end'],
                             row_color=theme.value[0])
        elif index == len(table) - 1:
            # last split line
            print(theme.value[1](border_style['clo_line']), end='')
            print_row(row, theme.value[1], hilight=hilight,border_style=border_style,alignment=alignment)
            print_spilt_line(start=border_style['end_line_start'], line=border_style['row_line'],
                             mid=border_style['end_line_mid'], end=border_style['end_line_end'],
                             row_color=theme.value[1])
        else:
            print(theme.value[1](border_style['clo_line']), end='')
            print_row(row, theme.value[1], hilight=hilight,border_style=border_style,alignment=alignment)
            print_spilt_line(start=border_style['split_line_start'], mid=border_style['split_line_mid'],
                             end=border_style['split_line_end'],line=border_style['row_line'], row_color=theme.value[1])

# def help():
#     dispaly_mode = '''
#      0	终端默认设置
#      1	高亮显示
#      4	使用下划线
#      5	闪烁
#      7	反白显示
#      8	不可见
#     '''
#     print(dispaly_mode)
