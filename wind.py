import numpy as np

##################################################################
#global variables#
rocketMass = 5
#                 z y x
initWindVector = (4,2,6)
windFieldSize = 100 # 100x100x100
initRocketAngle = (1,0,0)
windStdDev = 0
heightScale = 1 # i.e. if heightScale = 2, stddev at top is twice stddev at bottom
##################################################################

def createWindField(initWindVector, windFieldSize, windStdDev, heightScale):
    wind = np.zeros((windFieldSize, windFieldSize, windFieldSize, 3))
    wind[:,:,:,:] = initWindVector[:]
    return wind
    
print(createWindField(initWindVector, windFieldSize, windStdDev, heightScale))
