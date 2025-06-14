import os
from google.genai import types


def get_files_info(working_directory, directory=None):
    
    if directory is None:
        return f"Error: You need to input a directory"
    
    pwd = os.path.abspath(working_directory)
    current_directory = os.path.abspath(os.path.join(working_directory, directory))
    
    if (not current_directory.startswith(f"{pwd}")):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(current_directory):
        return f'Error: "{directory}" is not a directory'
        
    try:
        dir_content = os.listdir(current_directory)

        content_list = []
        for content in dir_content:
            file_path = os.path.join(current_directory, content)
            content_list.append(f"- {content}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")

        return "\n".join(content_list)

    except Exception as e:
        return f"Error: The error is {e}"





schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


