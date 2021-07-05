from RainbowPrint import RainbowPrint as rp

# rp.rainbow_print("RainbowPrint",text_color=rp.TextColor.GREEN,background=rp.BackgroundColor.BLUE)
#
#
# #
# # rp.rainbow_error("Error")
# # rp.rainbow_error("Error")
# rp.error("Error")
# rp.debug("debug")
# rp.info("info")
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
    title = ['name','email','phone','address']
    row1 = ['huang','godhuangh;*&^%$#@!s@gmail.com',111,'jiangxi yichun']
    row2 = ['jinxin','jinxin666@163.com','110119112','jiangsu jiangyin']
    row3 = ['jinxin','jinxin666@163.com','110119112','jiangsu jiangyin']
    row4 = ['jinxin','jinxin666@163.com','110119112','jiangsu jiangyin']
    row5 = ['niubiwa','zhenniuwa6666@163.com','666666666666666666','beijing shanghai shenzhen']
    table.append(title)
    table.append(row1)
    table.append(row2)
    table.append(row3)
    table.append(row4)
    # table.append(row5)
    # rp.print_table(table,title,theme=rp.Theme.WHITE_RED,rich_mode=False)
    # rp.print_table(table,title,theme=rp.Theme.DEFAULT,rich_mode=True)
    # rp.print_table(table,title,theme=rp.Theme.BLUE_YELLOW,rich_mode=False)
    # rp.print_table(table,title,rich_mode=False,hilight=[2])
    rp.print_table(table, title, theme=rp.Table_Theme.BLUE_YELLOW,hilight=[2])
    rp.print_table(table,title,border_style=rp.BorderStyle.SINGLE_LINE.value,hilight=[2])
    rp.print_table(table, title, border_style=rp.BorderStyle.ROUND.value,hilight=[2])
test_print_table()