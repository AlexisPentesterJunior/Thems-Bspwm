import os
import platform
import shutil
import signal
import sys
import subprocess
from datetime import datetime
from sys import stdout

# =============== Utilidades =================
def run_command(command, cwd=None):
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        red()
        print(f"[!] Error al ejecutar: {command}\nDetalles: {e}")
        reset_color()

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

# =============== Funciones para Git ========================
def checkout_branch(branch, cwd=None):
    """Realiza un git checkout de la rama especificada."""
    print(f"[+] Cambiando a la rama '{branch}'...")
    run_command(f"git checkout {branch}", cwd=cwd)

def download_branch(branch, cwd=None):
    """Descarga las ramas necesarias."""
    print(f"[+] Descargando los archivos de la rama '{branch}'...")
    run_command(f"git pull origin {branch}", cwd=cwd)

# =============== Menú de Selección de Temas ==================
def mostrar_menu_temas():
    print("\n[+] Selecciona los temas que deseas instalar:")
    print("1. Tema A (rama 's4vitar')")
    print("2. Tema B (rama 'theme-b')")
    print("3. Tema C (rama 'theme-c')")
    print("4. Todos los temas")
    print("0. Salir")

def obtener_seleccion_usuario():
    """Obtiene la selección del usuario del menú."""
    try:
        seleccion = int(input("\n[+] Ingresa el número de tu selección: "))
        return seleccion
    except ValueError:
        red()
        print("[!] Por favor ingresa un número válido.")
        reset_color()
        return None

def procesar_seleccion(seleccion, cwd):
    """Procesa la selección del usuario y realiza el checkout de las ramas necesarias."""
    if seleccion == 1:
        checkout_branch("s4vitar", cwd)
        download_branch("s4vitar", cwd)
    elif seleccion == 2:
        checkout_branch("theme-b", cwd)
        download_branch("theme-b", cwd)
    elif seleccion == 3:
        checkout_branch("theme-c", cwd)
        download_branch("theme-c", cwd)
    elif seleccion == 4:
        # Descargar todos los temas
        for branch in ["s4vitar", "theme-b", "theme-c"]:
            checkout_branch(branch, cwd)
            download_branch(branch, cwd)
    elif seleccion == 0:
        print("[+] Saliendo del instalador.")
        sys.exit(0)
    else:
        red()
        print("[!] Selección no válida. Intenta nuevamente.")
        reset_color()

# =============== Main ========================
def main():
    clear_console()
    print("\n[+] Instalador de temas")

    # Obtener el directorio donde se ejecuta el script
    cwd = os.getcwd()

    while True:
        mostrar_menu_temas()
        seleccion = obtener_seleccion_usuario()
        if seleccion is not None:
            procesar_seleccion(seleccion, cwd)

if __name__ == "__main__":
    main()
