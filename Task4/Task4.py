import sys

def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = 0
    for num in nums:
        moves += abs(num - median)
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <имя_файла>")
        sys.exit(1)

    filename = sys.argv[1]
    nums = []

    try:
        with open(filename, 'r') as f:
            for line in f: 
                try:
                    num = int(line.strip()) 
                    nums.append(num)
                except ValueError:
                    print(f"Ошибка: Неверный формат данных в строке: '{line.strip()}'. Пропускаем строку.")


    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        sys.exit(1)


    result = min_moves(nums)
    print("Минимальное количество шагов: " + str(result))
