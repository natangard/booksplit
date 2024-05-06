import os
import nltk
from nltk.tokenize import sent_tokenize

# Убедимся, что библиотека NLTK загружена
nltk.download('punkt')

def ensure_directories_exist():
    # Создаем папки 'input' и 'output', если они не существуют
    for directory in ['input', 'output']:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Создана папка '{directory}'. Пожалуйста, добавьте файлы для обработки в папку 'input'.")

def split_sentences(input_file, output_file):
    # Читаем текстовый файл
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Разделяем текст на предложения
    sentences = sent_tokenize(text)

    # Записываем предложения в новый файл, каждое с новой строки
    with open(output_file, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(sentence + '\n')

def choose_file():
    # Список файлов в папке 'input'
    files = os.listdir('input')
    files = [file for file in files if os.path.isfile(os.path.join('input', file))]
    
    if not files:
        print("В папке 'input' нет файлов.")
        return None, None
    
    print("Доступные файлы для обработки:")
    for index, file in enumerate(files):
        print(f"{index + 1}: {file}")

    while True:
        try:
            file_index = int(input("Выберите номер файла для обработки: ")) - 1
            if 0 <= file_index < len(files):
                input_file = os.path.join('input', files[file_index])
                output_file = os.path.join('output', f"{files[file_index]}_sentences.txt")
                return input_file, output_file
            else:
                print("Неверный ввод. Пожалуйста, введите номер из списка.")
        except ValueError:
            print("Пожалуйста, введите корректный номер файла.")

if __name__ == "__main__":
    ensure_directories_exist()
    input_file, output_file = choose_file()
    if input_file and output_file:
        split_sentences(input_file, output_file)
        print(f"Обработка завершена. Файл сохранен в '{output_file}'.")
    else:
        print("Операция отменена.")

