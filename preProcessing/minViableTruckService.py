# -*- coding: utf-8 -*-
"""
Pallet Generation Service
TUL - Universidad de Los Andes
Diego Suarez - Andrés Romero
"""

# Imports
import pandas as pd
import numpy as np

class MinViableTruckService:
    # FUNCTIONS
    def fun1(self, p1: float, p2: float):
        if (p1 + p2) > 5:
            return True
        else:
            return False

    def fun2(self, p1: float, p2: float):
        if p1 > p2:
            return True
        else:
            return False
    
    # MAIN
    def main(self, data):
        p1,p2 = len(data), len(data)/2
        if (self.fun1(p1,p2) and self.fun2(p1,p2)):
            return "Carry"
        else:
            return "Sencillo"