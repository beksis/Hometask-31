from concurrent.futures import ThreadPoolExecutor
import time


def red_light():
    print("Запрещающий красный цвет")
    time.sleep(4)


def yellow_light():
    print("Предупреждающий желтый цвет")
    time.sleep(6)


def green_light():
    print("Разрешающий зеленый цвет")
    time.sleep(5)


def multithreading_traffic_light():
    with ThreadPoolExecutor(max_workers=3) as executor:
        while True:
            executor.submit(red_light)
            executor.submit(yellow_light)
            executor.submit(green_light)


# Вызов функции
multithreading_traffic_light()
