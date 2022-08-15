from multiprocessing import Event
from typing import Set, Iterable, Any
from numpy import isin

from tcod.context import Context
from tcod.console import Console
from actions import EscapeAction, MovementAction
from entity import Entity
from inputHandlers import EventHandler

"""
Engine to handle drawing of game map and entities residing within.
"""
class Engine:
    """
    entities:       enforces unique entities inside a set
    eventHandler:   handles events ingame
    player:         player entity due to requiring instance 
                    more than other entities in set
    """
    def __init__(self, entities: Set[Entity], eventHandler: EventHandler, player: Entity):
        self.entities = entities
        self.eventHandler = eventHandler
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            # Dispatch action made to our event_handler instance for processing
            action = self.eventHandler.dispatch(event)

            # Skip loop if key pressed is not recognised within event.
            if action is None:
                continue
            # Check if action sourced from event handler is a movement, and move player by distance stored if true.
            if isinstance(action, MovementAction):
                self.player.move(dx = action.dx, dy=action.dy)

            # Close program if escape action is confirmed.
            elif isinstance(action, EscapeAction):
                raise SystemExit()

    def render(self, console: Console, context: Context) -> None:
        # Print all entities to their game locations and present onto context.v
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()