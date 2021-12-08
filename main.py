import rocket as R
import wind as W  
import tests as T
import numpy as N

##############################################################################
initWindVector = (0,0,0) # Initial wind velocity (up, north, east), in meters/sec
windFieldSize = 200 # Length of one side of wind field, in meters
windStdDev = 0 # Standard deviation of initial wind velocity (meters/sec)
heightStdDevScale = 2 # i.e. if heightStdDevScale = 2, stddev at top level is twice stddev at bottom level
heightMagScale = 2 # i.e if heightMagScale = 2, magnitude of vectors at top level is twice the magnitude of vectors at bottom level

initRocketAngle = (1.0,0.0,0.0)  # Rocket direction unit vector (up, north, east)
initialPosition = N.array([0,windFieldSize/2,windFieldSize/2]) # Rocket position, in meters

timeSlice = .05 # Simulation time slice, in seconds

tests = True # valid entries are True (runs tests) or False
##############################################################################

if __name__ == '__main__':
    # Generate a wind vector with initial velocity + randomness applied
    wind = W.createWind(initWindVector, windFieldSize, heightMagScale, windStdDev, heightStdDevScale)
    # Run the simulation and calculate positions
    positions = R.launchRocket(initRocketAngle, wind, timeSlice, initialPosition)
    # Execute tests if enabled
    if tests:
        T.execute()
  
