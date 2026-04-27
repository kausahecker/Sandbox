import subprocess
import os
from pathlib import Path

def run_command_in_terminal(command:str)->str:
    return subprocess.run(command,shell=True,capture_output=True,text=True).stdout

def create_file(filename:str)->bool:
    try:
        with open(filename,"w",encoding="utf-8") as f:
            return True
    except Exception as e:
        print(e)
        return False

def get_cwd()->str:
    try:
        cwd=Path(os.getenv("CWD")).resolve()
        if not cwd.exists():
            return "No valid directory '"+os.getenv("CWD")+"'"
        return cwd.as_posix()
    except Exception as e:
        print(e)
        return "No valid directory '"+os.getenv("CWD")+"'"

def set_cwd(path:str)->bool:
    try:
        cwd=Path(path).resolve()
        if not cwd.exists():
            return False
        os.environ["CWD"]=cwd.as_posix()
        return True
    except Exception as e:
        print(e)
        return False

print(get_cwd())