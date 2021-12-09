import rocket as R
import wind as W  
import tests as T
import numpy as N
import visualize as V

##############################################################################
# WIND PROPERTIES
initWindVector = (0,1,0) # Initial wind velocity (up, north, east), in meters/sec
windFieldSize = 300 # Length of one side of wind field, in meters
windStdDev = 1 # Standard deviation of initial wind velocity (meters/sec)
heightStdDevScale = 3 # i.e. if heightStdDevScale = 2, stddev at top level is twice stddev at bottom level
heightMagScale = 2 # i.e if heightMagScale = 2, magnitude of vectors at top level is twice the magnitude of vectors at bottom level

# ROCKET PROPERTIES
initRocketAngle = (1.0,0.0,0.0)  # Rocket direction unit vector (up, north, east)
initialPosition = N.array([0,windFieldSize/2,windFieldSize/2]) # Rocket position, in meters


# SIMULATION PROPERTIES
timeSlice = .05 # Simulation time slice, in seconds
numSimulations = 100
##############################################################################

if __name__ == '__main__':
    
    # Create simulations array
    simulations = []
    
    # Generate a wind vector with initial velocity
    wind = W.createWind(initWindVector, windFieldSize, heightMagScale, windStdDev, heightStdDevScale)
    # Calculate deviation step for when we apply STDEV
    stdDevStep = ((windStdDev * heightStdDevScale) - windStdDev) / windFieldSize
    
    # Run simulations
    for i in range(numSimulations):
        # Run the simulation and calculate positions
        positions = R.launchRocket(initRocketAngle, wind, windStdDev, stdDevStep, timeSlice, initialPosition)
        # Append positions
        simulations.append(positions)
    
    # Visualize the launch
    simulations = N.array(simulations)
    V.visualizeFlightPath(simulations, windFieldSize, timeSlice)
    #V.visualizeTimeData(simulations, windFieldSize, timeSlice)
  
