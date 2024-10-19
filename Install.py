import subprocess
import platform
from tkinter import messagebox


os = platform.system()

if os == "Windows":
    subprocess.run(["py", "-m", "pip", "install", "winotify"])
else:
    subprocess.run(["py", "-m", "pip3", "install", "winotify"])

messagebox.showinfo("Done", "Setup done")