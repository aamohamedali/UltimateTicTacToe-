import subprocess
import platform

## This lets us consistantly run the server from the same directory anytime and fixes pathing issues that were being encountered with imports
if platform.system() == "Windows":
    subprocess.run(["python", "ServerAPI//serverAPI.py"])
else:
    subprocess.run(["python3", "ServerAPI//serverAPI.py"])
