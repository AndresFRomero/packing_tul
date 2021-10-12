# -*- coding: utf-8 -*-
"""
Pallet Generation Service
TUL - Universidad de Los Andes
Diego Suarez - Andrés Romero
"""
#Cargar paquetes
import json
import math

#Cargar archivo de json
data=open("1red.json",)
data=json.load(data)

# =============================================================================
# Pallet Generation Service
# =============================================================================

#Diccionarios con los productos frágiles y no frágiles de cada categoría
A=dict()
Afrag=dict()
B=dict()
Bfrag=dict()
C=dict()
Cfrag=dict()
D=dict()
Dfrag=dict()

#Dividir los productos que conforman el pedido en sus diccionarios correspondientes
#según sus características de fragilidad y del paquete en el que deben ir asignados
for key,value in data["products"].items():
    if value["pallet"] =="A":
        if value["fragile"]==True:
            value["volT"]=value["length"]*value["width"]*value["height"]*value["quantity"]
            value["volU"]=value["length"]*value["width"]*value["height"]
            del value["pallet"]
            del value["fragile"]
            del value["length"]
            del value["width"]
            del value["height"]
            Afrag[key]=value
        else:
            value["volU"]=value["length"]*value["width"]*value["height"]
            del value["pallet"]
            del value["fragile"]
            del value["length"]
            del value["width"]
            del value["height"]
            A[key]=value
    elif value["pallet"]=="B":
        if value["fragile"]==True:
            value["volT"]=value["length"]*value["width"]*value["height"]*value["quantity"]
            value["volU"]=value["length"]*value["width"]*value["height"]
            del value["pallet"]
            del value["fragile"]
            del value["length"]
            del value["width"]
            del value["height"]
            Bfrag[key]=value
        else:
            value["vol"]=value["length"]*value["width"]*value["height"]
            del value["pallet"]
            del value["fragile"]
            del value["length"]
            del value["width"]
            del value["height"]
            B[key]=value
    elif value["pallet"]=="C":
        if value["fragile"]==True:
            value["volT"]=value["length"]*value["width"]*value["height"]*value["quantity"]
            value["volU"]=value["length"]*value["width"]*value["height"]
            del value["pallet"]
            del value["fragile"]
            del value["length"]
            del value["width"]
            del value["height"]
            Cfrag[key]=value
        else:
            value["vol"]=value["length"]*value["width"]*value["height"]
            del value["pallet"]
            del value["fragile"]
            del value["length"]
            del value["width"]
            del value["height"]
            C[key]=value
    else:
        if value["fragile"]==True:
            value["volT"]=value["length"]*value["width"]*value["height"]*value["quantity"]
            value["volU"]=value["length"]*value["width"]*value["height"]
            del value["pallet"]
            del value["fragile"]
            del value["length"]
            del value["width"]
            del value["height"]
            Dfrag[key]=value
        else:
            value["vol"]=value["length"]*value["width"]*value["height"]
            del value["pallet"]
            del value["fragile"]
            del value["length"]
            del value["width"]
            del value["height"]
            D[key]=value
        
#Crear diccionario con el volumen disponible en cada uno de los tipos de caja
volP=dict()
for key,value in data["pallets"].items():
    volP[key]=value["length"]*value["width"]*value["height"]
    
#Resolver como "voy llenando cajas" [Caja abierta(?)]
#Cajas frágiles

#Creación de variables de la cantidad de cajas frágiles de cada tipo que son 
#necesarias en el pedido
nAfragTot = 0
nBfragTot = 0
nCfragTot = 0
nDfragTot = 0

#Variables auxiliares
nAfragi= 0
nBfragi= 0
nCfragi= 0
nDfragi= 0

#Diccionario en donde guardo la información de cada una de las cajas por categoría
cajas = dict()


#Cálculo de cantidad de cajas frágiles tipo A requeridas y el peso asignado a cada
#una de ellas
contadorCajas=0
for k,v in Afrag.items():
    nAfragTot += math.ceil(v["volT"]/volP["A"])
    nAfragi=math.ceil(v["volT"]/volP["A"])
    for cajita in range(1,nAfragi+1):
        if cajita==nAfragi:
            if v["volT"] % volP["A"] == 0:
                cajas[contadorCajas]={"weight":math.floor(volP["A"]/v["volU"])*v["weight"],"palletized":True,"type":"A","fragile":True}
                contadorCajas += 1
            else:
                cajas[contadorCajas]={"weight":math.ceil((v["volT"] % volP["A"])/v["volU"])*v["weight"],"palletized":True,"type":"A","fragile":True}
                contadorCajas += 1
        else:
            cajas[contadorCajas]={"weight":math.floor(volP["A"]/v["volU"])*v["weight"],"palletized":True,"type":"A","fragile":True}
            contadorCajas += 1

