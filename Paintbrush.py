import tkinter as tk
from typing import List, Tuple

class Paintbrush:
    def __init__(self, canvas:tk.Canvas, color='black', width=1):
        '''
        初始化画笔，并且将画布绑定鼠标事件

        :param canvas: 画布对象
        :param color: 画笔颜色，默认为黑色
        :param width: 画笔宽度，默认为1
        '''
        canvas.bind("<B1-Motion>",self._duration)
        canvas.bind("<ButtonPress-1>",self._start)
        canvas.bind("<ButtonRelease-1>",self._end)
        self._logs:List[Tuple[int,int]] = []
        self._canvas = canvas
        self.color = color
        '''画笔颜色'''

        self.width = width
        '''画笔宽度'''

    def undo(self, n=1):
        '''
        撤销指定次数的操作

        :param n: 要撤销的次数，默认为1
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
        清空所有的操作
        '''
        for start_id, end_id in self._logs:
            for i in range(start_id,end_id+1):
                self._canvas.delete(i)
        self._logs = []

    def _start(self, event:tk.Event):
        self._end_x = event.x
        self._end_y = event.y

        #这里只是记录一下id
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
