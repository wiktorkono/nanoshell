from colorama import Fore as c
from colorama import Back as bg
from colorama import Style as s
import os

from imports import *

white = c.WHITE
dim = s.DIM
green = c.GREEN
r = s.RESET_ALL

running = True

print(f"{green}nanoshell v0.0.1 {dim}{white} - {r}{white}(C) Kwadratz, Mihael2017 2023")

while running:
    prompt = input(f"{green}nanoshell{dim}{white} > {r}")

    # DO NOT WRITE ANYTHING BELOW!