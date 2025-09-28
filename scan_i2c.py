from machine import Pin, I2C

i2c = I2C(0, sda=Pin(7), scl=Pin(11), freq=100000)

print('Scanning I2C bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C devices found.")
else:
    print('Found I2C devices at addresses:')
    for device in devices:
        print("Decimal address: ",device," | Hexa address: ",hex(device))
