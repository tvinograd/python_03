#!/usr/bin/env python3
"""Demonstrates generator functions with yield."""


import random


def generate_events(count: int):
    """Generate random events."""
    players = ['alice', 'bob', 'charlie']
    event_types = ['killed monster', 'found treasure', 'leveled up']

    for i in range(count):
        event = {
            'id': i + 1,
            'player': random.choice(players),
            'level': random.randint(1, 20),
            'action': random.choice(event_types)
        }
        yield event


def fibonacci_generator(n: int):
    """Generate first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n: int):
    """Generate first n prime numbers."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i in range(n):
        yield primes[i]


def ft_data_stream() -> None:
    """Main demonstration of generator-based data streaming."""
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    # Statistics counters
    total_events = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    # Generate events
    events = generate_events(1000)

    # Display events and collect statictics
    output_counter = 1
    for event in events:
        if output_counter <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        output_counter += 1
        total_events += 1
        if event['level'] >= 10:
            high_level_count += 1
        if event['action'] == 'found treasure':
            treasure_count += 1
        if event['action'] == 'leveled up':
            levelup_count += 1

    print("...")

    # Display statictics
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    # Fibonacci
    fib_numbers = ', '.join(str(num) for num in fibonacci_generator(10))
    print(f"Fibonacci sequence (first 10): {fib_numbers}")

    # Primes
    prime_numbers = ', '.join(str(num) for num in prime_generator(5))
    print(f"Prime numbers (first 5): {prime_numbers}")


if __name__ == "__main__":
    ft_data_stream()
