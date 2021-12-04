
import numpy as np
import math

##############################################################################
# user defined variables #
rocketMass = 5
#                 z y x
initWindVector = (4,2,6)
windFieldSize = 100 # 100x100x100
initRocketAngle = (1,0,0)
windStdDev = 1.0
heightStdDevScale = 2 # i.e. if heightStdDevScale = 2, stddev at top level is twice stddev at bottom level
heightMagScale = 2 # i.e if heightMagScale = 2, magnitude of vectors at top level is twice the magnitude of vectors at bottom level
##############################################################################
# consts #
DIMS = 3
##############################################################################

# creates wind field with each 3D cell set to the given wind vector
def createWindField(initWindVector, windFieldSize, DIMS):
    wind = np.zeros((windFieldSize, windFieldSize, windFieldSize, DIMS))
    wind[:,:,:,:] = initWindVector[:]
    return wind
    
# applies magnitude scaling to the height of the wind field
# pre: 3D wind field is created with only initial wind vector in each cell
def applyMagScale(wind, heightMagScale, windFieldSize):
    magStep = (heightMagScale - 1) / (windFieldSize - 1)
    # distance formula
    origMag = math.sqrt(wind[0,0,0,0]**2 + wind[0,0,0,1]**2 + wind[0,0,0,2]**2)
    # for each height level
    for height in range(0, windFieldSize):
        # to get desired magnitude, multiply each element of vector by scale
        #   at the current height
        # scale at height level 0 equals 1
        wind[height,:,:,:] *= 1 + height * magStep
    return wind

# randomizes the wind vectors by using the given standard deviation and 
# height scaling
# pre: 3D wind field is created with height scaling applied
# post: 3D wind field is altered to be random according to given standard
#       deviation and standard deviation is scaled with height according to 
#       the given scaling
def applyStdDev(wind, windStdDev, heightStdDevScale, windFieldSize, DIMS):
    stdDevStep = ((windStdDev * heightStdDevScale) - windStdDev) / windFieldSize
    # for each height level
    for height in range(0,windFieldSize):
        wind[height,:,:,:] += np.random.uniform(low=-((windStdDev + (stdDevStep * height)) * 2),
                                                high=((windStdDev + (stdDevStep * height)) * 2),
                                                size=(windFieldSize, windFieldSize, DIMS))
    return wind
    

if __name__ == '__main__':
    wind = createWindField(initWindVector, windFieldSize, DIMS)
    wind = applyMagScale(wind, heightMagScale, windFieldSize)
    wind = applyStdDev(wind, windStdDev, heightStdDevScale, windFieldSize, DIMS)
    print(wind)
