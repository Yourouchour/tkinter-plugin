# Tkinter Plugin

tkinter-plugin is a Python module that contains several plugins that make Python programming more convenient.

## How to use:

### paintbrush

Paintbrush is a Python module that creates a paintbrush object used for drawing on a Tkinter canvas. You can customize the color and width of the brush to draw better graphics.


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

## Method:

### paintbrush

* `__init__(self, canvas: eztk.Canvas, color='black', width=1)` - initialize the Paintbrush object with a canvas, color, and width.
* `undo(self, n=1)` - undo a specified number of drawing operations
* `clear(self)` - clear all drawing operations
* `_start(self, event: tk.Event)` - begin a drawing operation
* `_duration(self, event: tk.Event)` - continue a drawing operation
* `_end(self, event: tk.Event)` - end a drawing operation

Note: the methods `_start`, `_duration`, and `_end` are for internal use only and should not be called directly.
