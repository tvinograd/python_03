#!/usr/bin/env python3
"""Demonstrates dictionary operations."""


import sys


def ft_inventory_system() -> None:
    """Inventory management system demonstration."""
    if len(sys.argv) <= 1:
        print("No items provided. Usage: python3 ft_inventory_system.py "
              "<key>:<value> <key>:<value>...")
        return

    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in sys.argv[1:]:
        item, quantity = arg.split(':')
        inventory.update({item: int(quantity)})
    total = sum(inventory.values())
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    for item, quantity in sorted_items:
        percentage = (quantity / total) * 100
        unit_text = "unit" if quantity == 1 else "units"
        print(f"{item}: {quantity} {unit_text} ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_item = max(inventory.items(), key=lambda x: x[1])
    least_item = min(inventory.items(), key=lambda x: x[1])
    print(f"Most abundant: {most_item[0]} ({most_item[1]} units)")
    print(f"Least abundant: {least_item[0]} ({least_item[1]} unit)")

    print("\n=== Item Categories ===")
    moderate = {item: qty for item, qty in inventory.items() if qty > 3}
    scarce = {item: qty for item, qty in inventory.items() if qty <= 3}
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock = [item for item, qty in inventory.items() if qty <= 1]
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
    print(f"'sword' qty in inventory: {inventory.get('sword')}")


if __name__ == "__main__":
    try:
        ft_inventory_system()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

"""
Testing example:
python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1
"""
