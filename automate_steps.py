#!/usr/bin/env python3
import os
import platform
import subprocess

# Step 1: Create a virtual environment
subprocess.run(["python", "-m", "venv", "venv"])

# Step 2: Activate the virtual environment
if platform.system() == "Windows":
    activate_command = ".\\venv\\Scripts\\activate"
else:
    activate_command = "source venv/bin/activate"

# Modify the subsequent commands to be executed within the activated environment
commands = [
    f"{activate_command} && pip install -r requirements.txt",
    f"{activate_command} && set FLASK_APP=app && flask db init",
    f"{activate_command} && set FLASK_APP=app && flask db migrate",
    f"{activate_command} && set FLASK_APP=app && flask db upgrade",
    f"{activate_command} && flask --debug run",
]

# Execute the commands
for command in commands:
    subprocess.run(command, shell=True, executable="cmd" if platform.system() == "Windows" else "/bin/bash")
