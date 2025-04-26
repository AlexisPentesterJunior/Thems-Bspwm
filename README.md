# Theme Selector and Installer

This project provides a command-line theme selector and installer script for Linux distributions, primarily targeting Kali Linux and Parrot OS. It allows users to select and install custom themes easily through a simple menu interface.

## Features

## Installation

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3 installed.
3. Run the script using Python:

```bash
git clone https://github.com/AlexisPentesterJunior/Thems-Bspwm.git
cd Thems-Bspwm
```

- Usar este comando para instalcion de recursos y otros

```bash
python install.py
```

- Usar

```bash
python thems.py
```

## Additional Installer Script: install.py

This project also includes an installer script `install.py` that provides a menu-driven interface to install various components commonly used in a bspwm environment:

- BSPWM window manager
- SXHKD hotkey daemon
- Polybar status bar
- Picom compositor
- Option to install all components at once

The script handles system updates, dependency installation, cloning source repositories, building, and installing each component.
