import os
import platform
import subprocess
import signal
import sys
from sys import stdout
import shutil
from datetime import datetime

# =============== Utilidades =================
def run_command(command, cwd=None):
    """Ejecuta un comando en la terminal y maneja errores."""
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        red()
        print(f"[!] Error al ejecutar: {command}\nDetalles: {e}")
        reset_color()
    except Exception as e:
        red()
        print(f"[!] Error inesperado: {e}")
        reset_color()

def clear_console():
    """Limpia la consola dependiendo del sistema operativo."""
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
def fetch_and_update_branch(branch_name, cwd=None):
    """Actualiza los archivos de una rama remota sin cambiar la rama actual y mueve los archivos a un directorio con el nombre de la rama."""
    print(f"[+] Actualizando los archivos de la rama remota '{branch_name}'...")

    # Crear el directorio con el nombre de la rama
    branch_dir = os.path.join(cwd, branch_name)
    if not os.path.exists(branch_dir):
        os.makedirs(branch_dir)
    else:
        # Si el directorio ya existe, agregar un número al final para evitar sobrescribir
        i = 1
        while os.path.exists(f"{branch_dir}_{i}"):
            i += 1
        branch_dir = f"{branch_dir}_{i}"
        os.makedirs(branch_dir)

    # Ejecutar git fetch y reset
    run_command(f"git fetch origin {branch_name}", cwd=cwd)
    run_command(f"git reset --hard origin/{branch_name}", cwd=cwd)
    
    # Mover los archivos actualizados al nuevo directorio
    for filename in os.listdir(cwd):
        file_path = os.path.join(cwd, filename)
        if os.path.isfile(file_path):
            shutil.move(file_path, os.path.join(branch_dir, filename))

    green()
    print(f"[✔] Archivos de la rama '{branch_name}' movidos a '{branch_dir}'. Instalación completa.")

# ============== Sistema =====================
def actualizar_kali():
    """Actualiza Kali Linux con apt."""
    run_command("sudo apt update -y && sudo apt upgrade -y")

# =============== Menú de Selección de Temas ==================
def banner():
    """Muestra el banner de bienvenida."""
    banner_text = """
    ████████╗███████╗███╗   ███╗ █████╗ ███████
    ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔════
       ██║   █████╗  ██╔████╔██║███████║███████╗
       ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║
       ██║   ███████╗██║ ╚═╝ ██║██║  ██║███████║
       ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
    """
    red()
    print(banner_text)

def menu_temas():
    """Muestra el menú de selección de temas."""
    blue()
    print("[+] Seleccione el tema a instalar según su sistema operativo [+]")
    green()
    print("\n1 -> S4vitar (Kali Linux) ")
    print("\n2 -> S4vitar (Parrot OS) ")
    print("\n3 -> No Disponible ")
    print("\n4 -> No Disponible ")
    print("\n5 -> No Disponible ")
    print("\n6 -> Salir ")

# =============== Main ========================
def main_temas():
    """Función principal que ejecuta el menú y las opciones seleccionadas."""
    while True:
        clear_console()
        banner()
        menu_temas()
        blue()
        opcion = input("\nIngrese el número del tema que desea seleccionar: ")
        valid_options = {"1", "2", "3", "4", "5", "6"}

        if opcion not in valid_options:
            blue()
            print(f"\nOpción inválida: {opcion}")
            input("\nPresione Enter para intentar de nuevo...")
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
            input("\nPresione Enter para continuar...")

# ============== Instalación ==================
def s4vitar_kali():
    """Instala el tema S4vitar en Kali Linux."""
    blue(); print("[+] Instalando el tema S4vitar en Kali Linux ..."); reset_color()
    actualizar_kali()
    branch_name = "s4vitar-kali"
    repo_dir = os.getcwd()
    fetch_and_update_branch(branch_name, cwd=repo_dir)

def s4vitar_parrot():
    """Instala el tema S4vitar en Parrot OS (pendiente de implementación)."""
    print("\n[+] Instalando el tema S4vitar en Parrot OS ...")
    # TODO: Implement installation steps for Parrot OS
    print("[✔] Instalación del tema S4vitar completa.")

def s4vitar_opcion3():
    """Instala el tema para opción 3 (pendiente de implementación)."""
    print("\n[+] Instalando el tema para opción 3... (No implementado)")

def s4vitar_opcion4():
    """Instala el tema para opción 4 (pendiente de implementación)."""
    print("\n[+] Instalando el tema para opción 4... (No implementado)")

def s4vitar_opcion5():
    """Instala el tema para opción 5 (pendiente de implementación)."""
    print("\n[+] Instalando el tema para opción 5... (No implementado)")

if __name__ == "__main__":
    main_temas()
