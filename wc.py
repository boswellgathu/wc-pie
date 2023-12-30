import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated


def main(
    file_path: Annotated[Optional[str], typer.Argument()] = None,
    count_bytes: Annotated[bool, typer.Option("-c", help="Return bytes of file provided.")] = False,
    count_lines: Annotated[bool, typer.Option("-l", help="Return number of lines in the file provided.")] = False,
    count_words: Annotated[bool, typer.Option("-w", help="Return number of words in the file provided.")] = False,
    count_chars: Annotated[bool, typer.Option("-m", help="Return number of characters in the file provided.")] = False,
):
    """Unix wc tool written in Python"""
    check_file_exists(file_path)
    
    message = generate_wc_message(file_path, count_bytes, count_lines, count_words, count_chars)
    
    if message:
        sys.stdout.write(message)

def check_file_exists(file_path: str):
    """Check if the file exists"""
    if file_path and not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found")

def generate_wc_message(file_path: Optional[str], count_bytes: bool, count_lines: bool, count_words: bool, count_chars: bool) -> str:
    """Generate the 'wc' message based on selected options"""
    message = ""
    if count_bytes:
        message += f"\t{get_byte_count(file_path)}"
    if count_lines:
        message += f"\t{get_line_count(file_path)}"
    if count_words:
        message += f"\t{get_word_count(file_path)}"
    if count_chars:
        message += f"\t{get_char_count(file_path)}"

    if not any([count_bytes, count_lines, count_words, count_chars]):
        bytes_count, lines_count, words_count = get_all(file_path)
        message = f"\t{lines_count}\t{words_count}\t{bytes_count} "

    if file_path:
        message += f"\t{file_path}"

    return message

def get_byte_count(file: Optional[str]) -> int:
    byte_count = 0
    if file:
        with open(file, 'rb') as file:
            for line in file:
                byte_count += len(line)
    else:
        for line in sys.stdin:
            byte_count += len(line.encode('utf-8'))

    return byte_count

def get_line_count(file: Optional[str]) -> int:
    if file:
        with open(file, 'r') as file:
            line_count = sum(1 for _ in file)
    else:
        line_count = sum(1 for _ in sys.stdin)
    
    return line_count

def get_word_count(file: Optional[str]) -> int:
    if file:
        with open(file, 'r') as file:
            word_count = sum(len(line.split()) for line in file)
    else:
        word_count = sum(len(line.split()) for line in sys.stdin)

    return word_count

def get_char_count(file: Optional[str]) -> int:
    if file:
        with open(file, 'r', encoding='utf-8-sig') as file:
            char_count = sum(len(line) for line in file)
    else:
        char_count = sum(len(line) for line in sys.stdin)

    return char_count

def get_all(file: Optional[str]) -> int:
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