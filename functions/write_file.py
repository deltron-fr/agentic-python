import os
from google.genai import types

def write_file(working_directory, file_path, content):
    pwd = os.path.abspath(working_directory)
    current_file = os.path.abspath(os.path.join(working_directory, file_path))

    if (not current_file.startswith(f"{pwd}")):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(current_file):
            with open(current_file, 'w') as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
        with open(current_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Cannot create file {file_path} - {e}'
    

        

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite content to the file provided.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to get the contents of the file from.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content you are to write to the file",
            )
        },
    ),
)