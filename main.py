import machine
import time
led = machine.Pin(5, machine.Pin.OUT)
led.on()
time.sleep(1)
led.off()
