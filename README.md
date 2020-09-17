# Temperature Web Server

The idea is to have a simple web server that shows temperature.
The web server is hosted by a Raspberry Pi and based on Python's Flask library.
The temperature sensor is connected to one of the analog to digital converters on an Arduion Uno.
The Arduino and Raspberry Pi are connected via a USB cable.

A Pi camera is also used.
A new picture is taken every hour using ```cron``` and ```raspistill```.
The use of Flask's render_template requries that the picture is stored in a directory called *static*, which is at the same level as the *templates* directory.

To start the server in the background start ```screen``` and type
```sudo python3 nServer.py```
To return to the shell, type ```Ctrl + A``` and then```D```. It might not work the first time. To return to that "screen", type ```screen -r```.
