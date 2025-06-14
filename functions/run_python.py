import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    pwd = os.path.abspath(working_directory)
    current_file = os.path.abspath(os.path.join(working_directory, file_path))

    if (not current_file.startswith(f"{pwd}")):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(current_file):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = ["python3", f"{current_file}"]
        if args:
            commands.extend(args)
            
        result = subprocess.run(commands, timeout=30, capture_output=True, cwd=pwd, text=True)

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
    

schema_run_python = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            )
        },
    ),
)

    