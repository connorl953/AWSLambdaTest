from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(5)  # Wait for 5 seconds
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)