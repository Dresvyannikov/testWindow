# -*- coding: utf-8 -*-
__author__ = "DresvyannikovEO"
__version__ = "0.0.1"
import logging

import pygame

# # Сообщение отладочное
# logging.debug( u'This is a debug message' )
# # Сообщение информационное
# logging.info( u'This is an info message' )
# # Сообщение предупреждение
# logging.warning( u'This is a warning' )
# # Сообщение ошибки
# logging.error( u'This is an error message' )
# # Сообщение критическое
# logging.critical( u'FATAL!!!' )

log = logging.basicConfig(level=logging.DEBUG, format=u"(levelname)-8s [%(asctime)s] %(message)s",
                          filename=u"window.log")

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)  # создание окна с параметрами.
#  depth - глубина цвета
pygame.display.set_caption("First window for WINDOWS")  # заголовок окна
helloText = "This text for window/ HELLO .!."
(x, y, fontSize) = (10, 40, 14)  # координаты положения текста по осям и его размер
myFont = pygame.font.SysFont("None", fontSize)  # создали стандортный шрифт
fontColor = (255, 255, 0)  # цвет шрифта в RGB
bgColor = (0, 0, 0)  # цвет фона в RGB
# надо преобразовать в изображение и лишь только потом рисовать это изображение в окне, для хранения
#  изображения мы определим переменную с именем fontImage а метод объекта myFont,
# который преобразует текст в картинку выглядит следующим образом -
# render(text, antialias, color, background=None), где text – текст,
# antialias – сглаживание шрифта, color – цвет текста, background – цвет фона (не обязательный параметр)
fontImage = myFont.render(helloText, 0, (fontColor))
mainLoop = True  # создание флага цикла отображение кадров
while mainLoop:
    for event in pygame.event.get():  # формируем интерпретатор event, который проходим по списку и формирует событие
        logging.info(event)
        logging.info(event.type)
        #  по методу pygame.event.get()
        if event.type == 12:  # если событие выхода, то выходим из цикла
            mainLoop = False
        screen.fill(bgColor)  # сформировали кадр и залили его цветом
        screen.blit(fontImage, (x, y))  # вставляем текст в окно
        pygame.display.update()
pygame.quit()

