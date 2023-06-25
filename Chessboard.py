import tkinter as tk
from typing import Dict, Tuple, Union, Callable

class Chessboard:
    '''This class builds a simple chessboard'''
    def __init__(self,
                 master :Union[tk.Tk,tk.Frame,tk.Toplevel],
                 rows   :int = 8,
                 cols   :int = 8,
                 width  :int = 800,
                 height :int = 500,
                ):
        """
        Initialize the chessboard. The variable `canvas` is stored in self.canvas.

        :param master: The container in which the canvas is stored.
        :param rows: The number of rows in the chessboard. Defaults to 8.
        :param cols: The number of columns in the chessboard. Defaults to 8.
        :param width: The width of the canvas. Defaults to 800.
        :param height: The height of the canvas. Defaults to 500.
        """
        self._ROWS = rows
        self._COLS = cols
        self._WIDTH = width
        self._HEIGHT = height
        self._master = master
        self.canvas = tk.Canvas(master, width=width, height=height)
        self.canvas.pack()
        self.pieces:Dict[Tuple[int,int], Tuple[int,str]] = {}
        self.draw_board()
    
    def draw_board(self) -> None:
        """
        Draw the chessboard in the canvas, which will be executed for you at the same time as initialization.
        """
        self._CELL_WIDTH  = self._WIDTH  * 0.8 / self._COLS
        self._CELL_HEIGHT = self._HEIGHT * 0.8 / self._ROWS
        self._X_OFFSET = (self._WIDTH  - self._CELL_WIDTH  * (self._COLS-1)) / 2
        self._Y_OFFSET = (self._HEIGHT - self._CELL_HEIGHT * (self._ROWS-1)) / 2
        self._PIECE_SIZE = min(self._CELL_WIDTH/2.1,self._CELL_HEIGHT/2.1)
        for i in range(self._COLS):
            self.canvas.create_line(
                self._X_OFFSET + self._CELL_WIDTH *i,
                self._Y_OFFSET,
                self._X_OFFSET + self._CELL_WIDTH *i,
                self._Y_OFFSET + self._CELL_HEIGHT*(self._ROWS-1),
                fill='black'
            )
        for j in range(self._ROWS):
            self.canvas.create_line(
                self._X_OFFSET,
                self._Y_OFFSET + self._CELL_HEIGHT*j,
                self._X_OFFSET + self._CELL_WIDTH *(self._COLS-1),
                self._Y_OFFSET + self._CELL_HEIGHT*j,
                fill='black'
            )
    
    def put_piece(self, row:int, col:int, color:str='black', overwrite:bool=True) -> None:
        """
        This method adds a piece of the specified color at the position `(row, col)` on the chessboard.

        :param row: The row index.
        :param col: The column index.
        :param color: The color of the piece to add. Defaults to 'black'
        :return: None
        """
        piece = self.pieces.get((row,col), None)
        if piece is not None and not overwrite:
            return
        if piece is not None and piece[1] != color:
            self.del_piece(row, col)
        x_pos = self._X_OFFSET + self._CELL_WIDTH *col
        y_pos = self._Y_OFFSET + self._CELL_HEIGHT*row
        piece_id = self.canvas.create_oval(
            x_pos - self._PIECE_SIZE,
            y_pos - self._PIECE_SIZE,
            x_pos + self._PIECE_SIZE,
            y_pos + self._PIECE_SIZE,
            fill = color
        )
        self.pieces[(row, col)] = (piece_id, color)
    
    def del_piece(self, row:int, col:int):
        """
        This method removes the piece at the position `(row, col)` from the chessboard, if there is any.

        :param row: The row index.
        :param col: The column index.
        :return: None
        """
        piece = self.pieces.pop((row, col), None)
        if piece is not None:
            self.canvas.delete(piece[0])
    
    def mov_piece(self,
                  from_row: int,
                  from_col: int,
                  to_row : int,
                  to_col : int,
                 ):
        """
        This method moves the chess piece from the position `(from_row, from_col)` to the position `(to_row, to_col)`.

        :param from_row: The row index.
        :param from_col: The column index.
        :param to_row: The target row index.
        :param to_col: The target column index.
        :return: None
        """
        if (from_row, from_col) in self.pieces:
            piece_id, color = self.pieces[(from_row, from_col)]
            del self.pieces[(from_row, from_col)]
            self.canvas.delete(piece_id)
            self.put_piece(to_row, to_col, color)

    def bind_press(self, function:Callable[[int, int, str], None], always_call: bool = False) -> None:
        """
        Bind a mouse click event on the chessboard. When a chess piece is clicked, call the
        function `function(row: int, col: int, color: str)`. Arguments row and col
        represent the position of the clicked piece, color is the color of the chess piece.

        If there is no chess piece on the clicked position and `always_call` is true, call the function
        with an empty color string.

        :param function: The function to call when a chess piece is clicked.
        :param always_call: Whether or not to always call the function, even when there is no chess piece on
                            the clicked position.
        :return: None
        """
        def press(event):
            col = int((event.x - self._X_OFFSET + self._CELL_WIDTH /2) // self._CELL_WIDTH)
            row = int((event.y - self._Y_OFFSET + self._CELL_HEIGHT/2) // self._CELL_HEIGHT)
            if (row, col) in self.pieces:
                _, color = self.pieces[(row, col)]
                function(row, col, color)
            elif always_call:
                function(row, col, "")

        self.canvas.bind('<Button-1>', press)

    def add_point(self, row:int, col:int, color:str, r:int=1) -> int:
        """
        This method adds a circular marker with a specified radius(r) and color on position `(row, col)`
        of the chessboard. Returns an id for the created marker.

        :param row: The row index of the marker.
        :param col: The column index of the marker.
        :param color: The color of the marker.
        :param r: The radius of the marker. Defaults to 1.
        :return: An id for the created marker.
        """
        x_pos = self._X_OFFSET + self._CELL_WIDTH *col
        y_pos = self._Y_OFFSET + self._CELL_HEIGHT*row
        size  = self._PIECE_SIZE * r
        return self.canvas.create_oval(
            x_pos - size,
            y_pos - size,
            x_pos + size,
            y_pos + size,
            fill = color
        )

    def get_point(self, row:int, col:int) -> Tuple[float,float]:
        """
        This method returns the coordinates (x, y in pixels) of the point in the chessboard cell
        located at position `(row, col)`.

        :param row: The row index of the point.
        :param col: The column index of the point.
        :return: A tuple of the (x, y) coordinates in pixels.
        """
        return (
            self._X_OFFSET + self._CELL_WIDTH *col,
            self._Y_OFFSET + self._CELL_HEIGHT*row
        )