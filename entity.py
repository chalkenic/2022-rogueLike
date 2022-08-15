from typing import Tuple

class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        # X and Y define the entity's co-ordinates.
        self.x = x
        self.y = y
        # Symbol to define the entity.
        self.char = char
        # Colour of entity, defined by RGB colours (3 integers).
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy