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

totalEngineImpulse = 5 # in Newtons
engineDuration = 1.6 # in seconds
timeSlice = .05 # in seconds


surfaceArea = .025398 #in m^2
airDensity = 1.229 # in kg/m^3
##############################################################################




def launchRocket( initRocketAngle, wind, timeSlice, initPosition):
    
    propulsionAccel = getPropulsionAccel(rocketMass, initRocketAngle, totalEngineImpulse, engineDuration)
    gravity = N.array([-9.8, 0.0, 0.0]) # in m/s^2
    rocketPosition = initPosition
    rocketVector = N.array([0.0,0.0,0.0])
    timeElapsed = 0.0
    pDeployed = False
    positions = initPosition
    while(rocketPosition[0] >= 0.0):
        rocketVector, rocketPosition = rocketStep(rocketVector, rocketPosition, propulsionAccel, wind, gravity)
        timeElapsed = timeElapsed + timeSlice
        if(rocketPosition[0] >= 0.0):
            positions = N.vstack((positions,rocketPosition))
        if timeElapsed > engineDuration : 
            propulsionAccel = (0.0,0.0,0.0)
        if (rocketVector[0] < 0.0) and (pDeployed == False):
            gravity = gravity / 10
            pDeployed = True
    return positions
    
def rocketStep(rocketVector, rocketPosition, propulsionAccel, wind, gravity ):
    newAccel = N.array([gravity[0] + propulsionAccel[0] + getWindAccel(wind[int(rocketPosition[0]) , int(rocketPosition[1]) , int(rocketPosition[2]) , 0]),  \
                gravity[1] + propulsionAccel[1] + getWindAccel(wind[int(rocketPosition[0]) , int(rocketPosition[1]) , int(rocketPosition[2]) , 1]),   \
                gravity[2] + propulsionAccel[2] + getWindAccel(wind[int(rocketPosition[0]) , int(rocketPosition[1]) , int(rocketPosition[2]) , 2])])
    newRocketVector = rocketVector + (newAccel * timeSlice)

    
    newPosition = rocketPosition + newRocketVector
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

