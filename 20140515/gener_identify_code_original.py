#coding: UTF-8
#载入必要的模块
# 注意：如果要生成中文其中的字体设置中，要设置支持中文的字体。不然会生成乱码
import os
import pygame
from pygame.locals import *
#pygame初始化
pygame.init()
text = u"PythonTab中文网"
#设置字体和字号
font = pygame.font.SysFont('Microsoft YaHei', 64)
#渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
ftext = font.render(text, True, (65, 83, 130),(255, 255, 255))
#保存图片
pygame.image.save(ftext, "D:/pythontab.jpg")#图片保存地址