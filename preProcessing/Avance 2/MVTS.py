# -*- coding: utf-8 -*-
"""
Minimum Viable Truck Service
TUL - Universidad de Los Andes
Diego Suarez - Andrés Romero
"""

#Cargar paquetes
import json

#Cargar archivo de json
data=open("1ref.json",) #Cambiar el nombre del archivo según se requiera
data=json.load(data)

#Inicialización si el pedido se pudo empacar y lista con infromación de camiones 
factible = False
factibleTruck = "None"
truckList = []

#Creación de lista con información de los camiones
for key,value in data["fleet"].items():
   sublist = []
   sublist.append(key)
   sublist.append(value["weightCapacity"])
   sublist.append(value["volumeCapacity"])
   sublist.append(value["widthCapacity"])
   sublist.append(value["heightCapacity"])
   sublist.append(value["lengthCapacity"])
   truckList.append(sublist)
   
truckList = sorted(truckList, key=lambda x: x[2])

#Cálculo del volumen total de los ítems del pedido
totalVolume = 0
totalWeight = 0

for key,value in data["products"].items():
    totalVolume += value["length"]*value["width"]*value["height"]*value["quantity"]
    totalWeight += value["weight"]*value["quantity"]
    
for i in range(len(truckList)):
    if truckList[i][1]>=totalWeight and truckList[i][2]>=totalVolume:
        contador = 0
        for key,value in data["products"].items():
            if value["length"]>truckList[i][5] or  value["width"]>truckList[i][3] or value["height"]>truckList[i][3]:
                contador += 1
        if contador == 0:
            factibleTruck = truckList[i][0]
            factible = True
            break
    
print("Factible?", factible, "Camión:", factibleTruck)

    