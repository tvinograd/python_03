#!/usr/bin/env python3
"""Demonstrates list, dict, and set comprehensions."""


def ft_analytics_dashboard() -> None:
    """Demonstrate three types of comprehensions."""
    print("=== Game Analytics Dashboard ===\n")

    # Data
    player_scores = [
        {'name': 'alice', 'score': 2300, 'achievs': 5,
         'active': True, 'region': 'north'},
        {'name': 'bob', 'score': 1800, 'achievs': 3,
         'active': True, 'region': 'east'},
        {'name': 'charlie', 'score': 2150, 'achievs': 7,
         'active': True, 'region': 'central'},
        {'name': 'diana', 'score': 2050, 'achievs': 4,
         'active': False, 'region': 'south'},
        {'name': 'diana', 'score': 2050, 'achievs': 4,
         'active': False, 'region': 'south'}
    ]

    # List comprehensions
    print("=== List Comprehension Examples ===")

    high_scorers = [p['name'] for p in player_scores if p['score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [p['score'] * 2 for p in player_scores]
    print(f"Scores doubled: {doubled_scores}")

    active_players = [p['name'] for p in player_scores if p['active']]
    print(f"Active players: {active_players}")

    # Dictionary comprehensions
    print("\n=== Dict Comprehension Examples ===")

    player_scores_map = {p['name']: p['score'] for p in player_scores}
    print(f"Player scores: {player_scores_map}")

    score_categories = {
        'high': sum(1 for p in player_scores if p['score'] > 2000),
        'medium': sum(1 for p in player_scores if 1500 <= p['score'] <= 2000),
        'low': sum(1 for p in player_scores if p['score'] < 1500)
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {p['name']: p['achievs'] for p in player_scores}
    print(f"Achievement counts: {achievement_counts}")

    # Set comprehansions
    print("\n=== Set Comprehension Examples ===")

    unique_players = {p['name'] for p in player_scores}
    print(f"Unique players: {unique_players}")

    active_regions = {p['region'] for p in player_scores if p['active']}
    print(f"Active regions: {active_regions}")

    # Combined analysis
    print("\n=== Combined Analysis ===")

    total_players = len(unique_players)
    print(f"Total players: {total_players}")

    avg_score = sum(p['score'] for p in player_scores) / len(player_scores)
    print(f"Average score: {avg_score:.1f}")


if __name__ == "__main__":
    ft_analytics_dashboard()
