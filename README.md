# Python Games and Turtle Animations

A collection of small interactive games and drawing experiments by Farzan Rahmani. The programs use Python's standard-library `turtle` module to practice graphics, keyboard input, movement, collision logic, and procedural drawing.

## Programs

| File | Description | Interaction |
| --- | --- | --- |
| `def_snake.py` | Snake game with food, movement, and scoring | Arrow keys |
| `paddle.py` | Paddle-and-ball game with rows of colored targets | Left and right arrows |
| `FirstGame.py` | Projectile/target game | Enter launch angle and velocity in the terminal |
| `animations/circle.py`, `square.py`, `triangle.py` | Geometric drawing experiments | Run the chosen script |
| `animations/tree.py` | Tree drawing | Run the script |
| Other files in `animations/` | Additional Turtle sketches and visual experiments | Inspect the source for parameters |

## Requirements

Use Python 3 with Tk/Tkinter support and a graphical desktop. The scripts use standard-library modules; no pip dependency file is needed. Some Linux Python installations require a separate system package for Tkinter.

Check the Turtle environment with:

```sh
python -m turtle
```

## Run a Game

From the repository root:

```sh
python def_snake.py
```

Or choose another program:

```sh
python paddle.py
python animations/tree.py
```

Run one program at a time. Click the game window to give it keyboard focus; for `FirstGame.py`, keep the terminal visible for its prompts. Stop a long-running animation or game from the terminal with `Ctrl+C` if closing the graphics window does not exit cleanly.

## Project Scope

These are independent learning projects rather than a packaged game engine. Speeds, colors, positions, and drawing parameters are configured directly in each script.

## License

See [LICENSE](LICENSE) for license terms.
