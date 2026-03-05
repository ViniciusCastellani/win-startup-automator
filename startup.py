import ctypes
import subprocess
import os
import time
import pyautogui
import pygetwindow as gw


def is_capslock_on():
    return ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 1


def is_numlock_on():
    return ctypes.WinDLL("User32.dll").GetKeyState(0x90) & 1


def ensure_capslock():
    if not is_capslock_on():
        pyautogui.press("capslock")


def ensure_numlock():
    if not is_numlock_on():
        pyautogui.press("numlock")


def enable_bluetooth():
    try:
        subprocess.run(
            ["powershell", "Start-Service", "bthserv"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except:
        pass


def open_shortcut(path):
    os.startfile(path)


def wait_window(title_part, timeout=30):
    start = time.time()

    while time.time() - start < timeout:
        windows = gw.getWindowsWithTitle(title_part)

        if windows:
            window = windows[0]
            window.activate()
            return window

        time.sleep(1)

    return None


def fullscreen():
    time.sleep(1)
    pyautogui.press("f11")


def minimize(window):
    window.minimize()

time.sleep(15)
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
matific = os.path.join(desktop, "Matific.lnk")
elefante = os.path.join(desktop, "Elefante Letrado Login.lnk")

ensure_capslock()
ensure_numlock()
enable_bluetooth()
open_shortcut(matific)
matific_window = wait_window("Matific")

if matific_window:
    fullscreen()
    time.sleep(2)
    minimize(matific_window)

open_shortcut(elefante)
elefante_window = wait_window("Elefante")

if elefante_window:
    fullscreen()

print("Startup concluído.")