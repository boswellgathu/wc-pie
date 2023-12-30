import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated


def main(
    file: Annotated[Optional[str], typer.Argument()] = None,
    n_bytes: Annotated[bool, typer.Option("-c", help="return bytes of file provided.")] = False,
    lines: Annotated[bool, typer.Option("-l", help="return number of lines in the file provided")] = False,
    words: Annotated[bool, typer.Option("-w", help="return number of words in the file provided")] = False,
    chars: Annotated[bool, typer.Option("-m", help="return number of characters in the file provided")] = False,
):
    """
    unix wc tool written in python
    """
    
    if file and not os.path.exists(file):
        raise FileNotFoundError(f"file {file} not found")

    msg = ""

    if n_bytes:
        msg += f"\t{get_byte_count(file)}"
    if lines:
        msg += f"\t{get_line_count(file)}"
    if words:
        msg += f"\t{get_word_count(file)}"
    if chars:
        msg += f"\t{get_char_count(file)}"
    
    if (not n_bytes and not lines and not words and not chars):
        n_bytes, lines, words = get_all(file)
        msg = f"\t{lines}\t{words}\t{n_bytes} "

    if file:
        msg += f"\t{file}"

    if msg != "":
        sys.stdout.write(msg)

def get_byte_count(file):
    byte_count = 0
    if file:
        with open(file, 'rb') as file:
            for line in file:
                byte_count += len(line)
    else:
        for line in sys.stdin:
            byte_count += len(line.encode('utf-8'))

    return byte_count

def get_line_count(file):
    if file:
        with open(file, 'r') as file:
            line_count = sum(1 for _ in file)
    else:
        line_count = sum(1 for _ in sys.stdin)
    
    return line_count

def get_word_count(file):
    if file:
        with open(file, 'r') as file:
            word_count = sum(len(line.split()) for line in file)
    else:
        word_count = sum(len(line.split()) for line in sys.stdin)

    return word_count

def get_char_count(file):
    if file:
        with open(file, 'r', encoding='utf-8-sig') as file:
            char_count = sum(len(line) for line in file)
    else:
        char_count = sum(len(line) for line in sys.stdin)

    return char_count

def get_all(file):
    byte_count = 0
    word_count = 0
    line_count = 0
    if file:
        with open(file, 'rb') as file:
            for line in file:
                byte_count += len(line)
                word_count += len(line.split())
                line_count += 1
    else:
        for line in sys.stdin:
            byte_count += len(line.encode('utf-8'))
            word_count += len(line.split())
            line_count += 1
    
    return byte_count, line_count, word_count

if __name__ == "__main__":
    typer.run(main)