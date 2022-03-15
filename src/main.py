import time
from bmp280 import BMP280

try:
       from smbus2 import SMBus
except ImportError:
       from smbus import SMBus


bus1 = SMBus(1) #Hay que crear otro bus mas para el otro sensor
bmp280 = BMP280(i2c_dev=bus1)
"""
bus2 = 
ultravioleta = 
"""
