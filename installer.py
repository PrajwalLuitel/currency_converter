import subprocess
import sys

def install_packages(packages):
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install_packages(["requests", "tk", "python-dotenv"])