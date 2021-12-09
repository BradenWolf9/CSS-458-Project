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

""" PLOTTING FUNCTIONS """

def plotLandingProbabilities(ax, simulations, worldSize, graphUnits):
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
    ax.set_ylabel('South   -    North')
    ax.set_xlabel('West    -   East')
    ax.set_title('Landing Probability (top down view)')

def plotRocketPath3D(ax, simulations, worldSize):

    plt.xlim([0, worldSize])
    plt.ylim([0, worldSize])
    
    # For each simulation
    for sim in range(len(simulations)):
        # Plot rocket path
        positions = simulations[sim]
        ax.plot3D(worldSize - positions[:,1], positions[:,2], positions[:,0])
    
    ax.set_title('Rocket paths in 3D space')
    ax.set_xlabel('North    -    South')
    ax.set_ylabel('West   -   East')

def plotHeightOverTime(ax, simulations, timeSlice):
    # For each simulation
    for positions in simulations:
        # Get the number of position vectors
        num_positions = np.shape(positions)[0]
        heights = np.zeros((num_positions,))
        times = np.arange(0, num_positions) * timeSlice
        
        # Store heights
        for i in np.arange(num_positions):
            # Get position vector
            pos = positions[i]
            heights[i] = pos[0]
            
        # Plot the height over time
        ax.plot(times, heights)
        
    # Label
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Height (meters)')
    ax.set_title('Rocket Height over time')
    
def plotDisplacementOverTime(ax, simulations, worldSize, timeSlice):
    # For each simulation
    for positions in simulations:
        # Get the number of position vectors
        num_positions = np.shape(positions)[0]
        displacements = np.zeros((num_positions,))
        times = np.arange(0, num_positions) * timeSlice
        
        # Store heights
        for i in np.arange(num_positions):
            # Get position vector
            pos = positions[i]
            
            # Calculate distance
            distNS = pos[1] - worldSize / 2
            distEW = pos[2] - worldSize / 2
            
            displacements[i] = np.sqrt(distNS ** 2 + distEW ** 2)
            
        # Plot the height over time
        ax.plot(times, displacements)
        
    # Label
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Displacement (meters)')
    ax.set_title('Rocket Displacement over time')

""" VISUALIZATION FUNCTIONS """

def visualizeFlightPath(simulations, worldSize, timeSlice):
    # Create a 2x2 grid
    gs = gridspec.GridSpec(1, 2)
    
    # Figure
    fig = plt.figure()
    
    # Plot heatmap
    ax1 = fig.add_subplot(gs[0, 0])
    plotLandingProbabilities(ax1, simulations, worldSize, 50)
    
    # Plot flight path in 3D
    ax2 = fig.add_subplot(gs[0, 1], projection='3d')
    plotRocketPath3D(ax2, simulations, worldSize)

def visualizeTimeData(simulations, worldSize, timeSlice):
    # Create a 2x2 grid
    gs = gridspec.GridSpec(1, 2)
    
    # Figure
    fig = plt.figure()
    
    # Plot height vs time
    ax1 = fig.add_subplot(gs[0, 0])
    plotHeightOverTime(ax1, simulations, timeSlice)
    
    # Plot height vs time
    ax2 = fig.add_subplot(gs[0, 1])
    plotDisplacementOverTime(ax2, simulations, worldSize, timeSlice)