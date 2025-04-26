import os
import platform
import shutil
import signal
import sys
import subprocess
from datetime import datetime
from sys import stdout

# =============== Utilidades =================
def is_root():
    return os.geteuid() == 0

def run_command(command, cwd=None):
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        red()
        print(f"[!] Error al ejecutar: {command}\nDetalles: {e}")
        reset_color()

def clonar_o_actualizar(repo_url, carpeta, branch=None):
    if not os.path.exists(carpeta):
        cmd = f"git clone --recursive {repo_url}"
        if branch:
            cmd = f"git clone --recursive --branch {branch} {repo_url}"
        run_command(cmd)
    else:
        run_command(f"cd {carpeta} && git pull --recurse-submodules")

def limpiar_carpeta(carpeta):
    if os.path.exists(carpeta):
        shutil.rmtree(carpeta)

def clear_console():
    os.system("cls" if platform.system() == "Windows" else "clear")

# =============== Colores ====================
def set_color(color_code): stdout.write(color_code); stdout.flush()
def reset_color(): stdout.write("\033[0m"); stdout.flush()
def red(): set_color("\033[1;31m")
def green(): set_color("\033[0;32m")
def blue(): set_color("\033[1;34m")
def yellow(): set_color("\033[1;33m")
def purple(): set_color("\033[1;35m")
def white(): set_color("\033[1;37m")

# ============== Señal Ctrl+C ================
def signal_handler(sig, frame):
    blue(); print("\n[+] Cancelado por el usuario. Saliendo..."); reset_color()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# ============== Sistema =====================
def actualizar_sistema():
    run_command("sudo apt update -y && sudo apt upgrade -y")

# =============== Menú ========================
def banner_instalacion():
    banner = """
    ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗      █████╗  ██████╗██╗ ██████╗ ███╗   ██╗
    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║
    ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ███████║██║     ██║██║   ██║██╔██╗ ██║
    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██╔══██║██║     ██║██║   ██║██║╚██╗██║
    ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗██║  ██║╚██████╗██║╚██████╔╝██║ ╚████║
    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
    """
    red()
    print(banner)
    reset_color()

def menu_instalacion():
    blue()
    print("[+] Seleccione lo que desea instalar [+]")
    green()
    print("\n1 -> Instalar Bspwm ")
    print("\n2 -> Instalar Sxhkd ")
    print("\n3 -> Instalar Polybar ")
    print("\n4 -> Instalar Picom ")
    print("\n5 -> Instalar Todo ")
    print("\n6 -> Salir ")

# =============== Main ========================
def main_instalacion():
    while True:
        clear_console()
        banner_instalacion()
        menu_instalacion()
        blue()
        opciones = input("\n Ingrese el/los número(s) de la(s) opción(es) deseada(s) separados por coma: ")
        opciones_seleccionadas = [opcion.strip() for opcion in opciones.split(",")]
        valid_options = {"1", "2", "3", "4", "5", "6"}

        for opcion in opciones_seleccionadas:
            if opcion not in valid_options:
                blue()
                print(f"\n Opción inválida: {opcion}")
                continue
            if opcion == "1":
                instalar_bspwm()
            elif opcion == "2":
                instalar_sxhkd()
            elif opcion == "3":
                instalar_polybar()
            elif opcion == "4":
                instalar_picom()
            elif opcion == "5":
                instalar_bspwm()
                instalar_sxhkd()
                instalar_polybar()
                instalar_picom()
                blue()
                print("\n[✔] Instalación completa de todos los componentes.")
            elif opcion == "6":
                clear_console()
                blue()
                print("\n[+] Gracias por usar el instalador. ¡Hasta luego!")
                reset_color()
                sys.exit(0)
        blue()
        input("\n Presione Enter para continuar...")

# ============== Instalacion ==================
def instalar_bspwm():
    blue(); print("[+] Instalando BSPWM ..."); reset_color()
    actualizar_sistema()
    deps = ("git make gcc libxcb1-dev libxcb-util0-dev libxcb-ewmh-dev "
            "libxcb-randr0-dev libxcb-icccm4-dev bspwm libxcb-keysyms1-dev "
            "libxcb-xinerama0-dev libxcb-shape0-dev libxcb-xfixes0-dev "
            "libx11-xcb-dev libxcb-cursor-dev")
    run_command(f"sudo apt install -y {deps}")
    clonar_o_actualizar("https://github.com/baskerville/bspwm.git", "bspwm")
    run_command("cd bspwm && make && sudo make install")
    limpiar_carpeta("bspwm")
    green(); print("[✔] BSPWM instalado correctamente."); reset_color()

def instalar_sxhkd():
    blue(); print("[+] Instalando SXHKD ..."); reset_color()
    actualizar_sistema()
    deps = ("git make gcc libxcb1-dev libxcb-keysyms1-dev build-essential "
            "libx11-dev libxft-dev libxinerama-dev libxrandr-dev")
    run_command(f"sudo apt install -y {deps}")
    clonar_o_actualizar("https://github.com/baskerville/sxhkd.git", "sxhkd")
    run_command("cd sxhkd && make && sudo make install")
    limpiar_carpeta("sxhkd")
    green(); print("[✔] SXHKD instalado correctamente."); reset_color()

def instalar_polybar():
    blue(); print("[+] Instalando Polybar (desde código)..."); reset_color()
    actualizar_sistema()
    deps = ("build-essential git cmake pkg-config python3-sphinx python3-packaging "
            "libuv1-dev libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev "
            "libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev "
            "libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev "
            "libasound2-dev libpulse-dev libmpdclient-dev libcurl4-openssl-dev "
            "libnl-genl-3-dev libiw-dev")
    run_command(f"sudo apt install -y {deps}")
    clonar_o_actualizar("https://github.com/polybar/polybar", "polybar")
    run_command("cd polybar && mkdir -p build && cd build && cmake .. && make -j$(nproc) && sudo make install")
    limpiar_carpeta("polybar")
    green(); print("[✔] Polybar instalado correctamente."); reset_color()

def instalar_picom():
    blue(); print("[+] Instalando Picom (desde código)..."); reset_color()
    actualizar_sistema()
    deps = ("git build-essential pkg-config meson ninja-build libxext-dev libxcb1-dev "
            "libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev "
            "libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev "
            "libxcb-present-dev libxcb-xinerama0-dev libx11-xcb-dev libxcb-glx0-dev "
            "libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev "
            "libev-dev uthash-dev libepoxy-dev libxdg-basedir-dev")
    run_command(f"sudo apt install -y {deps}")
    clonar_o_actualizar("https://github.com/ibhagwan/picom", "picom", branch="next-rebase")
    run_command("cd picom && meson setup --buildtype=release build && ninja -C build && sudo ninja -C build install")
    limpiar_carpeta("picom")
    green(); print("[✔] Picom instalado correctamente."); reset_color()

if __name__ == "__main__":
    main_instalacion()