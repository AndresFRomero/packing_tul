# -*- coding: utf-8 -*-
"""
Pallet Generation Service
TUL - Universidad de Los Andes
Diego Suarez - Andrés Romero
"""

# Imports
import pandas as pd
import numpy as np

class PalletGenerationService:
    # FUNCTIONS
    def fun1(self, p1: float, p2: float):
        if (p1 + p2) > 5:
            return False
        else:
            return True

    def fun2(self, p1: float, p2: float):
        if p1 > p2:
            return True
        else:
            return False
    
    # MAIN
    def main(self, data):
        p1,p2 = len(data), len(data)/2
        return  {
            "A": {
                    "length": 120,
                    "width": 120,
                    "height": 120,
                    "weight": 2000,
                    "quantity": 5,
                    "fragile": True,
                    "palletized": True
            }
        }