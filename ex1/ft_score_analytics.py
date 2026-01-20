#!/usr/bin/env python3
"""Demonstrates list usage."""


import sys


def ft_score_analytics() -> None:
    """Display command-line arguments."""
    print("=== Player Score Analytics ===")

    total_args = len(sys.argv)
    user_args = total_args - 1

    if user_args == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")

    else:
        scores = []
        for arg in sys.argv[1:]:
            try:
                score = int(arg)
                scores.append(score)
            except ValueError:
                print(f"Warning: '{arg}' is not a valid number (skipped)")

        if scores:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        else:
            print("No valid scores to analyze.")


if __name__ == "__main__":
    ft_score_analytics()

"""
Testing examples:
python3 ft_score_analytics.py 1500 2300 1800 2100 1950
python3 ft_score_analytics.py
"""
