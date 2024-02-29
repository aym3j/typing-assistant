# Typing Assistant

This is a simple Typing Assistant utilizing Ollama and `gemma-2b` form Google that fixes typos and grammatical in your text.

## Usage/Examples

To use this Typing Assistant:

1. Install the required libraries from `requirements.txt`.

   ```
   pip install -r requirements.txt
   ```

2. Ensure that Ollama is installed on your machine and run it with `gemma:2b-instruct-q2_K` model.

   ```
   ollama run gemma:2b-instruct-q2_K
   ```

3. Execute the `main.py` script.
   ```
   python3 main.py
   ```
4. Press `F9` to fix typos on your current line or `F10` for selected text.
