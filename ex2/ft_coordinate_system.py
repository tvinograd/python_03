#!/usr/bin/env python3
"""Demonstrates tuple usage."""


import math


def calculate_distance(pos: tuple) -> float:
    """Calculate Euclidean distance from (0, 0, 0)."""
    x, y, z = pos
    dist = math.sqrt((x)**2 + (y)**2 + (z)**2)
    print(f"Distance between (0, 0, 0) and {pos}: {dist:.2f}\n")
    return dist


def ft_coordinate_system(pos: tuple | str) -> None:
    """Main demonstration of 3D coordinate system using tuples."""

    # If it's already a tuple:
    if isinstance(pos, tuple):
        print(f"Position created: {pos}")
        calculate_distance(pos)
        return

    # If it's a string:
    print(f"Parsing coordinates: \"{pos}\"")
    try:
        splitted = pos.split(',')
        parsed_tuple = (int(splitted[0]), int(splitted[1]), int(splitted[2]))
        print(f"Parsed position: {parsed_tuple}")
        calculate_distance(parsed_tuple)
        return parsed_tuple
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
        return


def demonstrate_unpacking(pos: tuple) -> None:
    """Demonstrate tuple unpacking."""
    x, y, z = pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    ft_coordinate_system((10, 20, 5))
    parsed_pos = ft_coordinate_system("3,4,0")
    ft_coordinate_system("abc,def,ghi")

    print("Unpacking demonstration:")
    if parsed_pos:
        demonstrate_unpacking(parsed_pos)
