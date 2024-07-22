import os

from imports import *
from bin.coloramasetup import *

running = True
versionStr = "0.1.4"

system_platform = {platform-placeholder} #run.py replaces it with the system platform

def platformWarning():
    if system_platform == "win" or system_platform == "linux" or system_platform == "darwin":
        print(f"{red}You're attempting to run a command from an addon that was made specifically for another platform. Due to possible instability, you can't use commands from this addon.{r}")
    else:
        print("Nanoshell was unable to identify your system platform. Please use a supported platform (win/linux/darwin).")

print(f"{a}{bright}nanoshell v{versionStr} {a}on {system_platform}{dim}{white} - {r}{white}(C) Hansquare, jajtic 2024")

while running:
    prompt = input(f"{bright}{a}nanoshell{dim}{white} > {r}")

    # DO NOT WRITE ANYTHING BELOW!
