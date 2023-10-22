from serial import Serial

port = '/dev/tty.usbserial-140'
baud = 115200

serial = Serial( port, baud, timeout=0.003 )

while True:

    print( serial.read() )
