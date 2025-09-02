# Reebog world maze solution

This follows the right wall up to a goal.
It starts by moving up to a wall to avoid being stuck in a no wall start scenario.

```
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()

while not at_goal():
    
    if wall_on_right() and not wall_in_front():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    else:
        turn_right()
        move()
```