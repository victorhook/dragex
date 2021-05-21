from ui import basemodels

try:
    from .filehandler import FileHandler
except:
    from filehandler import FileHandler


class Config:

    def __init__(self):
        self.k = 2
        self.f = 2.0
        self.name = 'asds'


class Param(basemodels.Frame):
    """ Represents a single parameter.
        The type can be: String, int, float.
    """

    def __init__(self, master, name: str, value: object):
        super().__init__(master)
        self.name = name

        self.label = basemodels.Label(self, text=name, width=15, anchor='w')
        self.param_type = type(value)

        if self.param_type is int:
            self.input = basemodels.Slider(self, orient=tk.HORIZONTAL)
            self.input.set(value)
        elif self.param_type is float:
            self.input = basemodels.Slider(self, orient=tk.HORIZONTAL,
                                           resolution=0.1)
            self.input.set(value)
        else:
            self.input = basemodels.Entry(self, width=10)

        self.label.grid(row=0, column=0, pady=5)
        self.input.grid(row=0, column=1, pady=5)

    def write(self, value: str) -> None:
        """ Writes the value. """
        if self.param_type is str:
            self.entry.delete(0, tk.LAST)
            self.entry.insert(0, value)

    def read(self) -> tuple:
        """ Returns a tuple of (name, value). """
        if self.param_type is int:
            value = self.input.get()
        elif self.param_type is float:
            value = self.input.get()
        else:
            value = self.input.get()

        return self.name, value


class UiConfig(basemodels.Frame):
    """ This class can be used to easly configure parameters.

        all non-private, non-magic attributes of config will
        be parametrized which can be configured and saved to disk.
    """

    def __init__(self, master, config: Config):
        super().__init__(master)
        self.fh = FileHandler()
        self.config = config
        self.conf_name = self.config.__class__.__name__

        self._frame = basemodels.Frame(self)
        self.params = []

        # If the config already exist, read the content from it.
        if self.fh.file_exists(self.conf_name):
            data = self.fh.open(self.conf_name, is_json=True)
            for k, v in data.items():
                setattr(config, k, v)

        # Fill the parameters with the config data.
        for attr in filter(lambda atr: not atr.startswith('_'), dir(config)):
            val = getattr(config, attr)
            param = Param(self._frame, attr, val)
            param.pack()
            self.params.append(param)

        self._btn_save = basemodels.Button(self, text='Save',
                                           command=self._save)

        self._frame.pack()
        self._btn_save.pack()

    def _save(self):
        """ Saves the parameter values to disk, using the name of the
            config class as filename.
        """
        conf = {}
        for param in self.params:
            name, value = param.read()
            conf[name] = value

        self.fh.save(self.conf_name, conf)


if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    conf = Config()
    ui = UiConfig(root, conf)

    ui.pack()
    root.mainloop()