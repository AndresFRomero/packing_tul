# -*- coding: utf-8 -*-
"""
Lower Bound Packing Service Validator
TUL - Universidad de Los Andes
Diego Suarez - Andrés Romero
"""

# Imports
import os
import json
import time
import matplotlib.pyplot as plt
import matplotlib.image as image

# Service
import lowerBoundPackingService as lbps

def plotSolution(sol):
    print('solution: ', sol)

LBPS = lbps.LowerBoundPackingService()

basicTests = './tests/lbps/basic'
performanceTests = './tests/lbps/performance' 
operationTests = './tests/lbps/operation' 
individualTest = './tests/lbps/individual'

print("\n", "INDIVIDUAL TEST")
for subdir, dirs, files in os.walk(individualTest):
    for file in files:
        strFile = os.path.join(subdir, file)
        # Se abren todos los archivos del directorio
        with open(strFile, 'r') as fp:
            data = json.load(fp)
        
        start_time = time.time()
        sol = LBPS.main(data)
        end_time = time.time()

        print(str(file), ' time: ', round(end_time-start_time,2))
        plotSolution(sol)