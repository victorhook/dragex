import tkinter as tk

from . import styles


class Frame(tk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, **styles.frames)


class Button(tk.Button):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, **styles.buttons)


class Label(tk.Label):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, **styles.labels)


class Entry(tk.Entry):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, **styles.entry)
