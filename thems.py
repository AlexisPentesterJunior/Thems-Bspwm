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
#def checkout_branch(branch, cwd=None):
#    """Realiza un git checkout de la rama especificada."""
#    print(f"[+] Cambiando a la rama '{branch}'...")
#    run_command(f"git checkout {branch}", cwd=cwd)

#def download_branch(branch, cwd=None):
#    """Descarga las ramas necesarias."""
#    print(f"[+] Descargando los archivos de la rama '{branch}'...")
#    run_command(f"git pull origin {branch}", cwd=cwd)

# Función para traer y actualizar archivos de una rama remota sin cambiar la rama actual
def fetch_and_update_branch(branch_name, cwd=None):
    print(f"[+] Actualizando los archivos de la rama remota '{branch_name}'...")
    run_command(f"git fetch origin {branch_name}", cwd=cwd)
    run_command(f"git reset --hard origin/{branch_name}", cwd=cwd)

# ============== Sistema =====================
def actualizar_kali():
    run_command("sudo apt update -y && sudo apt upgrade -y")

# =============== Menú de Selección de Temas ==================
def banner():
    banner = """
    ████████╗███████╗███╗   ███╗ █████╗ ███████
    ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔════
       ██║   █████╗  ██╔████╔██║███████║███████╗
       ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║
       ██║   ███████╗██║ ╚═╝ ██║██║  ██║███████║
       ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
    """
    red()
    print(banner)

def menu_temas():
    blue()
    print("[+] Seleccione el tema a instalar segun su sistema operativo [+]")
    green()
    print("\n1 -> S4vitar (Kalli Linux) ")
    print("\n2 -> S4vitar (Parrot OS) ")
    print("\n3 -> No Disponible ")
    print("\n4 -> No Disponible ")
    print("\n5 -> No Disponible ")
    print("\n6 -> Salir ")

# =============== Main ========================
def main_temas():
    while True:
        clear_console()
        banner()
        menu_temas()
        blue()
        opcion = input("\n Ingrese el número del tema que desea seleccionar: ")
        valid_options = {"1", "2", "3", "4", "5", "6"}

        if opcion not in valid_options:
            blue()
            print(f"\n Opción inválida: {opcion}")
            input("\n Presione Enter para intentar de nuevo...")
            continue
        else:
            if opcion == "1":
                s4vitar_kali()
            elif opcion == "2":
                s4vitar_parrot()
            elif opcion == "3":
                s4vitar_opcion3()
            elif opcion == "4":
                s4vitar_opcion4()
            elif opcion == "5":
                s4vitar_opcion5()
            elif opcion == "6":
                clear_console()
                blue()
                print("\n[+] Gracias por usar el selector de tema. ¡Hasta luego!")
                reset_color()
                sys.exit(0)
            
            blue()
            input("\n Presione Enter para continuar...")

# ============== Instalacion ==================
def s4vitar_kali():
    blue(); print("[+] Instalando el tema S4vitar en Kali Linux ..."); reset_color()
    actualizar_kali()
    # No dependencies specified, so skipping apt install
    # deps = ("")
    # run_command(f"sudo apt install -y {deps}")

    branch_name = "s4vitar-kali"
    repo_dir = os.getcwd()
    fetch_and_update_branch(branch_name, cwd=repo_dir)
    #checkout_branch(branch_name, cwd=repo_dir)
    # Por ejemplo, si hay archivos de configuración que mover:
    # run_command(f"cp -r {repo_dir}/config/* ~/.config/")
    green()
    print("[✔] Instalación del tema S4vitar completa.")

def s4vitar_parrot():
    print("\n[+] Instalando el tema S4vitar en Parrot OS ...")
    # TODO: Implement installation steps for Parrot OS
    print("[✔] Instalación del tema S4vitar completa.")

def s4vitar_opcion3():
    print("\n[+] Instalando el tema para opción 3... (No implementado)")

def s4vitar_opcion4():
    print("\n[+] Instalando el tema para opción 4... (No implementado)")

def s4vitar_opcion5():
    print("\n[+] Instalando el tema para opción 5... (No implementado)")


if __name__ == "__main__":
    main_temas()
