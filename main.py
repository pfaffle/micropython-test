import machine
import socket
import network
from my_utils import wifi

def turn_off_ap():
    print('Turning off access point interface')
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

def connect_to_wifi(essid, password):
    print('Connecting to wifi network: %s' % essid)
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(essid, password)
    while not sta_if.isconnected():
        pass

def http_get(url):
    print('Getting url %s' % url)
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

turn_off_ap()
connect_to_wifi(wifi.get_essid(), wifi.get_password())
http_get('http://micropython.org/ks/test.html')
