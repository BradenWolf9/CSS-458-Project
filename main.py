import rocket as R
from wind import *  
##############################################################################
# user defined variables #
rocketMass = 5
#                 z y x
initWindVector = (4,2,6)
windFieldSize = 100 # 100x100x100
initRocketAngle = (1,0,0)
windStdDev = 1.0
heightStdDevScale = 2 # i.e. if heightStdDevScale = 2, stddev at top level is twice stddev at bottom level
heightMagScale = 2 # i.e if heightMagScale = 2, magnitude of vectors at top level is twice the magnitude of vectors at bottom level
##############################################################################

if __name__ == '__main__':
  wind = createWind(initWindVector, windFieldSize, heightMagScale, windStdDev, heightStdDevScale)
