---
title: "KALIBSPWM Project Documentation"
author: "Auto-generated"
date: "`r Sys.Date()`"
output: html_document
---

## Project Overview

The KALIBSPWM project is a collection of scripts and configuration files to install and configure a customized Linux desktop environment using bspwm, sxhkd, polybar, picom, and a custom theme. The project includes an installation script, configuration files for window manager and terminal, and utility scripts.

## Installation Script (install.py)

The `install.py` script is the main installation utility for the project. It provides a menu-driven interface to install the following components:

- BSPWM: A tiling window manager
- SXHKD: A hotkey daemon
- Polybar: A status bar
- Picom: A compositor
- Custom Theme

## Key Functions

- `clonar_o_actualizar(repo_url, carpeta, branch=None)`: Clones a git repository recursively if the target folder does not exist, or pulls updates if it does.
- `run_command(command, cwd=None)`: Runs shell commands with error handling.
- `actualizar_sistema()`: Updates and upgrades the system packages.
- Installation functions for each component handle dependencies installation, cloning source code, building, and cleaning up.

The script uses colored terminal output and handles user interruptions gracefully.

## Configuration Files

## Kitty Terminal Configuration (`Config/kity/kitty.conf`)

This file configures the Kitty terminal emulator with settings such as:

- Font family and size
- Color and URL styles
- Key mappings for copy/paste and window/tab management
- Cursor shape and behavior
- Background opacity and shell to use (zsh)

## BSPWM Resize Script (`Config/bspwm/scripts/bspwm_resize`)

A shell script to resize bspwm windows depending on the focused window state (floating or tiled) and direction. It uses `bspc` commands to adjust window sizes.

## Project Structure

```bas
install.py
Config/
├── bspwm/
│   ├── bspwmrc
│   └── scripts/
│       └── bspwm_resize
├── kity/
│   ├── color.ini
│   └── kitty.conf
├── picom/
├── sxhkd/
│   └── sxhkdrc
```

## Usage

Run the `install.py` script to launch the installation menu. Select the desired components to install. The script will handle dependencies, clone repositories recursively, build from source, and install the components.

## Notes

- The git cloning commands use the `--recursive` flag to ensure submodules are cloned.
- The script cleans up source directories after installation.
- The project is designed for Linux systems with apt package manager.
