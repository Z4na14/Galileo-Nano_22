import sys
import sx126x
import threading
import time
import select
import termios
import tty
import busio, board
import adafruit_bmp280 as bmp280
import adafruit_ltr390 as ltr390

old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())

node = sx126x.sx126x(serial_num="/dev/ttyS0", freq=433, addr=0, power=22, rssi=False)

i2c = busio.I2C(board.SCL, board.SDA)
ltr = ltr390.LTR390(i2c)
bmp = bmp280.Adafruit_BMP280_I2C(i2c, 0x76)


def send_deal():
    get_rec = "0,"+"AAA"+" "+str(bmp.temperature)[:7]+" "+str(bmp.pressure)[:8]+" "+str(ltr.uvs)[:4]+" "+str(ltr.light)+" "

    while True:
        rec = sys.stdin.read(1)
        if rec != None:
            if rec == '\x0a': break
            get_rec += rec
            sys.stdout.write(rec)
            sys.stdout.flush()

    get_t = get_rec.split(",")

    node.addr_temp = node.addr
    node.set(node.freq, int(get_t[0]), node.power, node.rssi)
    node.send(get_t[1])
    time.sleep(0.2)
    node.set(node.freq, node.addr_temp, node.power, node.rssi)

    print('\x1b[2A', end='\r')
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print('\x1b[3A', end='\r')


try:
    time.sleep(1)

    while True:

        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            c = sys.stdin.read(1)

            # dectect key Esc
            if c == '\x1b':
                # f.close()
                break
            # dectect key i
            if c == '\x69':
                send_deal()
            sys.stdout.flush()

except:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
