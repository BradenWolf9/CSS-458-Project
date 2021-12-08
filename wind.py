
import numpy as np
import math

##############################################################################
# consts #
DIMS = 3
##############################################################################


# creates wind field with each 3D cell set to the given wind vector
# pre: user defined variables are set
# post: 3D wind field is created with only initial wind vector in each cell
# return: 4D array. First element is height, second is north south, third is
#         east west, fourth is 3D vector of height, north south, east west
def createWindField(initWindVector, windFieldSize, DIMS):
    wind = np.zeros((windFieldSize, windFieldSize, windFieldSize, DIMS))
    wind[:,:,:,:] = initWindVector[:]
    return wind

    
# applies magnitude scaling to the height of the wind field
# pre: 3D wind field is created with only initial wind vector in each cell
# post: 3D wind is altered so magnitude of vectors scale with height according
#       to given magnitude scaling
# return: 4D array. First element is height, second is north south, third is
#         east west, fourth is 3D vector of height, north south, east west
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
#       the given standard deviation scaling
# return: 4D array. First element is height, second is north south, third is
#         east west, fourth is 3D vector of height, north south, east west
def applyStdDev(wind, windStdDev, heightStdDevScale, windFieldSize, DIMS):
    stdDevStep = ((windStdDev * heightStdDevScale) - windStdDev) / windFieldSize
    # for each height level
    for height in range(0,windFieldSize):
        wind[height,:,:,:] += np.random.uniform(low=-((windStdDev + (stdDevStep * height)) * 2),
                                                high=((windStdDev + (stdDevStep * height)) * 2),
                                                size=(windFieldSize, windFieldSize, DIMS))
    return wind
    
    
# Combines the creating wind functions into one, so can call one function
# to create wind.
# return: 4D array. First element is height, second is north south, third is
#         east west, fourth is 3D vector of height, north south, east west    
def createWind(initWindVector, windFieldSize, heightMagScale, windStdDev, heightStdDevScale):
    wind = createWindField(initWindVector, windFieldSize, DIMS)
    wind = applyMagScale(wind, heightMagScale, windFieldSize)
    wind = applyStdDev(wind, windStdDev, heightStdDevScale, windFieldSize, DIMS)
    return wind
    

if __name__ == '__main__':
    wind = createWindField(initWindVector, windFieldSize, DIMS)
    wind = applyMagScale(wind, heightMagScale, windFieldSize)
    wind = applyStdDev(wind, windStdDev, heightStdDevScale, windFieldSize, DIMS)
    print(wind)
