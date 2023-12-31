# Python Word Count (wc) Tool

This is a Python command-line tool that performs word counting operations similar to the Unix `wc` command. It counts the number of lines, words, characters, and bytes in a given file.

## Features

- Count the number of lines in a file.
- Calculate the total number of words in a file.
- Determine the number of characters (including whitespace) in a file.
- Calculate the size of the file in bytes.

## Usage

### Installation

This tool does not require any special installation steps. 
- Make sure you have poetry installed
- clone the repo and check out to it
- run poetry install
- then poetry shell - this will activate a virtualenv

### Usage Syntax

```bash
python wc_tool.py [OPTIONS] [FILE]
```

### Options

    -c, --bytes: Return the number of bytes in the file.
    -l, --lines: Return the number of lines in the file.
    -w, --words: Return the number of words in the file.
    -m, --chars: Return the number of characters in the file.
    --help: Display help and usage instructions.

### Examples

Count lines in a file:

```bash
python wc_tool.py -l filename.txt
```

Count words in a file:

```bash
python wc_tool.py -w filename.txt
```

Count bytes in a file:

```bash
python wc_tool.py -c filename.txt
```

Count characters in a file:

```bash
python wc_tool.py -m filename.txt
```

Note
    If no option is specified, it will return the total count of lines, words, and bytes.
