from . import basemodels
import webbrowser


class LoginScreen(basemodels.Frame):

    def __init__(self, master):
        super().__init__(master, bd=1, highlightthickness=2)

        self._container = basemodels.Frame(self, )

        # Label and inputs
        self._label_user = basemodels.Label(self._container, text='Username')
        self._label_pass = basemodels.Label(self._container, text='Password')
        self._user = basemodels.Entry(self._container)
        self._pass = basemodels.Entry(self._container)

        # Forgot password & Create account
        self._forgot_password = basemodels.Label(self._container,
                                                 text='Forgot password',
                                                 cursor="hand2")
        self._create_account = basemodels.Label(self._container,
                                                text='Create account',
                                                cursor="hand2")

        # Status
        self._status = basemodels.Label(self._container, text='Bad stuff')

        # Login button
        self._btn_login = basemodels.Button(self._container, text='Login')

        # Place everything.
        self._label_user.grid(row=0, column=0, padx=10, pady=20)
        self._label_pass.grid(row=1, column=0, padx=10, pady=20)
        self._user.grid(row=0, column=1, padx=10, pady=20)
        self._pass.grid(row=1, column=1, padx=10, pady=20)

        self._status.grid(row=2, column=0, columnspan=2, pady=10)
        self._btn_login.grid(row=3, column=0, columnspan=2)

        basemodels.Label(self._container).grid(row=4)   # Dummy to fill a row.
        self._create_account.grid(row=5, column=0, padx=10, pady=20)
        self._forgot_password.grid(row=5, column=1, padx=10, pady=20)

        self._container.pack(padx=50, pady=50)

        # Bind callbacks
        self._forgot_password.bind('<Button-1>', self.create_account)
        self._create_account.bind('<Button-1>', self.create_account)

    def create_account(self, e):
        webbrowser.open_new('https://www.google.com')