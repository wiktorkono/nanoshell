from colorama import Fore as c
from colorama import Back as bg
from colorama import Style as s
import os

white = c.WHITE
dim = s.DIM
green = c.GREEN
r = s.RESET_ALL

running = True

print(f"{green}nanoshell v0.0.1 {dim}{white} - {r}{white}(C) Kwadratz, Mihael2017 2023")

while running:
    prompt = input(f"{green}nanoshell{dim}{white} > {r}")

    # DO NOT WRITE ANYTHING BELOW!
    if prompt == 'hellow' or prompt.startswith('hellow') == 'a': helloworld(prompt)
    elif prompt == 'hellow2' or prompt.startswith('hellow2') == 'a': helloworld2(prompt)
    elif prompt == 'printa' or prompt.startswith('printa') == 'a': a(prompt)