#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:21:51 2021

@author: timkozlov
"""

import numpy as np
import matplotlib.pyplot as plt

def visHeightVsDisplacement2D(positions):
    
    # Get number of position vectors
    num_positions = np.shape(positions)[0]
    
    # Create vector arrays
    displacements = np.zeros((num_positions,))
    heights = np.zeros((num_positions,))
  
    # Calculate displacement
    for i in np.arange(num_positions):
        # Get position vector
        pos = positions[i]
        
        # Store displacement
        displacements[i] = np.sqrt(pos[1] * pos[1] + pos[2] * pos[2])
        
        # Store height
        heights[i] = pos[0]
        
    
    # Plot the height over displacement
    plt.plot(displacements, heights)
    plt.xlabel('Horizontal Displacement (meters)')
    plt.ylabel('Height (meters)')
    plt.title('Rocket Displacement vs Height')

def visDisplacementChance2D(simulations, worldSize, graphUnits):
    # Create a grid
    grid = np.zeros((graphUnits, graphUnits))
    
    # For each simulation
    for sim in range(len(simulations)):
        # Get ending positions
        pos = simulations[sim][-1]
        north = round(pos[1] / worldSize * graphUnits)
        east = round(pos[2] / worldSize * graphUnits)
        
        print(north, east)
        
        # If it fits on board
        if north >= 0 and north < graphUnits:
            if east >= 0 and east < graphUnits:
                grid[north][east] += 1

                
    print(grid)

    # Plot the heatmap
    plt.imshow(grid, cmap='inferno')
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('North/South')
    plt.ylabel('East/West')
    plt.title('Landing Probability (top down view)')

def visRocketPath3D(simulations, worldSize):
    # Create a figure
    fig = plt.figure()
 
    # syntax for 3-D projection
    ax = plt.axes(projection ='3d')
    
    plt.xlim([-worldSize, worldSize])
    plt.ylim([-worldSize, worldSize])
    
    # For each simulation
    for sim in range(len(simulations)):
        # Plot rocket path
        positions = simulations[sim]
        ax.plot3D(positions[:,1], positions[:,2], positions[:,0])
    
    ax.set_title('Rocket paths in 3D space')
    plt.xlabel('North/South')
    plt.ylabel('East/West')
    plt.show()
    plt.ion()

if __name__ == "__main__":
    
    def genPositions(dx, dz):
        # Generate fake positions
        positions = []
        north = 500
        east = 500
        height = 0
        vnorth = 0
        veast = 0
        vheight = 20
        positions.append([height,north,east])
        while height >= 0:
            north += vnorth
            east += veast
            height += vheight
            vnorth += np.random.uniform(-dx, dx)
            veast += np.random.uniform(-dz, dz)
            vheight -= 5
            if height >= 0:
                positions.append([height,north,east])
            
        return np.array(positions)
    
    
    #visHeightVsDisplacement2D(genPositions(5, 5))
    
    #visDisplacementChance2D([genPositions(5, 7) for i in range(500)], 1000, 100)
    
    #visRocketPath3D([genPositions(0, 7) for i in range(50)], 200)
