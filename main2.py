# Асинхронная модель
import threading
import time


def red_light():
    print("Запрещающий красный цвет")
    time.sleep(8)


def yellow_light():
    print("Предупреждающий желтый цвет")
    time.sleep(4)


def green_light():
    print("Разрешающий зеленый цвет")
    time.sleep(5)


def asynchronous_traffic_light():
    while True:
        threading.Thread(target=red_light).start()
        threading.Thread(target=yellow_light).start()
        threading.Thread(target=green_light).start()


# Вызов функции
asynchronous_traffic_light()
