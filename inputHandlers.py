
# part of Python’s type hinting system
from typing import Optional

# use tcod’s event system
import tcod.event

# import action subclasses.
from actions import Action, EscapeAction, MovementAction

# allows program to send an event to its proper method based on what type of event it is.
class EventHandler(tcod.event.EventDispatch[Action]):

    # quit program event raises systemExit method.
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
 
    # receive key press events, and return either an Action subclass, or None, if no valid key was pressed.


    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:

        # variable that will hold whatever subclass of Action we end up assigning it to.
        action: Optional[Action] = None

        # Holds the key pressed (ignores Shift/Alt/Ctrl etc).
        key = event.sym

        # Conditional based on keys entered. Arrow keys return new MovementAction classes and x/y direction.
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        # Close program if escape key is pressed.
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action