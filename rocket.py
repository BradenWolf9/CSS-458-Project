import numpy as N
##############################################################################
# user defined variables #
rocketMass = .085 # in kg
#                 z y x
initWindVector = (4,2,6)
windFieldSize = 100 # 100x100x100
initRocketAngle = (1.0,0.0,0.0)  #must be a normalized vector
windStdDev = 1.0
heightStdDevScale = 2 # i.e. if heightStdDevScale = 2, stddev at top level is twice stddev at bottom level
heightMagScale = 2 # i.e if heightMagScale = 2, magnitude of vectors at top level is twice the magnitude of vectors at bottom level

totalEngineImpulse = 10 # in Newtons
engineDuration = 1.6 # in seconds
timeSlice = .05 # in seconds

initialPosition = (0,windFieldSize/2,windFieldSize/2)
surfaceArea = .025398 #in m^2
airDensity = 1.229 # in kg/m^3
##############################################################################




def launchRocket( initRocketAngle, wind, timeSlice, initPosition, surfaceArea):
    
    propulsionAccel = getPropulsionAccel(rocketMass, initRocketAngle, totalEngineImpulse, engineDuration)
    gravity = (-9.8, 0.0, 0.0) # in m/s^2
    rocketPosition = initialPosition
    rocketVector = (0.0,0.0,0.0)
    timeElapsed = 0.0
    rocketVector, rocketPosition = rocketStep(rocketVector, rocketPosition, propulsionAccel, wind, gravity)
    timeElapsed = timeElapsed + timeSlice
    while(rocketPosition[0] >= 0.0):
        rocketVector, rocketPosition = rocketStep(rocketVector, rocketPosition, propulsionAccel, wind, gravity)
        timeElapsed = timeElapsed + timeSlice
        if timeElapsed > engineDuration : 
            propulsionAccel = (0.0,0.0,0.0)
        if rocketVector[0] < 0.0:
            gravity = (-.98, 0.0, 0.0)
            
    
def rocketStep(rocketVector, rocketPosition, propulsionAccel, wind, gravity ):
    newAccel = (gravity[0] + propulsionAccel[0] + getWindAccel(wind[int(rocketPosition[0]) , int(rocketPosition[1]) , int(rocketPosition[2]) , 0]),  \
                gravity[1] + propulsionAccel[1] + getWindAccel(wind[int(rocketPosition[0]) , int(rocketPosition[1]) , int(rocketPosition[2]) , 1]),   \
                gravity[2] + propulsionAccel[2] + getWindAccel(wind[int(rocketPosition[0]) , int(rocketPosition[1]) , int(rocketPosition[2]) , 2]))
    newRocketVector = (0.0,0.0,0.0)
    newRocketVector[0] = rocketVector[0] + (newAccel[0] * timeSlice)
    newRocketVector[1] = rocketVector[1] + (newAccel[1] * timeSlice)
    newRocketVector[2] = rocketVector[2] + (newAccel[2] * timeSlice)
    
    newPosition = (0.0,0.0,0.0)
    newPosition[0] = rocketPosition[0] + newRocketVector[0]
    newPosition[1] = rocketPosition[1] + newRocketVector[1]
    newPosition[2] = rocketPosition[2] + newRocketVector[2]
    return newRocketVector , newPosition
    
    


def getPropulsionAccel(mass, angle, impulse, duration):
    avgPropForce = impulse / duration
    avgPropAccel = avgPropForce / mass
    normalisedPropulsion = (angle[0] * avgPropAccel, \
                            angle[1] * avgPropAccel, \
                                angle[2] * avgPropAccel)
    return normalisedPropulsion

def getWindAccel(windSpeed):
    windForce = surfaceArea * airDensity * windSpeed
    return windForce / rocketMass

