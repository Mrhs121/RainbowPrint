# RainbowPrint
python 彩色打印文本

# 安装
```
git clone https://github.com/Mrhs121/RainbowPrint.git
pip install ./dist/RainbowPrint-0.0.1-py3-none-any.whl
```

# 使用方法
## 默认自带三种配色，info，debug，error

```
from RainbowPrint import RainbowPrint as rp
rp.rainbow_info('test')
rp.rainbow_debug('test')
rp.rainbow_error('test')
```
![rp2](https://github.com/Mrhs121/RainbowPrint/blob/main/pics/rp2.png)  



## 使用 ``` rp.rainbow() ``` 查看所有颜色搭配
![rp](https://github.com/Mrhs121/RainbowPrint/blob/main/pics/rp.png)


## 自定义颜色，可以从rp.rainbow()中查询所有颜色
```
from RainbowPrint import RainbowPrint as rp
rp.rainbow_print("test",text_color=rp.TextColor.YELLOW,background=rp.BackgroundColor.BLUE)
```
![rp](https://github.com/Mrhs121/RainbowPrint/blob/main/pics/rp3.png)
