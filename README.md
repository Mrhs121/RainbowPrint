# RainbowPrint

## Install via pip:
`pip install RainbowPrint`

## Tutorial on how to use the RainbowPrint API

### All supported colors are below:

```
1. red
2. black
3. green
4. yellow
5. blue
6. magenta
7. cyan
8. white
```

### Pure color pattern

```
from RainbowPrint import RainbowPrint as rp
print(rp.red('Hello World'))
print(rp.red('Hello World'),rp.green('Hello Rainbow Print'))
```
You can also pass in multiple strings
```
from RainbowPrint import RainbowPrint as rp
print(rp.red('Hello World','Hello RainbowPrint'))
```

![pure](https://github.com/Mrhs121/RainbowPrint/blob/master/image/pure_color.png)



### Background color + Text clolor pattern

There are three default color schemes:

```
from RainbowPrint import RainbowPrint as rp
rp.info("Hello World")
rp.debug("Hello World")
rp.error("hello World")
```
You can also customize color schemes using the `rainbow_print` method
```
from RainbowPrint import RainbowPrint as rp
rp.rainbow_print("RainbowPrint",text_color=rp.TextColor.GREEN,background=rp.BackgroundColor.BLUE)
```

![back](https://github.com/Mrhs121/RainbowPrint/blob/master/image/back.png)

The `rainbow_print` method takes 4 arguments:
1. `data`, 
1. `display_mode`, default value is `DisplayMode.TERMINAL_DEFAULT_SETTINGS`
1. `text_color`,  default value is `TextColor.WHITE`
1. `background`,  default value is `BackgroundColor.RED`


## Customize
   ...

### Table

Beautify table print is supported starting with version 2.0 ^_^
```
    table = []
    title = ['name','email','phone','address']
    row1 = ['huang','hs123@gmail.com',111,'jiangxi yichun']
    row2 = ['jinxin','jinxin666@163.com','110119112','jiangsu jiangyin']
    row3 = ['jinxin','jinxin666@163.com','110119112','jiangsu jiangyin']
    row4 = ['jinxin','jinxin666@163.com','110119112','jiangsu jiangyin']
    table.append(title)
    table.append(row1)
    table.append(row2)
    table.append(row3)
    table.append(row4)
    rp.print_table(table, title, theme=rp.Table_Theme.BLUE_YELLOW,hilight=[2])
    rp.print_table(table,title,border_style=rp.BorderStyle.SINGLE_LINE.value,hilight=[2])
    rp.print_table(table, title, border_style=rp.BorderStyle.ROUND.value,hilight=[2])
```

The `rainbow_print` method takes 6 arguments:
1. `table`, Two-dimensional table
2. `title`, Table tile
3. `theme`, Default value is Table_Theme.GREEN, 
4. `border_style`, Default value is BorderStyle.DEFAULT.value. There are three options: `ROUND`,`SINGLE_LINE`,`DEFAULT`
5. `rich_mode`, Default value is False. Whether to turn on multi-color mode for titles
6. `hilight`, Default value is `[]`. Specifies the columns that need to be highlighted, such as `hilight=[2]`

![table](https://github.com/Mrhs121/RainbowPrint/blob/master/image/table.png)




