# -*- coding: utf-8 -*-
"""
Pallet Generation Service
TUL - Universidad de Los Andes
Diego Suarez - Andrés Romero
"""

# Imports
import json

class MinViableTruckService:
    # FUNCTIONS
    def fun1(self, data):
        for key,value in data["products"].items():
            #Ya se sabe las cajas tipo estándar cuál es su MVT
            if value["palletized"]==True:
                if value["type"]=="A":
                    value["MVT"]="Camion min que carga TipoA"
                elif value["type"]=="B":
                    value["MVT"]="Camion min que carga TipoB"
                elif value["type"]=="C":
                    value["MVT"]="Camion min que carga TipoC"
                else:
                    value["MVT"]="Camion min que carga TipoD"
            #Probar si cabe en cada uno de los camiones hasta encontrar su MVT
            else:
                encontre = False
                while encontre == False:
                    for keyT,valueT in data["fleet"].items():
                        #Revisar largo
                        #Importante que camiones vengan ordenados en el json de más pequeño a más grande
                        if (value["length"]<=valueT["lengthCapacity"] 
                            and value["width"]<=valueT["widthCapacity"]
                            and value["height"]<=valueT["heightCapacity"]):
                            encontre = True
                            value["MVT"] = keyT
                            break
        
                #Si no encontré entre todos los camiones posibles, ingresar infactible en MVT
                if encontre == False:
                    value["MVT"] = "unfeasible"
        
        return data
    
    # MAIN
    def main(self, data):
        #Cargar archivo de json
        data=open("data.json",) #Cambiar el nombre del archivo según se requiera
        data=json.load(data)
        return data