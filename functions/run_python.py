import os, subprocess

def run_python_file(working_directory, file_path):
    pwd = os.path.abspath(working_directory)
    current_file = os.path.abspath(os.path.join(working_directory, file_path))

    if (not current_file.startswith(f"{pwd}")):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(current_file):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python3", f"{current_file}"], timeout=30, capture_output=True, cwd=pwd, text=True)

        output = []

        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")

        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"

        if output is None:
            return "No output produced."
        return "".join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

    