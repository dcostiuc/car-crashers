#setup.py file needed for cx_Freeze to convert to .exe

import cx_Freeze
import os
import pygame
import idna



'''

'''

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("CarCrashersV3.py")]



cx_Freeze.setup(
    name = "Car Crashers",
    options = {"build_exe": {"packages": ["pygame", "idna", "os"], "include_files" :["bgmusic.wav","highscores.txt", "readme.txt","mainMenuMusic.wav","car.png", "carINVINCIBLE.png", "car2.png", "car2INVINCIBLE.png", "car3.png", "car3INVINCIBLE.png", "icon.png", "crash.wav", "gameTheme2.wav"]}},
    version = "3.0",
    description = "Play as a car that tries to avoid falling objects!",
    executables = executables
    )