#Cálculo de cantidad de cajas frágiles tipo B requeridas y el peso asignado a cada
#una de ellas
for k,v in Bfrag.items():
    nBfragTot += math.ceil(v["volT"]/volP["B"])
    nBfragi=math.ceil(v["volT"]/volP["B"])
    for cajita in range(1,nBfragi+1):
        if cajita==nBfragi:
            if v["volT"] % volP["B"] == 0:
                cajas[contadorCajas]={"weight":(volP["B"]/v["volU"])*v["weight"],"palletized":True,"type":"B","fragile":True}
                contadorCajas += 1
            else:
                cajas[contadorCajas]={"weight":math.ceil((v["volT"] % volP["B"])/v["volU"])*v["weight"],"palletized":True,"type":"B","fragile":True}
                contadorCajas += 1
        else:
            cajas[contadorCajas]={"weight":math.floor(volP["B"]/v["volU"])*v["weight"],"palletized":True,"type":"B","fragile":True}
            contadorCajas += 1
            
#Cálculo de cantidad de cajas frágiles tipo C requeridas y el peso asignado a cada
#una de ellas
for k,v in Cfrag.items():
    nCfragTot += math.ceil(v["volT"]/volP["C"])
    nCfragi=math.ceil(v["volT"]/volP["C"])
    for cajita in range(1,nCfragi+1):
        if cajita==nCfragi:
            if v["volT"] % volP["C"] == 0:
                cajas[contadorCajas]={"weight":(volP["C"]/v["volU"])*v["weight"],"palletized":True,"type":"C","fragile":True}
                contadorCajas += 1
            else:
                cajas[contadorCajas]={"weight":math.ceil((v["volT"] % volP["C"])/v["volU"])*v["weight"],"palletized":True,"type":"C","fragile":True}
                contadorCajas += 1
        else:
            cajas[contadorCajas]={"weight":math.floor(volP["C"]/v["volU"])*v["weight"],"palletized":True,"type":"C","fragile":True}
            contadorCajas += 1

#Cálculo de cantidad de cajas frágiles tipo D requeridas y el peso asignado a cada
#una de ellas
for k,v in Dfrag.items():
    nDfragTot += math.ceil(v["volT"]/volP["D"])
    nDfragi=math.ceil(v["volT"]/volP["D"])
    for cajita in range(1,nDfragi+1):
        if cajita==nDfragi:
            if v["volT"] % volP["D"] == 0:
                cajas[contadorCajas]={"weight":(volP["D"]/v["volU"])*v["weight"],"palletized":True,"type":"D","fragile":True}
                contadorCajas += 1
            else:
                cajas[contadorCajas]={"weight":math.ceil((v["volT"] % volP["D"])/v["volU"])*v["weight"],"palletized":True,"type":"D","fragile":True}
                contadorCajas += 1
        else:
            cajas[contadorCajas]={"weight":math.floor(volP["D"]/v["volU"])*v["weight"],"palletized":True,"type":"D","fragile":True}
            contadorCajas += 1

#Cajas no frágiles (Algoritmo First Fit)

#Creación de variables de la cantidad de cajas no frágiles de cada tipo que son 
#necesarias en el pedido
nATot = 0
nBTot = 0
nCTot = 0
nDTot = 0

#Diccionario en donde guardo la información de cada una de las cajas por categoría
cajasA = dict()
cajasB = dict()
cajasC = dict()
cajasD = dict()

#Cajas tipo A
#Cantidad máxima de cajas y su inicialización en listas
n = 0
for key,value in A.items():
    n += value["quantity"] 
    
volDispA = [0]*n #Se podría reducir la cantidad de cajas que se habilitan
pesoCajaA = [0]*n

# Algoritmo First Fit
for key,value in A.items():
    for producto in range(1,value["quantity"]+1):
        # Buscar si en alguna de las cajas que ya se abrió cabe el producto
        i = 0
        while( i < nATot):
            if (volDispA[i] >= value["volU"]):
                volDispA[i] -= value["volU"]
                pesoCajaA[i] += value["weight"]
                break
            i+=1
             
        # Abrir una nueva caja si el producto no cabe en ninguna de las que ya están abiertas
        if (i == nATot):
            volDispA[nATot] = volP["A"] - value["volU"]
            pesoCajaA[nATot] += value["weight"]
            nATot += 1       

#Almacenar respuesta en diccionario
for j in range(0,len(volDispA)):
    if pesoCajaA[j]>0:
        cajas[contadorCajas]={"weight":pesoCajaA[j],"palletized":True,"type":"A","fragile":False}
        contadorCajas += 1

#Cajas tipo B
#Cantidad máxima de cajas y su inicialización en listas
n = 0
for key,value in B.items():
    n += value["quantity"] 
    
volDispB = [0]*n #Se podría reducir la cantidad de cajas que se habilitan
pesoCajaB = [0]*n

