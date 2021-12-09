import numpy as N
import math
##############################################################################
totalEngineImpulse = 5 # in Newton seconds
engineDuration = .8 # in seconds
rocketMass = .085 # Rocket mass, in kilograms
rLength = .747 # Rocket length in meters
rDiameter = .034 # Rocket diameter in meters
parachuteDiameter = .457 # Parachute Diameter in meters
surfaceAreaSide = rLength * rDiameter #in m^2
pSurfaceArea = (math.pi * ((parachuteDiameter/2) **2))
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
    parachuteTerminalV = getParachuteTerminalV()
    
    # Adjusts engine duration to less reliable engines. Maxes out at engineDuration
    adjEngineDuration = N.random.normal(engineDuration, engineDuration/10)
    while adjEngineDuration > engineDuration:
        adjEngineDuration = N.random.normal(engineDuration, engineDuration/10)
        
    # Adds in variability to parachute deploy time. Parachute will deploy somewhere between 0m/s and -5m/s
    parachuteTrigger = (-5 * N.random.random()) - 5
    
    # Until the rocket hits the ground
    while(rocketPosition[0] >= 0.0):
        # Update the rocket velocity & position
        rocketVector, rocketPosition = rocketStep(rocketVector, rocketPosition, propulsionAccel, wind, windStdDev, stdDevStep, gravity, timeSlice, pDeployed, parachuteTerminalV)
        # Update timeElapsed
        timeElapsed = timeElapsed + timeSlice
        # If rocket is in the air, store the position 
        if(rocketPosition[0] >= 0.0):
            positions = N.vstack((positions,rocketPosition))
            
        # If the rocket's engine runs out
        if timeElapsed > adjEngineDuration: 
            propulsionAccel = (0.0,0.0,0.0) # Turn off acceleration by propulsion
        
        # If the rocket starts falling, deploy parachute
        if (rocketVector[0] < parachuteTrigger) and (pDeployed == False):
            #gravity = gravity * 0.1 # Parachute acts as 90% negating force to gravity
            pDeployed = True
            
    # Return simulation positions
    return positions
    
def rocketStep(rocketVector, rocketPosition, propulsionAccel, wind, windStdDev, stdDevStep, gravity, timeSlice, pDeployed, parachuteTerminalV ):
    # Wind vector
    worldSize = wind.shape[0]
    rocketY = max(0, min(worldSize - 1, int(rocketPosition[0])))
    rocketN = max(0, min(worldSize - 1, int(rocketPosition[1])))
    rocketE = max(0, min(worldSize - 1, int(rocketPosition[2])))
    
    #adds variability to the wind field based on a normal distribution
    #moved out of wind.py for efficiency
    windSpeed = N.copy(wind[rocketY, rocketN, rocketE])
    windSpeed += N.random.normal(
            loc = 0, \
            scale = windStdDev + stdDevStep * rocketPosition[0], \
            size = (3,))
    
    # Get new acceleration using gravity, propulsion, and wind vector
    newAccel = N.array([gravity[0] + propulsionAccel[0] + getWindAccel(windSpeed[0]),  \
                gravity[1] + propulsionAccel[1] + getWindAccel(windSpeed[1]),   \
                gravity[2] + propulsionAccel[2] + getWindAccel(windSpeed[2])])
    
    
    # Update rocket velocity using physics equation Vf=Vi+a*t
    newRocketVector = rocketVector + (newAccel * timeSlice )
    
    #if the parachute is deployed, caps the downwars speed to the terminal velocity
    if pDeployed == True:
        #terminal velocity
        if newRocketVector[0] < parachuteTerminalV:
            newRocketVector[0] = parachuteTerminalV
        #caps lateral velocity of our rocket to the speed of the wind.
        #rough approximation of air resistance pushing against the acceleration from wind
        if windSpeed[1] < 0:
            if newRocketVector[1] < windSpeed[1]:
                newRocketVector[1] = windSpeed[1]
        else:
            if newRocketVector[1] > windSpeed[1]:
                newRocketVector[1] = windSpeed[1]
                
        if windSpeed[2] < 0:
            if newRocketVector[2] < windSpeed[2]:
                newRocketVector[2] = windSpeed[2]
        else:
            if newRocketVector[2] > windSpeed[2]:
                newRocketVector[2] = windSpeed[2]
                

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

def getWindAccel(windSpeed):
    

    
    # Calculate the wind force
    windForce = surfaceAreaSide * airDensity * windSpeed
    
    #Calculate acceleration based on force and mass
    return windForce / rocketMass

#returns the terminal velocity of a rocket according to given variables
def getParachuteTerminalV():
    terminalV =  math.sqrt((2 * rocketMass * 9.8) / (airDensity * pSurfaceArea * .5))
    #flips to negative to represent downward speed
    return -terminalV
