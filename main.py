import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from function_calls import available_functions, call_function
from prompts import system_prompt

def main():
    load_dotenv()
    
    verbose = "--verbose" in sys.argv
    user_input = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not user_input:
        print("AI Code Assistant")
        print('\nUsage: python3 main.py "your prompt here"')
        print('\nEg: python main.py "How do I build a trading bot"')
        sys.exit(1)

    user_prompt = " ".join(user_input)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if verbose:
        print(f"User prompt: {user_prompt}")
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    for i in range(20):
        response = client.models.generate_content(
                model='gemini-2.0-flash-001', contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_prompt)
            )
        
        if verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        for candidate in response.candidates:
            messages.append(candidate.content)

        if not response.function_calls:
            print(response.text)
            break
        
        else:
            function_responses = []

            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part, verbose)

                if (
                    not function_call_result.parts
                    or not function_call_result.parts[0].function_response
                ):
                    raise Exception("empty function call result")
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                function_responses.append(function_call_result.parts[0])
                messages.append(function_call_result)
            
            if not function_responses:
                raise Exception("no function responses generated, exiting.")

if __name__ == "__main__":
    main()



   