import os

import typer
from typing_extensions import Annotated


def main(
    file: str,
    bytes: Annotated[bool, typer.Option("-c", help="return bytes of file provided.")] = False
):
    """
    unix wc tool written in python
    """
    
    if bytes:
        try:
            print(f"{get_byte_count(file)} {file}")
        except(FileNotFoundError):
            print(f"file {file} not found")

def get_byte_count(file):
    byte_count = 0

    with open(file, 'rb') as file:
        for line in file:
            byte_count += len(line)

    return byte_count

if __name__ == "__main__":
    typer.run(main)