import rocket as R
import wind as W  
import tests as T
import numpy as N

##############################################################################
# user defined variables #
rocketMass = 5
#                 z y x
initWindVector = (0,0,0)
#                 z y x   z: height, y: north(+) south(-), x: east(+) west(-)
#initWindVector = (4,2,6)
windFieldSize = 500 # windFieldSize * (1x1x1)
initRocketAngle = (1,0,0)
windStdDev = 0.0
heightStdDevScale = 1 # i.e. if heightStdDevScale = 2, stddev at top level is twice stddev at bottom level
heightMagScale = 1 # i.e if heightMagScale = 2, magnitude of vectors at top level is twice the magnitude of vectors at bottom level
timeSlice = .05
initialPosition = N.array([0,windFieldSize/2,windFieldSize/2])
tests = True # valid entries are True (runs tests) or False
##############################################################################

if __name__ == '__main__':
  wind = W.createWind(initWindVector, windFieldSize, heightMagScale, windStdDev, heightStdDevScale)
  positions = R.launchRocket(initRocketAngle, wind, timeSlice, initialPosition)
  if tests:
    T.execute()
