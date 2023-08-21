import os

from imports import *
from bin.coloramasetup import *

running = True
versionStr = "0.1.1"

platform = os.name
if platform == "nt":
    platform = "win"
elif platform == "posix":
    platform = "linux"
elif platform == "java":
    platform = "java"
else:
    platform = "unknown"

print(f"{a}nanoshell v{versionStr} {light_green}on {platform}{dim}{white} - {r}{white}(C) Kwadratz, Mihael2017 2023")

while running:
    prompt = input(f"{a}nanoshell{dim}{white} > {r}")

    # DO NOT WRITE ANYTHING BELOW!
