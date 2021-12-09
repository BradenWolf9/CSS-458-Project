import numpy as N
##############################################################################
totalEngineImpulse = 5 # in Newton seconds
engineDuration = 1.6 # in seconds
rocketMass = .085 # Rocket mass, in kilograms
surfaceArea = .025398 #in m^2
airDensity = 1.229 # in kg/m^3
##############################################################################


def launchRocket( initRocketAngle, wind, windStdDev, stdDevStep, timeSlice, initPosition):
    # Calculate propulsion acceleration vector
    propulsionAccel = getPropulsionAccel(rocketMass, initRocketAngle, totalEngineImpulse, engineDuration)
    # Get gravity acceleration vector (9.8m/s)
    gravity = N.array([-9.8, 0.0, 0.0]) # in m/s^2
    
    # Set rocket position and velocity vectors
    rocketPosition = initPosition
    rocketVector = N.array([0.0,0.0,0.0])
    
    # Declare some simulation state variables
    timeElapsed = 0.0
    pDeployed = False
    positions = initPosition
    
    # Until the rocket hits the ground
    while(rocketPosition[0] >= 0.0):
        # Update the rocket velocity & position
        rocketVector, rocketPosition = rocketStep(rocketVector, rocketPosition, propulsionAccel, wind, windStdDev, stdDevStep, gravity, timeSlice)
        # Update timeElapsed
        timeElapsed = timeElapsed + timeSlice
        # If rocket is in the air, store the position 
        if(rocketPosition[0] >= 0.0):
            positions = N.vstack((positions,rocketPosition))
            
        # If the rocket's engine runs out
        if timeElapsed > engineDuration: 
            propulsionAccel = (0.0,0.0,0.0) # Turn off acceleration by propulsion
        
        # If the rocket starts falling, deploy parachute
        if (rocketVector[0] < 0.0) and (pDeployed == False):
            gravity = gravity * 0.1 # Parachute acts as 90% negating force to gravity
            pDeployed = True
            
    # Return simulation positions
    return positions
    
def rocketStep(rocketVector, rocketPosition, propulsionAccel, wind, windStdDev, stdDevStep, gravity, timeSlice ):
    # Wind vector
    worldSize = wind.shape[0]
    rocketY = max(0, min(worldSize - 1, int(rocketPosition[0])))
    rocketN = max(0, min(worldSize - 1, int(rocketPosition[1])))
    rocketE = max(0, min(worldSize - 1, int(rocketPosition[2])))
    windSpeed = wind[rocketY, rocketN, rocketE]
    
    # Get new acceleration using gravity, propulsion, and wind vector
    newAccel = N.array([gravity[0] + propulsionAccel[0] + getWindAccel(windSpeed, windStdDev, stdDevStep, int(rocketPosition[0]))[0],  \
                gravity[1] + propulsionAccel[1] + getWindAccel(windSpeed, windStdDev, stdDevStep, int(rocketPosition[0]))[1],   \
                gravity[2] + propulsionAccel[2] + getWindAccel(windSpeed, windStdDev, stdDevStep, int(rocketPosition[0]))[2]])
    
    
    # Update rocket velocity using physics equation Vf=Vi+a*t
    newRocketVector = rocketVector + (newAccel * timeSlice )

    # Update rocket position using physics equation d=Vi*t+0.5*a*t^2
    newPosition = rocketPosition + (rocketVector * timeSlice) + (.5 * (newAccel * timeSlice * timeSlice))
    return newRocketVector , newPosition

def getPropulsionAccel(mass, angle, impulse, duration):
    # Impulse = force * time.
    avgPropForce = impulse / duration
    # Acceleration = force / mass
    avgPropAccel = avgPropForce / mass
    # Acceleration with direction
    normalisedPropulsion = (angle[0] * avgPropAccel, \
                            angle[1] * avgPropAccel, \
                                angle[2] * avgPropAccel)
    return normalisedPropulsion

def getWindAccel(windSpeed, windStdDev, stdDevStep, height):
    
    # Copy the wind speed vector
    windSpeedCopy = N.copy(windSpeed)
    
    # Apply a random normal distribution (moved out of wind.py for efficiency)
    windSpeedCopy += N.random.normal(
            loc = 0, \
            scale = windStdDev + stdDevStep * height, \
            size = (3,))
    
    # Calculate the wind force
    windForce = surfaceArea * airDensity * windSpeedCopy
    return windForce / rocketMass