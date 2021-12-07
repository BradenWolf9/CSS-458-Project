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
        displacements[i] = np.sqrt(pos[0] * pos[0] + pos[2] * pos[2])
        
        # Store height
        heights[i] = pos[1]
        
    
    # Plot the height over displacement
    plt.plot(displacements, heights)
    plt.xlabel('Horizontal Displacement (meters)')
    plt.ylabel('Height (meters)')
    plt.title('Rocket Displacement vs Height')

def visDisplacementChance2D(simulations, worldSize, unitSize):
    # Create a grid
    unitsInWorld = round(worldSize / unitSize)
    grid = np.zeros((unitsInWorld, unitsInWorld))
    
    # For each simulation
    for sim in range(len(simulations)):
        # Get ending positions
        pos = simulations[sim][-1]
        x = round(pos[0] / worldSize * unitSize + unitsInWorld / 2)
        z = round(pos[2] / worldSize * unitSize + unitsInWorld / 2)
        
        # If it fits on board
        if x >= 0 and x < unitsInWorld:
            if z >= 0 and z < unitsInWorld:
                grid[x][z] += 1

                
        # Plot the heatmap
        plt.imshow(grid, cmap='inferno')
        plt.xticks([])
        plt.yticks([])
        plt.xlabel('X Offset')
        plt.ylabel('Z Offset')
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
        ax.plot3D(positions[:,0], positions[:,2], positions[:,1])
    
    ax.set_title('Rocket paths in 3D space')
    plt.show()
    plt.ion()

if __name__ == "__main__":
    
    def genPositions(dx, dz):
        # Generate fake positions
        positions = []
        x = 0
        y = 0
        z = 0
        vx = 0
        vy = 20
        vz = 0
        positions.append([x,y,z])
        while y >= 0:
            x += vx
            y += vy
            z += vz
            vx += np.random.uniform(-dx, dx)
            vz += np.random.uniform(-dz, dz)
            vy -= 5
            if y >= 0:
                positions.append([x,y,z])
            
        return np.array(positions)
    
    
    #visHeightVsDisplacement2D(genPositions(5, 5))
    
    #visDisplacementChance2D([genPositions(5, 7) for i in range(500)], 1000, 50)
    
    visRocketPath3D([genPositions(5, 7) for i in range(50)], 200)
