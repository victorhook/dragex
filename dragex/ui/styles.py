font = 'Fixedsys'

colors = {
    'gray_light': '#D3D4D9',
    'gray_dark': '#252627',
    'gray_semi_dark': '#333436',
    'red': '#BB0A21',
    'white': '#FFF9FB'
}

labels = {
    'bg': colors['gray_dark'],
    'fg': colors['white'],
    'font': (font, 16)
}

buttons = {
    'bg': colors['gray_dark'],
    'fg': colors['red'],
    'font': (font, 18),
    'highlightbackground': colors['gray_light'],
    'highlightcolor': colors['white'],
    'padx': 20,
    'pady': 10
}

frames = {
    'highlightbackground': colors['gray_light'],
    'highlightcolor': colors['white'],
    'bg': colors['gray_dark'],
    'relief': 'ridge',
}

entry = {
    'font': (font, 16),
    'fg': colors['white'],
    'bg': colors['gray_semi_dark'],
    'highlightcolor': colors['gray_dark'],
    'highlightbackground': colors['gray_dark'],
    'insertbackground': colors['white'],
    'bd': 0,
}

scale = {
    'font': (font, 16),
    'fg': colors['white'],
    'bg': colors['gray_dark'],
    'highlightcolor': colors['gray_dark'],
    'highlightbackground': colors['gray_dark'],
    'bd': 0,
}