from _resolution import *

from _dataLOG import DataLOG

from numpy import ndarray
from numpy import frombuffer
from numpy import float32, uint16, uint8, int32, int16

from pandas import DataFrame



def _Parser_LOG( data: ndarray ):

    time = frombuffer( data[0:4].tobytes(), float32 )

    Lat = frombuffer( data[ 4: 8].tobytes(), int32 ) * RXRESOLUTION[LAT_RES]
    Lon = frombuffer( data[ 8:12].tobytes(), int32 ) * RXRESOLUTION[LON_RES]
    Alt = frombuffer( data[12:14].tobytes(), int16 ) * RXRESOLUTION[ALT_RES]

    posN = frombuffer( data[14:20].tobytes(), int16 ) * RXRESOLUTION[POS_RES]
    velN = frombuffer( data[20:26].tobytes(), int16 ) * RXRESOLUTION[VEL_RES]
    attB = frombuffer( data[26:32].tobytes(), int16 ) * RXRESOLUTION[ATT_RES]
    anvB = frombuffer( data[32:38].tobytes(), int16 ) * RXRESOLUTION[ANV_RES]

    thrust = frombuffer( data[38:42].tobytes(), uint16 ) * RXRESOLUTION[THR_RES]

    Mass = frombuffer( data[42:46].tobytes(), uint16 ) * RXRESOLUTION[MASS_RES]

    act = frombuffer( data[46:54].tobytes(), uint16 ) * RXRESOLUTION[ACT_RES]

    target = frombuffer( data[54:60].tobytes(), int16 ) * RXRESOLUTION[POS_RES]

    posL = ( Lat, Lon, Alt )
    stat = ( posN, velN, attB, anvB )

    return time, posL, stat, thrust, Mass, act, target


def Parser_LOG( DB: DataLOG, date ):

    idxn = DB.idxn
    Data = DB.rxData

    for idx in range( idxn ):

        buff = _Parser_LOG( Data[:,idx].astype(uint8) )

        DB.time[:,idx] = buff[0]
        DB.posL[0,idx] = buff[1][0]
        DB.posL[1,idx] = buff[1][1]
        DB.posL[2,idx] = buff[1][2]
        DB.posN[:,idx] = buff[2][0]
        DB.velN[:,idx] = buff[2][1]
        DB.attB[:,idx] = buff[2][2]
        DB.anvB[:,idx] = buff[2][3]

        DB.Thrust[:,idx]     = buff[3][0]
        DB.Thrust_CMD[:,idx] = buff[3][1]

        DB.Mass[:,idx]     = buff[4][0]
        DB.Mass_hat[:,idx] = buff[4][1]

        DB.act[0,idx]     = buff[5][0]
        DB.act[1,idx]     = buff[5][1]
        DB.act_CMD[0,idx] = buff[5][2]
        DB.act_CMD[1,idx] = buff[5][3]

        DB.target[:,idx] = buff[6]

    DF = DataFrame(
        {
            'time': DB.time[0,:idxn],

            'posLA': DB.posL[0,:idxn],
            'posLO': DB.posL[1,:idxn],
            'posAL': DB.posL[2,:idxn],
            'pos_N': DB.posN[0,:idxn],
            'pos_E': DB.posN[1,:idxn],
            'pos_D': DB.posN[2,:idxn],
            'vel_N': DB.velN[0,:idxn],
            'vel_E': DB.velN[1,:idxn],
            'vel_D': DB.velN[2,:idxn],
            'att_R': DB.attB[0,:idxn],
            'att_P': DB.attB[1,:idxn],
            'att_Y': DB.attB[2,:idxn],
            'anv_R': DB.anvB[0,:idxn],
            'anv_P': DB.anvB[1,:idxn],
            'anv_Y': DB.anvB[2,:idxn],

            'Thrust_CMD': DB.Thrust_CMD[0,:idxn],
            'Thrust'    : DB.Thrust[0,:idxn],

            'Mass'    : DB.Mass[0,:idxn],
            'Mass_hat': DB.Mass_hat[0,:idxn],

            'Act_X': DB.act[0,:idxn],
            'Act_Y': DB.act[1,:idxn],

            'Act_CMD_X': DB.act_CMD[0,:idxn],
            'Act_CMD_Y': DB.act_CMD[1,:idxn],

            'Target_N': DB.target[0,:idxn],
            'Target_E': DB.target[1,:idxn],
            'Target_D': DB.target[2,:idxn]
        }
    )    

    DF.to_csv( f'./LOG/{date}/log.csv' )
