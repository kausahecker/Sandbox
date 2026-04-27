import subprocess

def run_command_in_terminal(command:str)->str:
    return subprocess.run(command,shell=True,capture_output=True,text=True).stdout