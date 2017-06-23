micropython-test
===========

This is a test repo I made for experimenting with MicroPython and a ESP8266 microcontroller board.

Right now it makes the board connect to a local wifi network, connect to a website and get a test webpage, printing its content to the console.

license
-----
Apache 2.0

requirements
-----
* A ESP8266 board flashed with MicroPython (I used the latest stable version, 1.9.2 at the time of this writing)
* Python 3.x
* The `ampy` Python module
* Make

usage
-----
* Set environment variables `WIFI_ESSID` and `WIFI_PASSWORD` in your environment; these will be used to configure the board to connect to wifi.
* Set the environment variable `MP_PORT` to the serial port that your device is connected to.
* Run `make run`

contributing/customizing
-----
* Modify main.py to make the board do different things; see MicroPython documentation for what all you can do.
* You can add helper methods to the pseudo Python module `my_utils` in this directory

other resources:
-----
* [MicroPython's website](http://micropython.org)
* [The tutorial I followed](https://github.com/unreproducible/tinysnakes)