# Algoritmo First Fit
for key,value in B.items():
    for producto in range(1,value["quantity"]+1):
        # Buscar si en alguna de las cajas que ya se abrió cabe el producto
        i = 0
        while( i < nBTot):
            if (volDispB[i] >= value["volU"]):
                volDispB[i] -= value["volU"]
                pesoCajaB[i] += value["weight"]
                break
            i+=1
             
        # Abrir una nueva caja si el producto no cabe en ninguna de las que ya están abiertas
        if (i == nBTot):
            volDispB[nBTot] = volP["B"] - value["volU"]
            pesoCajaB[nBTot] += value["weight"]
            nBTot += 1    

#Almacenar respuesta en diccionario
for j in range(0,len(volDispB)):
    if pesoCajaB[j]>0:
        cajas[contadorCajas]={"weight":pesoCajaB[j],"palletized":True,"type":"B","fragile":False}
        contadorCajas += 1
        
#Cajas tipo C
#Cantidad máxima de cajas y su inicialización en listas
n = 0
for key,value in C.items():
    n += value["quantity"] 
    
volDispC = [0]*n #Se podría reducir la cantidad de cajas que se habilitan
pesoCajaC = [0]*n

# Algoritmo First Fit
for key,value in C.items():
    for producto in range(1,value["quantity"]+1):
        # Buscar si en alguna de las cajas que ya se abrió cabe el producto
        i = 0
        while( i < nCTot):
            if (volDispC[i] >= value["volU"]):
                volDispC[i] -= value["volU"]
                pesoCajaC[i] += value["weight"]
                break
            i+=1
             
        # Abrir una nueva caja si el producto no cabe en ninguna de las que ya están abiertas
        if (i == nCTot):
            volDispC[nCTot] = volP["C"] - value["volU"]
            pesoCajaC[nCTot] += value["weight"]
            nCTot += 1  

#Almacenar respuesta en diccionario
for j in range(0,len(volDispC)):
    if pesoCajaC[j]>0:
        cajas[contadorCajas]={"weight":pesoCajaC[j],"palletized":True,"type":"C","fragile":False}
        contadorCajas += 1

#Cajas tipo D
#Cantidad máxima de cajas y su inicialización en listas
n = 0
for key,value in D.items():
    n += value["quantity"] 
    
volDispD = [0]*n #Se podría reducir la cantidad de cajas que se habilitan
pesoCajaD = [0]*n

# Algoritmo First Fit
for key,value in D.items():
    for producto in range(1,value["quantity"]+1):
        # Buscar si en alguna de las cajas que ya se abrió cabe el producto
        i = 0
        while( i < nDTot):
            if (volDispD[i] >= value["volU"]):
                volDispD[i] -= value["volU"]
                pesoCajaD[i] += value["weight"]
                break
            i+=1
             
        # Abrir una nueva caja si el producto no cabe en ninguna de las que ya están abiertas
        if (i == nDTot):
            volDispD[nDTot] = volP["D"] - value["volU"]
            pesoCajaD[nDTot] += value["weight"]
            nDTot += 1 

#Almacenar respuesta en diccionario
for j in range(0,len(volDispD)):
    if pesoCajaD[j]>0:
        cajas[contadorCajas]={"weight":pesoCajaD[j],"palletized":True,"type":"D","fragile":False}
        contadorCajas += 1

dataPallets = json.dumps(cajas, indent=4)
dataPGS = dict()
fleet = dict()
fleet = {"Carry":{"weightCapacity": 800,"volumeCapacity": 4.5,"widthCapacity": 150,"heightCapacity": 150,
                  "lengthCapacity": 200},"Sencillo":{"weightCapacity": 10000,"volumeCapacity": 24,"widthCapacity": 300,
                    "heightCapacity": 200,"lengthCapacity": 600}}
dataPGS = {"products":cajas,"fleet":fleet}

#Crear archivo .json con los datos
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(dataPGS, f, ensure_ascii=False, indent=4)


# =============================================================================
# Min Viable Truck Service
# =============================================================================

#Cargar paquetes
import json

#Cargar archivo de json
data=open("data.json",) #Cambiar el nombre del archivo según se requiera
data=json.load(data)

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
                if (value["length"]<=valueT["lengthCapacity"] 
                    and value["width"]<=valueT["widthCapacity"]
                    and value["height"]<=valueT["heightCapacity"]):
                    encontre = True
                    value["MVT"] = keyT
                    break

        #Si no encontré entre todos los camiones posibles, ingresar infactible en MVT
        if encontre == False:
            value["MVT"] = "unfeasible"

#Crear archivo .json con los datos
with open('dataMVT.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# =============================================================================
# Lower bound packing service
# =============================================================================

#Que todas las cajas quepan por volumen

