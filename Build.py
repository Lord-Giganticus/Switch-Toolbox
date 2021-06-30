import os
from os import path
import subprocess
import shutil
import sys

home_dir = path.dirname(__file__)

if os.getcwd() is not home_dir:
    os.chdir(home_dir)

subprocess.call("nuget restore", shell=True)

commands = []

for file in os.listdir(os.getcwd()):
    if path.isfile(file) is True:
        if file.endswith(".sln") is True:
            commands.append(f'msbuild "{path.abspath(file)}" -p:Configuration=Release')

for command in commands:
    subprocess.call(command, shell=True)

files = []

f = open("Files.txt","r")

for line in f.readlines():
    files.append(line)

f.close()

os.chdir("Toolbox\\bin\\Release")

for file in files:
    subprocess.call(f'7z a "Toolbox-Latest.zip" "{file}"',shell=True)

shutil.move("Toolbox-Latest.zip", f"{home_dir}\\Toolbox-Latest.zip")

os.chdir(home_dir)

sys.exit(0)