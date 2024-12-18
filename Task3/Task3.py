import json
import sys

def fill_values(tests, values):
    for test in tests:
        if 'id' in test:
            for value_item in values:
                if value_item['id'] == test['id']:
                    test['value'] = value_item['value']
                    break
        if 'values' in test:
            fill_values(test['values'], values)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python script.py <файл_values.json> <файл_tests.json> <файл_report.json>")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    try:
        with open(values_file, 'r') as f:
            values_data = json.load(f)
            values = values_data['values']

        with open(tests_file, 'r') as f:
            tests_data = json.load(f)
            tests = tests_data['tests']

        fill_values(tests, values)

        with open(report_file, 'w') as f:
            json.dump(tests_data, f, indent=2)

    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {sys.exc_info()[1]}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Ошибка: неверный формат JSON файла: {sys.exc_info()[1]}")
        sys.exit(1)
    except KeyError as e:
      print(f"Ошибка: ключ не найден в JSON данных: {e}")
      sys.exit(1)
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        sys.exit(1)