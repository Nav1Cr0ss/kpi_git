import os
import sys
import json
import re


def example1():
    # Виправлено: Перевірка на нуль перед поділом
    a = 10
    b = 2
    if b == 0:
        print("Division by zero error")
    else:
        result = a / b
        print(result)


def example2():
    # Виправлено: Використання 'with' для автоматичного закриття файлу
    try:
        with open("data.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Error reading file")


def example3():
    # Виправлено: Використання вбудованої функції sum() для підсумовування
    data = [1, 2, 3, 4, 5]
    total = sum(data)
    print(total)


def example4():
    # Виправлено: Скорочення довгих рядків
    long_string = "This is a very long string which exceeds the acceptable length"
    if len(long_string) > 10:
        print("String is too long")


def example5():
    # Виправлено: Заміна застарілого методу has_key() на 'in'
    old_dict = {"key": "value"}
    if "key" in old_dict:
        print("Key exists")


def example6():
    # Виправлено: Закриття файлу в блоці 'with' для обробки ресурсів
    try:
        with open("somefile.txt", "r") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("File not found")
        return None


def example7(data: int = None):
    # Виправлено: Правильне порівняння None
    if data is None:  # Правильне порівняння з None
        print("Data is None")
    else:
        print("Data is not None")


def example11():
    # Виправлено: Покращено використання регулярних виразів
    pattern = r"\d{4}-\d{2}-\d{2}"
    result = re.findall(pattern, "2025-02-09 2025-13-02")
    print(result)


def example12():
    # Виправлено: Вирішення проблеми з багатопоточністю за допомогою Lock
    import threading
    shared_var = 0
    lock = threading.Lock()

    def increment():
        nonlocal shared_var
        with lock:
            shared_var += 1

    threads = []
    for _ in range(10):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(shared_var)



# Виклик усіх функцій для демонстрації
example1()
example2()
example3()
example4()
example5()
example6()
example7()
example11()
example12()
