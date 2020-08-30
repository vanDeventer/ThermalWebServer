from flask import Flask,render_template
import serial
import datetime

ser = serial.Serial("/dev/ttyACM0",9600)
ser.flush
app = Flask(__name__)

  
@app.route('/')
def root():
     now = datetime.datetime.now()
     timeString = now.strftime("%Y-%m-%d %H:%M")
     temperature_r = ser.read(5).decode('utf-8')
     templateData = {
         'title' : 'Max''s web page',
         'temperature' : temperature_r,
         'time' : timeString
     }
     return render_template('index.html', **templateData)   
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 80, debug = True)