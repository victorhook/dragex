import tkinter as tk

from . import styles


class Frame(tk.Frame):

    def __init__(self, master, **kwargs):
        kwargs = {**styles.frames, **kwargs}
        super().__init__(master, **kwargs)


class Button(tk.Button):

    def __init__(self, master, size: int = None, no_pad: bool = False,
                 **kwargs):
        if size is not None:
            kwargs.update(styles.buttons)
            kwargs['font'] = (styles.buttons['font'][0], size)
        if no_pad:
            kwargs.pop('padx')
            kwargs.pop('pady')
        super().__init__(master, **kwargs)


class Label(tk.Label):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, **styles.labels)


class Entry(tk.Entry):

    def __init__(self, master, size: int = None, **kwargs):
        if size is not None:
            kwargs.update(styles.entry)
            kwargs['font'] = (styles.entry['font'][0], size)
        super().__init__(master, **kwargs)


class CheckButton(tk.Checkbutton):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class Slider(tk.Scale):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, **styles.scale)


class Text(tk.Text):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, **styles.labels)


class Scrollbar(tk.Scrollbar):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, **styles.frames)


class LabelFrame(tk.LabelFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, **styles.frames)
