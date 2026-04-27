import subprocess
import os
from pathlib import Path

from tool import Tool

def run_command_in_terminal(command:str)->str:
    return subprocess.run(command,shell=True,capture_output=True,text=True).stdout

def get_cwd()->str:
    """
    A tool to get the current working directory for the Sandbox Agent

    Returns:
        str: The current working directory
    """

    try:
        cwd=Path(os.getenv("CWD")).resolve()
        if not cwd.exists():
            return "No valid directory '"+os.getenv("CWD")+"'"
        return cwd.as_posix()
    except Exception as e:
        print(e)
        return "No valid directory '"+os.getenv("CWD")+"'"

def set_cwd(path:str)->bool:
    """
    A tool to get the current working directory for the Sandbox Agent

    Args:
        path (str): The path to set as the current working directory
    
    Returns:
        bool: True if the path is valid and exists, False otherwise
    """

    try:
        cwd=Path(path).resolve()
        if not cwd.exists():
            return False
        os.environ["CWD"]=cwd.as_posix()
        return True
    except Exception as e:
        print(e)
        return False

def create_file(filename:str)->bool:
    """
    A tool to create a file in the current working directory

    Args:
        filename (str): The name of the file to create

    Returns:
        bool: True if the file was created, False otherwise
    """

    try:
        with open(filename,"w",encoding="utf-8") as f:
            return True
    except Exception as e:
        print(e)
        return False

def delete_file(filename:str)->bool:
    """
    A tool to delete a file in the current working directory

    Args:
        filename (str): The name of the file to create

    Returns:
        bool: True if the file was deleted, False otherwise
    """

    try:
        file_path=Path(filename)
        if not file_path.exists():
            return False
        file_path.unlink()
        return True
    except Exception as e:
        print(e)
        return False

def read_file(filename:str)->str:
    """
    A tool to read a file in the current working directory

    Args:
        filename (str): The name of the file to read

    Returns:
        str: The contents of the file
    """

    try:
        with open(filename,"r",encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(e)
        return ""

def write_file(filename:str,content:str)->bool:
    """
    A tool to write to a file in the current working directory

    Args:
        filename (str): The name of the file to write to
        content (str): The contents to write to the file

    Returns:
        bool: True if the file was written, False otherwise
    """

    try:
        with open(filename,"w",encoding="utf-8") as f:
            f.write(content)
            return True
    except Exception as e:
        print(e)
        return False

TOOL_FUNCTIONS=[get_cwd,set_cwd,create_file,delete_file,read_file,write_file]

TOOLS=[]

def init():
    for tool in TOOL_FUNCTIONS:
        TOOLS.append(Tool(tool.__name__,tool.__doc__,tool))