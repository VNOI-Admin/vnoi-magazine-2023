import os
import subprocess

def format_cpp(content):
    return subprocess.run(
            ['clang-format'],
            shell=True, check=True,
            input=content, encoding='utf-8',
            capture_output=True, text=True
            ).stdout
