#!/usr/bin/env python3
"""Demonstrates how programs receive and process command-line arguments."""


import sys


def ft_command_quest() -> None:
    """Display command-line arguments in a user-friendly format."""
    print("=== Command Quest ===")

    total_args = len(sys.argv)
    user_args = total_args - 1

    if user_args == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {user_args}")
        for i in range(1, total_args):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    ft_command_quest()

"""
Testing examples:
python3 ft_command_quest.py
python3 ft_command_quest.py hello world 42
python3 ft_command_quest.py "Data Quest"
"""
