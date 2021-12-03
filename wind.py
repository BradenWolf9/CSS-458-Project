
import numpy as np

##################################################################
#global variables#
rocketMass = 5
#                 z y x
initWindVector = (4,2,6)
windFieldSize = 100 # 100x100x100
initRocketAngle = (1,0,0)
windStdDev = 1.0
heightScale = 1 # i.e. if heightScale = 2, stddev at top is twice stddev at bottom
vectorDims = 3
##################################################################

def createWindField(initWindVector, windFieldSize, vectorDims):
    wind = np.zeros((windFieldSize, windFieldSize, windFieldSize, vectorDims))
    wind[:,:,:,:] = initWindVector[:]
    return wind
    
def applyStdDev(wind, windStdDev, windFieldSize, vectorDims):
    wind += np.random.uniform(low=-(windStdDev*2.0), 
                              high=(windStdDev*2.0),
                              size=(windFieldSize, windFieldSize, windFieldSize, vectorDims))
    return wind



if __name__ == '__main__':
    wind = createWindField(initWindVector, windFieldSize, vectorDims)
    print(wind)
    wind = applyStdDev(wind, windStdDev, windFieldSize, vectorDims)
    print(wind)
    print(np.max(wind))
