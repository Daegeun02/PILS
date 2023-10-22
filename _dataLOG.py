from numpy import zeros



class DataLOG:

    def __init__( self, n ):

        self.rxData = zeros((60,n))

        self.time = zeros((1,n))

        self.posL = zeros((3,n))
        self.posN = zeros((3,n))
        self.velN = zeros((3,n))
        self.attB = zeros((3,n))
        self.anvB = zeros((3,n))

        self.Thrust     = zeros((1,n))
        self.Thrust_CMD = zeros((1,n))

        self.Mass     = zeros((1,n))
        self.Mass_hat = zeros((1,n))

        self.act     = zeros((2,n))
        self.act_CMD = zeros((2,n))

        self.target = zeros((3,n))

        self.idxn = 0

        self.n = n

        self.recording = True
