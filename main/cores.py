def title(txt, cor=0, tam=30):
    print(Normal_colors[cor], end='')
    print('=' * tam)
    print(f'{txt}'.center(tam))
    print('=' * tam, end='')
    print(reset)


reset = '\033[m'

# Normal colors - cores normais
Normal_colors = {
    'Black': '\033[30m',
    'Red': '\033[31m',
    'Green': '\033[32m',
    'Yellow': '\033[33m',
    'Blue': '\033[34m',
    'Magenta': '\033[35m',
    'Cyan': '\033[36m',
    'Gray': '\033[37m'
}

# Intensy colors - cores fortes
IColors = {
    'IRed': '\033[38;5;9m',
    'IGreen': '\033[38;5;10m',
    'IYellow': '\033[38;5;11m',
    'IBlue': '\033[38;5;12m',
    'IMagenta': '\033[38;5;13m',
    'ICyan': '\033[38;5;14m',
    'IWhite': '\033[38;5;15m'
}


# Background colors - cores de fundo
Bg_Colors = {
    'Bg_Black': '\033[48;5;0m',
    'Bg_Red': '\033[48;5;1m',
    'Bg_Green': '\033[48;5;2m',
    'Bg_Yellow': '\033[48;5;3m',
    'Bg_Blue': '\033[48;5;4m',
    'Bg_Magenta': '\033[48;5;5m',
    'Bg_Cyan': '\033[48;5;6m',
    'Bg_Clay': '\033[48;5;7m'
}

# High Intensty backgrounds
On_IColors = {
    'On_IClay': '\033[48;5;8m',
    'On_IRed': '\033[48;5;9m',
    'On_IGreen': '\033[48;5;10m',
    'On_IYellow': '\033[48;5;11m',
    'On_IBlue': '\033[48;5;12m',
    'On_IMagenta': '\033[48;5;13m',
    'On_ICyan': '\033[48;5;14m',
    'On_IWhite': '\033[48;5;15m'
}

# Inclements
Inclements = {
    'Bold': '\033[1m',
    'Italic': '\033[3m',
    'Underlined': '\033[4m',
    'Inverted': '\033[7m',  # Inverte a cor do texto com o fundo
    'Strikethrough': '\033[9m'
}

# Demonstration
for name, color in Normal_colors.items():
    print(f'{color}{name.title()}{reset}')
print()
for name, color in IColors.items():
    print(f'{color}{name.title()}{reset}')
print()
for name, color in Bg_Colors.items():
    print(f'{color}{name.title()}{reset}')
print()
for name, color in On_IColors.items():
    print(f'{color}{name.title()}{reset}')
print()
for name, inclement in Inclements.items():
    print(f'{inclement}{name.title()}{reset}')
