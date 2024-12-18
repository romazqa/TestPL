import sys


def circular_path(n, m):
    arr = [i for i in range(1, n + 1)]
    path = []
    current_index = 0

    while arr[current_index] not in path:
        path.append(arr[current_index])
        current_index = (current_index + m - 1) % n

    return "".join(map(str, path))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py <n> <m>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        if n < 1 or m < 1:
            raise ValueError("n и m должны быть положительными целыми числами.")

    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

    result = circular_path(n, m)
    print(result)
