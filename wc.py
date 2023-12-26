import os

import typer
from typing_extensions import Annotated


def main(
    file: str,
    n_bytes: Annotated[bool, typer.Option("-c", help="return bytes of file provided.")] = False,
    lines: Annotated[bool, typer.Option("-l", help="return number of lines in the file provided")] = False,
    words: Annotated[bool, typer.Option("-w", help="return number of words in the file provided")] = False,
    chars: Annotated[bool, typer.Option("-m", help="return number of characters in the file provided")] = False,
):
    """
    unix wc tool written in python
    """
    if not os.path.exists(file):
        print(f"file {file} not found")
    msg = ""

    if n_bytes:
        msg += f"{get_byte_count(file)} "
    if lines:
        msg += f"{get_line_count(file)} "
    if words:
        msg += f"{get_word_count(file)} "
    if chars:
        msg += f"{get_char_count(file)} "
    
    if (not n_bytes or not lines or not words or not chars):
        pass
    
    if msg != "":
        print(f"{msg}{file}")

def get_byte_count(file):
    byte_count = 0

    with open(file, 'rb') as file:
        for line in file:
            byte_count += len(line)

    return byte_count

def get_line_count(file):
    with open(file, 'r') as file:
        line_count = sum(1 for _ in file)
    
    return line_count

def get_word_count(file):
    with open(file, 'r') as file:
        word_count = sum(len(line.split()) for line in file)

    return word_count

def get_char_count(file):
    with open(file, 'r', encoding='utf-8-sig') as file:
        char_count = sum(len(line) for line in file)

    return char_count

if __name__ == "__main__":
    typer.run(main)