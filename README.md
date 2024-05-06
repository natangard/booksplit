# Sentence Splitter for Text Books

This project is a Python script that processes the text of a book and divides it into sentences. Each sentence is output on a new line in a text file. This can be useful for linguistic research, text processing, and for creating training systems that need to work with individual sentences.

## Features

- Automatically checks for and creates necessary `input` and `output` directories.
- Interactively allows the user to select a text file from the `input` directory for processing.
- Outputs each sentence on a new line in a text file located in the `output` directory.

## Technologies

The project is developed using Python 3.8 and the `nltk` library for natural language processing.

## Directory Structure

- **input/**: Place your text files here. The script will read files from this directory.
- **output/**: Processed files will be saved here, with each sentence on a new line.

## Installation and Usage

1. **Installation**: Ensure you have Python 3.8 and install the NLTK library:
pip install nltk

2. **Running the script**:
- Run the script from your command line. The script will guide you through selecting a file from the `input` directory and will save the processed file in the `output` directory.

## License

The project is distributed under the MIT license.
