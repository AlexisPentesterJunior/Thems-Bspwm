# Theme Selector and Installer

This project provides a command-line theme selector and installer script for Linux distributions, primarily targeting Kali Linux and Parrot OS. It allows users to select and install custom themes easily through a simple menu interface.

## Features

- Interactive menu to select themes based on the operating system.
- Supports installation of the "S4vitar" theme for Kali Linux.
- Placeholder support for Parrot OS and other themes.
- Automatic system update and upgrade before theme installation.
- Git integration to fetch and update theme files from remote branches.

## Installation

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3 installed.
3. Run the script using Python:

```bash
git Clone https://github.com/AlexisPentesterJunior/Thems-Bspwm.git
cd Thems-Bspwm
```

```bash
python install.py
```

```bash
python thems.py
```

## Notes

- Options 3, 4, and 5 are currently placeholders and not implemented.
- The Parrot OS theme installation is a placeholder and needs implementation.
- The script requires `git` and `sudo` privileges for some operations.
- Tested on Kali Linux.

## Additional Installer Script: install.py

This project also includes an installer script `install.py` that provides a menu-driven interface to install various components commonly used in a bspwm environment:

- BSPWM window manager
- SXHKD hotkey daemon
- Polybar status bar
- Picom compositor
- Option to install all components at once

The script handles system updates, dependency installation, cloning source repositories, building, and installing each component.

## License

This project is open source and free to use.
