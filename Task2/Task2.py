import math
import sys


def read_circle_data(circle_file):
    with open('circle.txt', 'r') as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline())
        if not (-10 ** 38 <= x <= 10 ** 38 and -10 ** 38 <= y <= 10 ** 38):
            raise ValueError("Координаты должны быть в диапазоне от -10^38 до 10^38")
        if not (0 < radius <= 10 ** 38):  
            raise ValueError("Радиус должен быть больше 0 и не превышать 10^38")
    return (x, y, radius)

def read_points_data(points_file):
    points = []
    with open('points.txt', 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            if not (-10 ** 38 <= x <= 10 ** 38 and -10 ** 38 <= y <= 10 ** 38):
                raise ValueError("Координаты должны быть в диапазоне от -10^38 до 10^38")
            points.append((x, y))
            if not (1 <= len(points) <= 100):
                raise ValueError("Количество точек должно быть от 1 до 100")
    return points

def point_position_relative_to_circle(circle, point):
    cx, cy, r = circle
    px, py = point
    distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
    if distance < r:
        return 1  # Точка внутри
    elif distance == r:
        return 0  # Точка на окружности
    else:
        return 2  # Точка снаружи

def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py <файл_окружности> <файл_точек>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    try:
        circle = read_circle_data(circle_file)
        points = read_points_data(points_file)
        for point in points:
            result = point_position_relative_to_circle(circle, point)
            print(result)

    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {sys.exc_info()[1]}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка данных: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
