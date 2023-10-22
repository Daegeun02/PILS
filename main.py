from threading import Thread

from os import system

from _logger    import Logger_LOG
from _dataLOG   import DataLOG
from _parserLOG import Parser_LOG

from serial import Serial

from numpy import save

import datetime



port = '/dev/tty.usbserial-1140'
baud = 115200

serial = Serial( port, baud, timeout=0.1 )
DB     = DataLOG( 42000 )


if __name__ == "__main__":

    d    = datetime.datetime.now()
    date = f"{d.year}-{d.month:02}-{d.day:02}-{d.hour:02}-{d.minute:02}-{d.second:02}"

    system( f'cd ./LOG && mkdir {date}' )

    print( f"{date}" )

    thread = Thread( target=Logger_LOG, args=[ serial, DB ], daemon=True )
    thread.start()

    input( "press enter to finish Logging" )

    DB.recording = False

    thread.join()

    save( f"./LOG/{date}/raw", DB.rxData )

    Parser_LOG( DB, date )

