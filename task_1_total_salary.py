'''
Перше завдання
У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії.
Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

Вимоги до завдання:
    Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
    Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
    Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
    Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.
'''
'''
Рекомендації для виконання:
    Використовуйте менеджер контексту with для читання файлів.
    Пам'ятайте про встановлення кодування при відкриті файлів 
'''
    # open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    # Кодування рядків (ASCII, UTF-8, CP1251)
    # Python за замовчуванням використовує UTF-8, в якій один символ може займати від 1 до 4 байт,
'''
    Для розділення даних у кожному рядку можна застосувати метод split(',').
    Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
    Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.
'''


def total_salary(path):
    try:
        with open(path, mode='r', encoding='UTF-8') as sal:
            # if __name__ == '__main__':
            sal_list = []
            employee_salary_list = [el.strip() for el in sal.readlines()]
            # print(employee_salary_list)
            for el in employee_salary_list:
                salaries_list = int(el.split(',')[1])
                # print(salaries_list)
                sal_list.append(salaries_list)
            total = sum(sal_list)
            # print(total)
            # length = len(sal_list)
            length = sal_list.count()
            print(length)
            average = total / length
            average = int(average)
            return total, average
    except Exception:
        print(FileNotFoundError)

total, average = total_salary(r"salary_file.txt")
total_salary(r"salary_file1.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")






