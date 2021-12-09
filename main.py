import rocket as R
import wind as W  
import tests as T
import numpy as N
import visualize

##############################################################################
initWindVector = (0,0,-3) # Initial wind velocity (up, north, east), in meters/sec
windFieldSize = 500 # Length of one side of wind field, in meters
windStdDev = 3 # Standard deviation of initial wind velocity (meters/sec)
heightStdDevScale = 3 # i.e. if heightStdDevScale = 2, stddev at top level is twice stddev at bottom level
heightMagScale = 2 # i.e if heightMagScale = 2, magnitude of vectors at top level is twice the magnitude of vectors at bottom level

initRocketAngle = (1.0,0.0,0.0)  # Rocket direction unit vector (up, north, east)
initialPosition = N.array([0,windFieldSize/2,windFieldSize/2]) # Rocket position, in meters

timeSlice = .05 # Simulation time slice, in seconds
numSimulations = 500
tests = True # valid entries are True (runs tests) or False
##############################################################################

if __name__ == '__main__':
    # Execute tests if enabled
    if tests:
        T.execute()
        pass
    
    # Do simulations
    simulations = []
    
    # Generate a wind vector with initial velocity
    wind = W.createWind(initWindVector, windFieldSize, heightMagScale, windStdDev, heightStdDevScale)
    stdDevStep = ((windStdDev * heightStdDevScale) - windStdDev) / windFieldSize
    
    for i in range(numSimulations):
        # Run the simulation and calculate positions
        positions = R.launchRocket(initRocketAngle, wind, windStdDev, stdDevStep, timeSlice, initialPosition)
        # Append positions
        simulations.append(positions)
    
    # Visualize the launch
    #visualize.visHeightVsDisplacement2D(N.array(simulations), initialPosition)
    #visualize.visRocketPath3D(N.array(simulations), windFieldSize)
    #visualize.visDisplacementChance2D(N.array(simulations), windFieldSize, 100)
    visualize.visAllPlots(N.array(simulations), windFieldSize, 50, initialPosition)

  
