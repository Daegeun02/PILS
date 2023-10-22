from serial import Serial

from _dataLOG import DataLOG

from numpy import frombuffer
from numpy import uint8



def Logger_LOG( serial: Serial, DB: DataLOG ):

    hdrf = 0

    rxData = DB.rxData

    serial.timeout = 0.001

    while ( DB.recording and DB.idxn != DB.n ):

        idxn = DB.idxn

        if ( hdrf == 2 ):
            byte = serial.read(60)
            rxbf = frombuffer( byte, uint8 )
            hdrf = 0

            if ( len( rxbf ) == 60 ):
                rxData[:,idxn] = rxbf

            DB.idxn += 1

            if ( DB.idxn == DB.n ):
                DB.recording = False

        elif ( hdrf == 0 ):
            byte = serial.read()
            if ( byte == b'\x4C' ):
                hdrf = 1

        elif ( hdrf == 1 ):
            byte = serial.read()
            if ( byte == b'\x4D' ):
                hdrf = 2

        else:
            hdrf = 0
