#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:21:51 2021

@author: timkozlov
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

def visHeightVsDisplacement2D(simulations, startPos):

    # Create vector arrays
    for positions in simulations:
        # Get number of position vectors
        num_positions = np.shape(positions)[0]
        displacements = np.zeros((num_positions,))
        heights = np.zeros((num_positions,))
      
        # Calculate displacement
        for i in np.arange(num_positions):
            # Get position vector
            pos = positions[i]
            
            dnorth = pos[1] - startPos[1]
            deast = pos[2] - startPos[2]
            
            # Store displacement
            displacements[i] = np.sqrt(dnorth * dnorth + deast * deast)
            
            # Store height
            heights[i] = pos[0] - startPos[0]
    
        # Plot the height over displacement
        plt.plot(displacements, heights)
        
    # Label        
    plt.xlabel('Horizontal Displacement (meters)')
    plt.ylabel('Height (meters)')
    plt.title('Rocket Displacement vs Height')
    plt.show()

def visDisplacementChance2D(simulations, worldSize, graphUnits):
    # Create a grid
    grid = np.zeros((graphUnits, graphUnits))
    
    # For each simulation
    for sim in range(len(simulations)):
        # Get ending positions
        pos = simulations[sim][-1]
        north = round((1 - pos[1] / worldSize) * graphUnits)
        east = round(pos[2] / worldSize * graphUnits)
        
        # If it fits on board
        if north >= 0 and north < graphUnits:
            if east >= 0 and east < graphUnits:
                grid[north][east] += 1

    # Plot the heatmap
    plt.imshow(grid, cmap='inferno')
    plt.xticks([])
    plt.yticks([])
    plt.ylabel('South   -    North')
    plt.xlabel('West    -   East')
    plt.title('Landing Probability (top down view)')

def visRocketPath3D(simulations, worldSize):
        # Create a figure
        fig = plt.figure()
     
        # syntax for 3-D projection
        ax = plt.axes(projection ='3d')
        
        plt.xlim([0, worldSize])
        plt.ylim([0, worldSize])
        
        # For each simulation
        for sim in range(len(simulations)):
            # Plot rocket path
            positions = simulations[sim]
            ax.plot3D(worldSize - positions[:,1], positions[:,2], positions[:,0])
        
        ax.set_title('Rocket paths in 3D space')
        plt.xlabel('North    -    South')
        plt.ylabel('West   -   East')
        plt.show()
        plt.ion()
    
def plotHeightVsDisplacement2D(simulations, startPos, ax):
    # Create vector arrays
    for positions in simulations:
        # Get number of position vectors
        num_positions = np.shape(positions)[0]
        displacements = np.zeros((num_positions,))
        heights = np.zeros((num_positions,))
      
        # Calculate displacement
        for i in np.arange(num_positions):
            # Get position vector
            pos = positions[i]
            
            dnorth = pos[1] - startPos[1]
            deast = pos[2] - startPos[2]
            
            # Store displacement
            displacements[i] = np.sqrt(dnorth * dnorth + deast * deast)
            
            # Store height
            heights[i] = pos[0] - startPos[0]
    
        # Plot the height over displacement
        ax.plot(displacements, heights)
        
    # Label        
    #ax.xlabel('Horizontal Displacement (meters)')
    #ax.ylabel('Height (meters)')
    #ax.title('Rocket Displacement vs Height')

def plotDisplacementChance2D(simulations, worldSize, graphUnits, ax):
    # Create a grid
    grid = np.zeros((graphUnits, graphUnits))
    
    # For each simulation
    for sim in range(len(simulations)):
        # Get ending positions
        pos = simulations[sim][-1]
        north = round((1 - pos[1] / worldSize) * graphUnits)
        east = round(pos[2] / worldSize * graphUnits)
        
        # If it fits on board
        if north >= 0 and north < graphUnits:
            if east >= 0 and east < graphUnits:
                grid[north][east] += 1

    # Plot the heatmap
    ax.imshow(grid, cmap='inferno')
    ax.xaxis.set_major_locator(ticker.NullLocator())
    ax.yaxis.set_major_locator(ticker.NullLocator())
    #plt.ylabel('South   -    North')
    #plt.xlabel('West    -   East')
    ax.set_title('Landing Probability (top down view)')

def plotRocketPath3D(simulations, worldSize, ax):
    
    plt.xlim([0, worldSize])
    plt.ylim([0, worldSize])
    
    # For each simulation
    for sim in range(len(simulations)):
        # Plot rocket path
        positions = simulations[sim]
        ax.plot3D(worldSize - positions[:,1], positions[:,2], positions[:,0])
    
    ax.set_title('Rocket paths in 3D space')
    #plt.xlabel('North    -    South')
    #plt.ylabel('West   -   East')
    #plt.show()
    #plt.ion()

def visAllPlots(simulations, worldSize, graphUnits, startPos):
    # Create 2x2 sub plots
    gs = gridspec.GridSpec(1, 2)
    
    fig = plt.figure()
    
    ax2 = fig.add_subplot(gs[0, 0]) # row 0, col 1
    plotDisplacementChance2D(simulations, worldSize, graphUnits, ax2)
    
    ax3 = fig.add_subplot(gs[0, 1], projection='3d') # row 1, span all columns
    plotRocketPath3D(simulations, worldSize, ax3)