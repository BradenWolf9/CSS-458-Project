import wind as W
import numpy as np
import math

# test createWindField from wind.py to make sure the initial wind vector is 
# in the wind field
# will display output if it fails, so if no output then test past
def test_createWindField_windVector():
    initWindVector = (2,43,483)
    windFieldSize = 52
    wind = W.createWindField(initWindVector, windFieldSize)
    # if any vector on the bottom level is not equal to the inital wind vector
    if any(np.not_equal(wind[0,0,0,:],np.array([2,43,483]))) == True:
        print("Failed to put the initial wind vector in the wind field.")
        
        
# test createWindField from wind.py to make sure the wind field is the correct 
# size
# will display output if it fails, so if no output then test past
def test_createWindField_windFieldSize():
    initWindVector = (2,43,483)
    windFieldSize = 52
    wind = W.createWindField(initWindVector, windFieldSize)
    if len(wind) != 52:
        print("Failed to set the correct size of the wind field.")

     
# test applyMagScale from wind.py to check magnitude scaled from bottom level 
# to top
# will display output if it fails, so if no output then test past
def test_applyMagScale_magScale():
    initWindVector = (2,5,1)
    windFieldSize = 10
    wind = W.createWindField(initWindVector, windFieldSize)
    # magnitude of vector at top should be twice as much as magnitud at bottom
    heightMagScale = 2
    wind = W.applyMagScale(wind, heightMagScale, windFieldSize)
    # if a vector's magnitude on top level is not twice as much as 
    # vector's magnitude on bottom
    # uses distance formula to calc magnitude
    if math.sqrt(wind[9,0,0,0]**2 + wind[9,0,0,1]**2 + wind[9,0,0,2]**2) != \
       (math.sqrt(wind[0,0,0,0]**2 + wind[0,0,0,1]**2 + wind[0,0,0,2]**2)) * 2:
        print("Failed to scale the magnitude correctly.")


# test applyStdDev from wind.py to check standard devation 
def test_applyStdDev_stdDev():
    initWindVector = (5,5,5)
    windFieldSize = 100
    wind = W.createWindField(initWindVector, windFieldSize)
    windStdDev = 1
    # std dev at bottom should be same at top with scaling factor of 1
    heightStdDevScale = 1
    wind = W.applyStdDev(wind, windStdDev, heightStdDevScale, windFieldSize)
    less = np.less(wind, 3)
    greater = np.greater(wind, 7)
    # if any value in wind less than 3 or greater than 7
    if less.any() or greater.any():
        print("Failed to set standard deviation correctly.")
    

# executes all the tests
def execute():
    test_createWindField_windVector()
    test_createWindField_windFieldSize()
    test_applyMagScale_magScale()
    test_applyStdDev_stdDev()


if __name__ ==  '__main__':
    execute()
