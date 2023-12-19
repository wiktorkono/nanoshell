import os

from imports import *
from bin.coloramasetup import *

running = True
versionStr = "0.1.2"

system_platform = {platform-placeholder} #run.py replaces it with the system platform

def platformWarning():
    if system_platform == "win":
        print(f"{red}You're attempting to run a command from an addon that was made for the platform {light_green}linux{red}. Due to possible instability, you can't use commands from this addon.{r}")
    if system_platform == "linux":
        print(f"{red}You're attempting to run a command from an addon that was made for the platform {light_green}win{red}. Due to possible instability, you can't use commands from this addon.{r}")
    else:
        print("Nanoshell was unable to identify your system platform. Please use a supported platform (win/linux).")

print(f"{a}nanoshell v{versionStr} {light_green}on {system_platform}{dim}{white} - {r}{white}(C) Kwadratz, Mihael2017 2023")

while running:
    prompt = input(f"{a}nanoshell{dim}{white} > {r}")

    # DO NOT WRITE ANYTHING BELOW!
