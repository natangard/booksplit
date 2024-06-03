import os
import nltk
from nltk.tokenize import sent_tokenize
import ebooklib
from ebooklib import epub
from xml.etree import ElementTree as ET

# Ensure that the NLTK library is loaded
nltk.download('punkt')

# Create the 'input' directory if it doesn't exist
if not os.path.exists('input'):
    os.makedirs('input')


def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_fb2(file_path):
    ns = {'fb': 'http://www.gribuser.ru/xml/fictionbook/2.0'}
    tree = ET.parse(file_path)
    root = tree.getroot()
    sections = root.findall('.//fb:body//fb:p', namespaces=ns)
    return ' '.join(section.text for section in sections if section.text)


def read_epub(file_path):
    book = epub.read_epub(file_path)
    content = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content.append(item.content.decode('utf-8'))
    return ' '.join(content)


def choose_file():
    # List files in the 'input' directory
    files = os.listdir('input')
    files = [file for file in files if os.path.isfile(os.path.join('input', file))]

    if not files:
        print("No files in the 'input' directory.")
        return None, None

    print("Available files for processing:")
    for index, file in enumerate(files):
        print(f"{index + 1}: {file}")

    while True:
        try:
            file_index = int(input("Select the file number for processing: ")) - 1
            if 0 <= file_index < len(files):
                input_file = os.path.join('input', files[file_index])
                output_file = os.path.join('output', f"{files[file_index]}_sentences.txt")
                return input_file, output_file
            else:
                print("Invalid input. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid file number.")


def split_sentences(input_file, output_file):
    file_extension = os.path.splitext(input_file)[1].lower()
    if file_extension == '.txt':
        text = read_txt(input_file)
    elif file_extension == '.fb2':
        text = read_fb2(input_file)
    elif file_extension == '.epub':
        text = read_epub(input_file)
    else:
        print("File format not supported.")
        return

    sentences = sent_tokenize(text)
    with open(output_file, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(sentence + '\n')


if __name__ == "__main__":
    input_file, output_file = choose_file()
    if input_file and output_file:
        split_sentences(input_file, output_file)
        print(f"Processing completed. File saved as '{output_file}'.")
