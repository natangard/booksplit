# Sentence Splitter for Text Books

This project is a Python script that processes the text of a book and divides it into sentences. Each sentence is output on a new line in a text file. This can be useful for linguistic research, text processing, and for creating training systems that need to work with individual sentences.

## Features

- Input of book text in TXT format (support for FB2 and EPUB is planned in future updates).
- Splitting the text into sentences.
- Outputting each sentence on a new line in the resulting text file.

## Technologies

The project is developed using Python 3.8 and the `nltk` library for natural language processing.

## Installation and Usage

To use the script, first install the dependencies:

pip install nltk

To split a book into sentences, run:

python sentence_splitter.py <path_to_book_file.txt>

The output file will be saved in the same directory as the input file, with a `_sentences` suffix added.

## License

The project is distributed under the MIT license.

# Разделитель предложений для текстовых книг

Этот проект представляет собой скрипт на Python, который анализирует текст книги и разделяет его на предложения. Каждое предложение выводится на новой строке в текстовом файле. Это может быть полезно для лингвистических исследований, обработки текстов и для создания систем обучения с подкреплением, которым необходимо работать с отдельными предложениями.

## Особенности

- Ввод текста книги в формате TXT (поддержка FB2 и EPUB планируется в будущих обновлениях).
- Разбиение текста на предложения.
- Вывод каждого предложения на новой строке в выходном текстовом файле.

## Технологии

Проект разработан с использованием Python 3.8 и библиотеки `nltk` для обработки естественного языка.

## Установка и использование

Для использования скрипта необходимо сначала установить зависимости:

pip install nltk

Для разделения книги на предложения выполните:

python sentence_splitter.py <путь_к_файлу_книги.txt>

Выходной файл будет сохранен в той же директории, что и входной файл, с добавлением суффикса `_sentences`.

## Лицензия

Проект распространяется под лицензией MIT.
