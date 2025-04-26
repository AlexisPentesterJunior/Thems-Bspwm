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
def actualizar_kali():
    run_command("sudo apt update -y && sudo apt upgrade -y")

# =============== Función para clonar y renombrar rama ====================

def clone_and_rename_repo(repo_url, branch_name, new_repo_name):
    """
    Clona un repositorio desde una rama específica y renombra el directorio del repositorio clonado a un nombre especificado.

    :param repo_url: URL del repositorio Git.
    :param branch_name: Nombre de la rama que se desea clonar.
    :param new_repo_name: Nuevo nombre para el directorio del repositorio.
    """
    try:
        # Clonamos el repositorio y especificamos la rama que se desea clonar
        print(f"[+] Clonando la rama '{branch_name}' del repositorio {repo_url}...")
        run_command(f"git clone --branch {branch_name} {repo_url}")

        # Obtener el nombre del repositorio de la URL para usarlo como nombre de carpeta
        repo_name = repo_url.split('/')[-1].replace(".git", "")
        repo_path = os.path.join(os.getcwd(), repo_name)

        # Verificar si el directorio existe antes de intentar cambiar a él
        if not os.path.isdir(repo_path):
            print(f"[!] Error: El directorio {repo_path} no se creó correctamente.")
            return

        # Renombrar el directorio del repositorio clonado
        new_repo_path = os.path.join(os.getcwd(), new_repo_name)
        os.rename(repo_path, new_repo_path)  # Renombrar el directorio
        print(f"[✔] El directorio del repositorio ha sido renombrado a: {new_repo_name}")

    except Exception as e:
        print(f"[!] Error al clonar o renombrar el repositorio: {e}")

# =============== Menú de Selección de Temas ==================
def banner():
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
    print("\n[+] Instalando el tema S4vitar en Kali Linux ...")

    repo_url = "https://github.com/AlexisPentesterJunior/Thems-Bspwm.git"
    branch_name = "s4vitar-kali"
    new_repo_name = "dotfiles"
    clone_and_rename_repo(repo_url, branch_name, new_repo_name)

    print("[✔] Instalación del tema S4vitar completa.")

def s4vitar_parrot():
    print("\n[+] Instalando el tema S4vitar en Parrot OS ...")
    print("[✔] Instalación del tema S4vitar completa.")

def s4vitar_opcion3():
    print("\n[+] Instalando el tema para opción 3... (No implementado)")

def s4vitar_opcion4():
    print("\n[+] Instalando el tema para opción 4... (No implementado)")

def s4vitar_opcion5():
    print("\n[+] Instalando el tema para opción 5... (No implementado)")

if __name__ == "__main__":
    main_temas()
