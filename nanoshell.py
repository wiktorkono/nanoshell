import os

from imports import *
from bin.coloramasetup import *

running = True
versionStr = "0.1.2"

system_platform = "win" #run.py replaces it with the system platform

def platformWarning():
    if system_platform == "win":
        print(f"{red}You're attempting to run a command from an addon that was made for the platform {light_green}linux{red}. Due to possible instability, you can't use commands from this addon.{r}")
    if system_platform == "linux":
        print(f"{red}You're attempting to run a command from an addon that was made for the platform {light_green}win{red}. Due to possible instability, you can't use commands from this addon.{r}")
    else:
        print("Nanoshell was unable to identify your system platform. Please use a supported platform (win/linux).")

print(f"{a}{bright}nanoshell v{versionStr} {light_green}on {system_platform}{dim}{white} - {r}{white}(C) Kwadratz, Mihael2017 2023")

while running:
    prompt = input(f"{bright}{a}nanoshell{dim}{white} > {r}")

    # DO NOT WRITE ANYTHING BELOW!

    if prompt.startswith('addons'): AddonManagementmainAddonMng(prompt)
    elif prompt.startswith('clear'): ClearScreenclear(prompt)
    elif prompt.startswith('datetime'): DateTimeshowDateTime(prompt)
    elif prompt.startswith('exit'): Exitexit(prompt)
    elif prompt.startswith('help'): Helpmain(prompt)
    elif prompt.startswith('reload'): AddonReloadmain(prompt)
    elif prompt.startswith('user'): CurrentUsershowUser(prompt)
    elif prompt.startswith('gethash'): GetHashobtain_hash(prompt)
    elif prompt.startswith('hibernate'): HibernatefromOffboardhibernate(prompt)
    elif prompt.startswith('lock'): LockfromOffboardlock(prompt)
    elif prompt.startswith('off'): OffboardforWindowslaunchOffboard(prompt)
    elif prompt.startswith('restart'): RestartfromOffboardrestart(prompt)
    elif prompt.startswith('shutdown'): ShutdownfromOffboardshutdown(prompt)
    elif prompt.startswith('sleep'): SleepfromOffboardsleep(prompt)
    elif prompt.startswith('photoview'): PhotoViewerphotoview(prompt)
    elif prompt.startswith('win95keygen'): Windows95KeygenkeyPicker(prompt)
    else: print(f'{bright}{red}Error:{r} Command not found. Type {a}{bright}help{r} for the list of all commands')