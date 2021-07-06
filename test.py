from RainbowPrint import RainbowPrint as rp
# print('\n')
# rp.rainbow_print("Background color + Text clolor pattern Hello RainbowPrint",text_color=rp.TextColor.GREEN,background=rp.BackgroundColor.BLUE)
#
# rp.rainbow_print("Background color + Text clolor pattern Hello RainbowPrint",text_color=rp.TextColor.RED,background=rp.BackgroundColor.GREEN)
#
# #
# #
# # #
# # # rp.rainbow_error("Error")
# # # rp.rainbow_error("Error")
# rp.error("Hello World")
# rp.debug("Hello World")
# rp.info("Hello World")
# #
# # rp.rainbow()
# # # rp.help()
# #
# print(rp.red("Rank 0"))
# print(rp.yellow("Rank 0"))
# print(rp.magenta("Rank 0"))
# print(rp.white("Rank 0"))
# print(rp.black("Rank 0"))
# print(rp.green("Rank 0"))
# print(rp.blue("Rank 0"))


def test_print_table():
    table = []
    title = ['name','ip','phone','address']
    row1 = ['node1','192.168.3.1',111,'jiangxi yichun']
    row2 = ['node2','192.168.3.221','11012','Test TestTest Test Test T']
    row3 = ['node3','af@163.com','1','jiangsu']
    row4 = ['jafjahf','jinxin666fafdsf66666@163.com','fafasdfsda','jiangsu']

    # table.append(title)
    table.append(row1)
    table.append(row2)
    table.append(row3)
    table.append(row4)

    # rp.print_table(table, title, theme=rp.Table_Theme.BLUE_YELLOW,hilight=[2])
    # rp.print_table(table, title, border_style=rp.BorderStyle.DEFAULT,alignment=rp.Alignment.RIGHT)
    rp.print_table(table, title, border_style=rp.BorderStyle.DEFAULT, alignment=rp.Alignment.MID)
    rp.print_table(table, title, border_style=rp.BorderStyle.ROUND, alignment=rp.Alignment.RIGHT)
    rp.print_table(table, title, border_style=rp.BorderStyle.SINGLE_LINE, alignment=rp.Alignment.LEFT)
    # rp.print_table(table, title, border_style=rp.BorderStyle.DEFAULT)
    # rp.print_table(table, title, border_style=rp.BorderStyle.ROUND,alignment=rp.Alignment.RIGHT)
    # rp.print_table(table, title, border_style=rp.BorderStyle.ROUND.value, alignment=rp.Alignment.MID)

test_print_table()

