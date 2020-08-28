from flask import Flask, render_template
import datetime
import serial

app = Flask(__name__)

@app.route('/')
def root():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    if ser.in_waiting > 0:
        line = ser.readline()
        tLine = u(line.decode('utf-8'))
    ser.close()
    templateData = {
        'title' : 'Max''s web page',
        'time' : timeString,
        'temperature'=tLine
    }
    return render_template('index.html', **templateData)

@app.route('/time')
def dtime():
    now = datetime.datetime.now()
    timeString = now.strftime("%H")
    templateData = {
        'title' : 'Swedish Time',
        'time' : timeString
    }
    return render_template('time.html', **templateData)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
