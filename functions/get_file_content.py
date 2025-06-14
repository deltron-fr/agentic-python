import os
from google.genai import types

def get_file_content(working_directory, file_path):

    pwd = os.path.abspath(working_directory)
    current_file = os.path.abspath(os.path.join(working_directory, file_path))

    if (not current_file.startswith(f"{pwd}")):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(current_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000

    try:
        with open(current_file, "r") as f:
            content = f.read()
            if len(content) > MAX_CHARS:
                return f'[...File "{file_path}" truncated at 10000 characters]'
        
            return content
    
    except Exception as e:
        return f"Error: The error is {e}" 


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Return the content of the file specified, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to get the contents of the file from.",
            ),
        },
    ),
)
