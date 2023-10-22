import matplotlib.pyplot as plt

from pandas import read_csv



def convenience( ax: plt.Axes ):
    ax.tick_params( axis='both', labelsize=7 )
    ax.legend( fontsize=7 )
    ax.grid()

def axis_labeling( ax: plt.Axes, label: str ):
    ax.set_xlabel( label[0] )
    ax.set_ylabel( label[1] )


def plot( date ):

    DF = read_csv( f"./LOG/{date}/log.csv" )

    time = DF['time']
    
    ## delete garbage values
    posLA = DF['posLA'].to_numpy()[time != 0]
    posLO = DF['posLO'].to_numpy()[time != 0]
    posAL = DF['posAL'].to_numpy()[time != 0]

    pos_N = DF['pos_N'].to_numpy()[time != 0]
    pos_E = DF['pos_E'].to_numpy()[time != 0]
    pos_D = DF['pos_D'].to_numpy()[time != 0]

    vel_N = DF['vel_N'].to_numpy()[time != 0]
    vel_E = DF['vel_E'].to_numpy()[time != 0]
    vel_D = DF['vel_D'].to_numpy()[time != 0]

    att_R = DF['att_R'].to_numpy()[time != 0]
    att_P = DF['att_P'].to_numpy()[time != 0]
    att_Y = DF['att_Y'].to_numpy()[time != 0]

    anv_R = DF['anv_R'].to_numpy()[time != 0]
    anv_P = DF['anv_P'].to_numpy()[time != 0]
    anv_Y = DF['anv_Y'].to_numpy()[time != 0]

    Thrust_CMD = DF['Thrust_CMD'].to_numpy()[time != 0]
    Thrust     = DF['Thrust'].to_numpy()[time != 0]

    Mass     = DF['Mass'].to_numpy()[time != 0]
    Mass_hat = DF['Mass_hat'].to_numpy()[time != 0]

    Act_X = DF['Act_X'].to_numpy()[time != 0]
    Act_Y = DF['Act_Y'].to_numpy()[time != 0]

    Act_CMD_X = DF['Act_CMD_X'].to_numpy()[time != 0]
    Act_CMD_Y = DF['Act_CMD_Y'].to_numpy()[time != 0]

    Target_N = DF['Target_N'].to_numpy()[time != 0]
    Target_E = DF['Target_E'].to_numpy()[time != 0]
    Target_D = DF['Target_D'].to_numpy()[time != 0]

    time = time.to_numpy()[time != 0]

    fig = plt.figure( figsize=(14,6) )
    fig.suptitle( "Rocket's position and velocity" )
    
    ax1 = fig.add_subplot( 231 )
    ax1.plot( time, pos_N   , label='position N' )
    ax1.plot( time, Target_N, label='target N' )
    convenience( ax1 )
    axis_labeling( ax1, ('time [s]', 'position N [m]') )

    ax2 = fig.add_subplot( 232 )
    ax2.plot( time, pos_E   , label='position E' )
    ax2.plot( time, Target_E, label='target E' )
    axis_labeling( ax2, ('time [s]', 'position E [m]') )
    convenience( ax2 )

    ax3 = fig.add_subplot( 233 )
    ax3.plot( time, pos_D   , label='position D' )
    ax3.plot( time, Target_D, label='target D' )
    axis_labeling( ax3, ('time [s]', 'position D [m]') )
    convenience( ax3 )

    ax4 = fig.add_subplot( 234 )
    ax4.plot( time, vel_N, label='velocity N' )
    axis_labeling( ax4, ('time [s]', 'velocity N [m/s]') )
    convenience( ax4 )

    ax5 = fig.add_subplot( 235 )
    ax5.plot( time, vel_E, label='velocity E' )
    axis_labeling( ax5, ('time [s]', 'velocity E [m/s]') )
    convenience( ax5 )

    ax6 = fig.add_subplot( 236 )
    ax6.plot( time, vel_D, label='velocity D' )
    axis_labeling( ax6, ('time [s]', 'velocity D [m/s]') )
    convenience( ax6 )

    fig.savefig( f"./LOG/{date}/figure1.png")

    fig = plt.figure( figsize=(14,6) )
    fig.suptitle( "Rocket's attitude and angular velocity" )

    ax1 = fig.add_subplot( 231 )
    ax1.plot( time, att_R, label='roll' )
    axis_labeling( ax1, ('time[s]', 'roll [deg]') )
    convenience( ax1 )

    ax2 = fig.add_subplot( 232 )
    ax2.plot( time, att_P, label='pitch' )
    axis_labeling( ax2, ('time[s]', 'pitch [deg]') )
    convenience( ax2 )

    ax3 = fig.add_subplot( 233 )
    ax3.plot( time, att_Y, label='yaw' )
    axis_labeling( ax3, ('time[s]', 'yaw [deg]') )
    convenience( ax3 )

    ax4 = fig.add_subplot( 234 )
    ax4.plot( time, anv_R, label='roll rate' )
    axis_labeling( ax4, ('time[s]', 'roll rate [deg/s]') )
    convenience( ax4 )

    ax5 = fig.add_subplot( 235 )
    ax5.plot( time, anv_P, label='pitch rate' )
    axis_labeling( ax5, ('time[s]', 'pitch rate [deg/s]') )
    convenience( ax5 )

    ax6 = fig.add_subplot( 236 )
    ax6.plot( time, anv_Y, label='yaw rate' )
    axis_labeling( ax6, ('time[s]', 'yaw rate [deg/s]') )
    convenience( ax6 )

    fig.savefig( f"./LOG/{date}/figure2.png")

    fig = plt.figure( figsize=(14,7) )
    fig.suptitle( "actuator command and response" )

    ax1 = fig.add_subplot( 211 )
    ax1.plot( time, Act_X    , alpha=0.7, label='response X' )
    ax1.plot( time, Act_CMD_X, alpha=0.7, label='command X' )
    axis_labeling( ax1, ('time[s]', 'actuator X [%]') )
    convenience( ax1 )

    ax2 = fig.add_subplot( 212 )
    ax2.plot( time, Act_Y    , alpha=0.7, label='response Y' )
    ax2.plot( time, Act_CMD_Y, alpha=0.7, label='command Y' )
    axis_labeling( ax2, ('time[s]', 'actuator Y [%]') )
    convenience( ax2 )

    fig.savefig( f"./LOG/{date}/figure3.png")

    fig = plt.figure( figsize=(14,5) )
    fig.suptitle( "Thrust and Rocket's Mass" )

    ax1 = fig.add_subplot( 121 )
    ax1.plot( time, Thrust    , alpha=0.7, label='Thrust response' )
    ax1.plot( time, Thrust_CMD, alpha=0.7, label='Thrust command' )
    axis_labeling( ax1, ('time[s]', 'thrust [N]') )
    convenience( ax1 )

    ax2 = fig.add_subplot( 122 )
    ax2.plot( time, Mass    , alpha=0.7, label='Mass by PILS' )
    ax2.plot( time, Mass_hat, alpha=0.7, label='Mass estimated' )
    axis_labeling( ax2, ('time[s]', 'mass [kg]') )
    convenience( ax2 )

    fig.savefig( f"./LOG/{date}/figure4.png")


if __name__ == "__main__":
    date = input( "date >>>\n" )

    plot( date )
