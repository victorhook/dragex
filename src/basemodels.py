import tkinter as tk
import styles


class Frame(tk.Frame):

    def __init__(self, master):
        super().__init__(master, **styles.frames)


class Button(tk.Button):

    def __init__(self, master):
        super().__init__(master, **styles.buttons)


class Label(tk.Label):

    def __init__(self, master):
        super().__init__(master, **styles.labels)
