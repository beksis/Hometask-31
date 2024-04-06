# Синхронная модель
import time


def red_light():
    print("Запрещающий красный цвет")
    time.sleep(7)


def yellow_light():
    print("Предупреждающий желтый цвет")
    time.sleep(5)


def green_light():
    print("Разрешающий зеленый цвет")
    time.sleep(6)


def synchronous_traffic_light():
    while True:
        red_light()
        yellow_light()
        green_light()


# Вызов функции
synchronous_traffic_light()
