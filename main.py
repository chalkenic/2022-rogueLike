#!/usr/bin/env python3
import tcod


# Import event handler for computing keystroke events.
from inputHandlers import EventHandler

# Import game rendering class.
from engine import Engine

from entity import Entity


def main() -> None:
    
    # Screen size
    screen_width = 80
    screen_height = 50


    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # event instance.
    event_handler = EventHandler()

    # Create player entity with initial position, symbol and color
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    # Create NPC entity with initial position, symbol and color
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    # Store created entities into set.
    entities = {npc, player}

    engine = Engine(entities=entities, eventHandler=event_handler, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Pitiful Pete",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console = root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()