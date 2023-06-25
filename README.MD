# Tkinter Plugin

tkinter-plugin is a Python module that contains several plugins that make Python programming more convenient.

## Directory

- [Paintbrush](#Paintbrush)
- [Chessboard](#Chessboard)

## Paintbrush

Paintbrush is a Python module that creates a paintbrush object used for drawing on a Tkinter canvas. You can customize the color and width of the brush to draw better graphics.

### How to use:

1. Import paintbrush

```python
from tkinter-plugin import Paintbrush
```

2. Instantiate a Paintbrush object

```python
from tkinter import *
root = Tk()
canvas = Canvas(root,width=550,height=400)

pb = Paintbrush.Paintbrush(canvas)
```

3. Use the Paintbrush object to draw on the Canvas

```python
pb.color = 'red'
pb.wigth = 5
```

4. Undo or clear previous drawings

```python
pb.undo(n=1)
pb.clear()
```

5. When you launch mainloop, your paintbrush is ready

```python
root.mainloop()
```

### Method:

* `__init__(self, canvas: eztk.Canvas, color='black', width=1)` - initialize the Paintbrush object with a canvas, color, and width.
* `undo(self, n=1)` - undo a specified number of drawing operations
* `clear(self)` - clear all drawing operations
* `_start(self, event: tk.Event)` - begin a drawing operation
* `_duration(self, event: tk.Event)` - continue a drawing operation
* `_end(self, event: tk.Event)` - end a drawing operation

Note: the methods `_start`, `_duration`, and `_end` are for internal use only and should not be called directly.

## Chessboard

The `Chessboard` class is a simple implementation of a chessboard using the Tkinter library in Python. This class provides methods to create a chessboard with a specific number of rows and columns, add pieces to the chessboard, move pieces between cells, and more.

### How to use:

To use the `Chessboard` class, first you need to import it:

```python
from chessboard import Chessboard
```

Then, you need to create an instance of the class by calling the constructor and specifying the container where the chessboard will be displayed (`master`), the number of rows and columns (`rows` and `cols`, respectively), and the width and height of the canvas (`width` and `height`, respectively).

```python
my_chessboard = Chessboard(master, rows, cols, width, height)
```

After creating the chessboard, you can use its methods to add, move and delete chess pieces on the board.

To add a chess piece to the board, you need to call the `put_piece()` method with the row and column where the piece will be placed. You can also specify the color of the piece (black or white) as an optional parameter.

```python
my_chessboard.put_piece(row=3, col=4, color='black')
```

To move a piece from one cell to another, you should call the `mov_piece()` method with the current and target positions of the piece.

```python
my_chessboard.mov_piece(from_row=3, from_col=4, to_row=5, to_col=6)
```

To delete a piece from the board, use the `del_piece()` method and specify the row and column of the cell from which the piece will be removed.

```python
my_chessboard.del_piece(row=5, col=6)
```

It’s also possible to add markers or bind mouse click events to the chessboard using the `add_point()` and `bind_press()` methods, respectively.

### Method:

The `Chessboard` class has the following methods:

* `__init__(self, master: Union[tk.Tk, tk.Frame, tk.Toplevel], rows: int = 8, cols: int = 8, width: int = 800, height: int = 500)`: Initializes the chessboard with the specified number of rows and columns, and width and height of the canvas.
* `draw_board(self) -> None`: Draws the chessboard on the canvas.
* `put_piece(self, row: int, col: int, color: str = 'black', overwrite: bool = True) -> None`: Adds a piece of the specified color to the specified position on the chessboard.
* `mov_piece(self, from_row: int, from_col: int, to_row: int, to_col: int) -> None`: Moves the chess piece from the position `(from_row, from_col)` to the position `(to_row, to_col)`.
* `del_piece(self, row: int, col: int) -> None`: Deletes the piece at the specified position on the chessboard.
* `bind_press(self, function, always_call=False) -> None`: Binds a mouse click event on the chessboard.
* `add_point(self, row: int, col: int, color: str, r: int = 1) -> int`: Adds a marker on the specified position on the chessboard.
* `get_point(self, row: int, col: int) -> Tuple[float, float]`: Returns the coordinates in pixels of the point in the chessboard cell located at position `(row, col)`.
