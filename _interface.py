from _dataLOG    import DataLOG
from _resolution import *
from _parserLOG  import Parser_LOG

from numpy import zeros
from numpy import set_printoptions



set_printoptions( formatter={'float_kind': lambda x: "{0:0.6f}".format(x)} )


def Interface_LOG( DB: DataLOG ):

    while DB.recording:

        if DB.flag:

            idxn = DB.idxn-1

            rxData = DB.rxData[:,idxn]

            data = Parser_LOG( rxData )

            time = data[0]
            posL = data[1]
            posN = data[2][0]
            velN = data[2][1]
            attB = data[2][2]
            anvB = data[2][3]
            thrust = data[3]
            Mass = data[4]
            act  = data[5]
            target = data[6]