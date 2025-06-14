# agentic-python

A command-line AI coding agent powered by Google Gemini, designed to interact with your codebase using function calls. The agent can:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

---

## Features

- **Function Call Planning:** The agent interprets user prompts and generates a plan using available function calls.
- **Secure File Access:** All file operations are restricted to a configurable working directory.
- **Extensible Functions:** Add new tools by implementing Python functions and registering their schemas.
- **Verbose Mode:** Use `--verbose` to see detailed logs of prompts, responses, and function calls.

---

## Usage

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Set up your environment:**
   
   Copy `.env.sample` to your `.env` and add your gemini api key. Steps to get the [api key](https://ai.google.dev/gemini-api/docs/api-key).

3. **Run the agent:**
   ```
   python3 main.py "How do I build a calculator app in Python?"
   ```

---

## Project Structure

- `main.py` - Entry point for the agent
- `function_calls.py` - Registers available function tools and dispatches function calls.
- `functions` - Directory that contains implementations for file listing, reading, writing, and Python execution.
- `prompts.py` - System prompt for the LLM.
- `config.py` - Configuration, including working directory and limits.
- `calculator` - sample workspace for the agent and not part of the agents core logic.
- `requirements.txt` - Python dependencies.

---

## Security

- All file operations are sandboxed to the working directory specified in `config.py`.
- Paths are validated to prevent directory traversal.

---

## Extending

- Fix harder and more complex bugs
- Refactor sections of code
- Add entirely new features
- Giving it more functions to call

## ⚠️ Warning

This agent can read, write, and execute code within its working directory. **Even with sandboxing, there are security risks.** Do not give the agent access to sensitive files or directories, and do not share this code with others for their use. Like commercial agentic tools, this project is not perfectly secure — use at your own risk.