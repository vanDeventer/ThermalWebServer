import os
from flask import Flask, render_template
import serial

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!")

@app.route('/test')
def test():
    return "Hello World!"

@app.route('/temperature')
def temperature():
   return render_template('index.html', message=line)

if __name__ == "__main__":
    ser = serial.Serial('dev/ttyACM0', 9600, timeout=1)
    ser.flush
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
     app.run(host='0.0.0.0', port=80, debug=True)
