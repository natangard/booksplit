import os
import time
from openai import OpenAI


def read_api_key():
    with open("secrets", "r") as file:
        return file.read().strip()


# Чтение ключа API из файла secrets
api_key = read_api_key()
client = OpenAI(api_key=api_key)


def choose_file():
    # Список файлов в текущей директории
    files = os.listdir('.')
    files = [file for file in files if os.path.isfile(file)]

    if not files:
        print("No files found in the current directory.")
        return None

    print("Available files for processing:")
    for index, file in enumerate(files):
        print(f"{index + 1}: {file}")

    while True:
        try:
            file_index = int(input("Select the file number to process: ")) - 1
            if 0 <= file_index < len(files):
                return files[file_index]
            else:
                print("Invalid input. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid file number.")


def translate_to_german(prompt, temperature=0.7, max_tokens=100):
    response = client.completions.create(model="davinci-002", prompt=prompt)
    return response.choices[0].text.strip()


def translate_file(input_file):
    output_file = input_file.replace('.txt', '_translated.txt')

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translated_lines = []
    counter = 0
    max_tokens_per_minute = 250000
    max_requests_per_minute = 3000
    request_interval = 60 / max_requests_per_minute  # Calculate the interval between requests

    for line in lines:
        # Переводим строку с русского на немецкий
        translated_line = translate_to_german(f"Übersetze den Satz von Russisch nach Deutsch: {line}")
        translated_lines.append(line.strip() + '\n' + translated_line.strip() + '\n')

        counter += len(line.split())  # Учитываем количество токенов в строке
        if counter >= max_tokens_per_minute:
            print("Достигнут лимит токенов, приостанавливаемся...")
            time.sleep(60)  # Пауза на 1 минуту
            counter = 0  # Сбрасываем счетчик
        elif len(translated_lines) >= max_requests_per_minute:
            print("Достигнут лимит запросов, приостанавливаемся...")
            time.sleep(60)  # Пауза на 1 минуту
        print(line.strip() + '\n' + translated_line.strip() + '\n')

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(translated_lines)

    print(f"Перевод завершен. Переведенный текст сохранен в файле '{output_file}'.")


if __name__ == "__main__":
    input_file = choose_file()
    if input_file:
        translate_file(input_file)
