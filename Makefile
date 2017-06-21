build:
	ampy -p COM3 put main.py

run: build
	ampy -p COM3 run main.py
