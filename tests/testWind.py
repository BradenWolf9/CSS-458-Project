# test createWindField to make sure the initial wind vector is in the wind
# field
def test_createWindField_windVector():
    initWindVector = (2,43,483)
    windFieldSize = 52
    wind = createWindField(initWindVector, windFieldSize)
    if any(np.not_equal(wind[0,0,0,:],np.array([2,43,483]))) == True:
        print("Failed to put the initial wind vector in the wind field.")
        
        
# test createWindField to make sure the wind field is the correct size
def test_createWindField_windFieldSize():
    initWindVector = (2,43,483)
    windFieldSize = 52
    wind = createWindField(initWindVector, windFieldSize)
    if len(wind) != 52:
        print("Failed to set the correct size of the wind field.")

     
# executes all the tests for wind
def execute():
    test_createWindField_windVector()
    test_createWindField_windFieldSize()
