MP_PORT ?= COM3

.PHONY: build my_utils run clean

build: my_utils
	ampy -p ${MP_PORT} put main.py

my_utils: my_utils/secrets.py
	ampy -p ${MP_PORT} put my_utils

run: build
	ampy -p ${MP_PORT} run main.py

my_utils/secrets.py:
	@echo 'WIFI_ESSID="${WIFI_ESSID}"' > my_utils/secrets.py
	@echo 'WIFI_PASSWORD="${WIFI_PASSWORD}"' >> my_utils/secrets.py

clean:
	rm my_utils/secrets.py
