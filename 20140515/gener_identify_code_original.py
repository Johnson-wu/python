#coding: UTF-8
#�����Ҫ��ģ��
# ע�⣺���Ҫ�����������е����������У�Ҫ����֧�����ĵ����塣��Ȼ����������
import os
import pygame
from pygame.locals import *
#pygame��ʼ��
pygame.init()
text = u"PythonTab������"
#����������ֺ�
font = pygame.font.SysFont('Microsoft YaHei', 64)
#��ȾͼƬ�����ñ�����ɫ��������ʽ,ǰ�����ɫ��������ɫ
ftext = font.render(text, True, (65, 83, 130),(255, 255, 255))
#����ͼƬ
pygame.image.save(ftext, "D:/pythontab.jpg")#ͼƬ�����ַ