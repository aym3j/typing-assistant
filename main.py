from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time
import httpx
from string import Template

controller = Controller()

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate" 
OLLAMA_CONFIG = {
    "model": "gemma:2b-instruct-q2_K",
    "prompt":"Why is the sky blue?",
    "stream": False,
}

PROMT_TEMPLATE = Template(
    """Fix all typos and grammatical errors in the following text, but preserve all newlines and formatting:
    
    $text
    
    return the fixed text. don't include a preamble or any other text."""
)

def fix_selected_text(text):
    OLLAMA_CONFIG["prompt"] = PROMT_TEMPLATE.substitute(text=text)
    
    # Send text to OLLAMA
    response = httpx.post(OLLAMA_ENDPOINT,
                          json=OLLAMA_CONFIG,
                          headers={"Content-Type": "application/json"},
                          timeout=10)
    
    response.raise_for_status()
    
    return response.json()["response"]



def fix_selection():
    # Copy to clipboard
    with controller.pressed(Key.ctrl):
        controller.tap('c')

    # Get text from clipboard
    time.sleep(0.1)
    text = pyperclip.paste()


    # Fix text
    fixed_text = fix_selected_text(text)

    # Paste text to clipboard
    pyperclip.copy(fixed_text)
    time.sleep(0.1)

    # Paste text to selected area
    with controller.pressed(Key.ctrl):
        controller.tap('v')

def fix_current_line():
    # Select current line
    controller.tap(Key.home)
    with controller.pressed(Key.shift):
        controller.tap(Key.end)
    
    fix_selection()


def on_activate_f9():
    fix_current_line()

def on_activate_f10():
    fix_selection()

f9_key = str(Key.f9.value)
f10_key = str(Key.f10.value)

with keyboard.GlobalHotKeys({
        f9_key: on_activate_f9,
        f10_key: on_activate_f10
}) as h:
    h.join()
