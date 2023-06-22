import tkinter as tk
from typing import List, Tuple

class Paintbrush:
    def __init__(self, canvas:tk.Canvas, color='black', width=1):
        '''
        Initialize the paintbrush and bind mouse events to the canvas.

        :param canvas: canvas object
        :param color: paintbrush color, default is black
        :param width: paintbrush width, default is 1
        '''
        canvas.bind("<B1-Motion>",self._duration)
        canvas.bind("<ButtonPress-1>",self._start)
        canvas.bind("<ButtonRelease-1>",self._end)
        self._logs:List[Tuple[int,int]] = []
        self._canvas = canvas
        self.color = color
        '''Paintbrush color'''

        self.width = width
        '''Paintbrush width'''

    def undo(self, n=1):
        '''
        Undo the specified amount of operations.

        :param n: number of operations to undo, default is 1
        '''
        if n >= len(self._logs):
            self.clear()
        else:
            for _ in range(n):
                start_id, end_id = self._logs.pop()
                for i in range(start_id,end_id+1):
                    self._canvas.delete(i)

    def clear(self):
        '''
        Clear all operations.
        '''
        for start_id, end_id in self._logs:
            for i in range(start_id,end_id+1):
                self._canvas.delete(i)
        self._logs = []

    def _start(self, event:tk.Event):
        self._end_x = event.x
        self._end_y = event.y

        # Only record the id here.
        self._start_id = self._canvas.create_oval(self._end_x,self._end_y,self._end_x,self._end_y,fill=self.color)
        self._end_id = self._start_id

    def _duration(self, event:tk.Event):
        self._start_x = event.x
        self._start_y = event.y
        self._canvas.create_line(self._end_x,self._end_y,self._start_x,self._start_y,fill=self.color,width=self.width)
        self._end_id += 1
        self._end_x = self._start_x
        self._end_y = self._start_y

    def _end(self, event:tk.Event):
        self._logs.append((self._start_id,self._end_id))
