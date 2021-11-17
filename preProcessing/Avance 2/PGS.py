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


if len(data["pallets"])>0:
    #Las cajas que no tienen pallet no deben incluir la clave "pallet" en el json
    #Si es necesaria la información de l, w, d de los pallets, me avisas y la agrego
    
    #Crear la lista con la información de los pallets
    #pallet_list = [info_pallet_1, ..., info_pallet_n]
    #info_pallet_i = [Nombre, Volumen]
    pallet_list = []
    
    #Listas para clasificar un producto según su tipo
    non_fragile_product_list = []
    fragile_product_list = []
    
    #Listas para cada uno de los pallets que se van a crear
    fragile_pallet_list = []
    non_fragile_pallet_list = []
    
    for i in range(0,len(data["pallets"])):
        #Agregar nombre del pallet a la lista
        sub_list= []
        sub_list.append(list(data["pallets"].keys())[i])
        
        #Agregar el volumen del pallet a la lista
        pallet_specifications = list(data["pallets"].values())[i]
        pallet_volume = list(pallet_specifications.values())[0]*list(pallet_specifications.values())[1]*list(pallet_specifications.values())[2]
        sub_list.append(pallet_volume)
        
        #Agregar el pallet a la lista de pallets
        pallet_list.append(sub_list)
        
        #Agregar en lista de productos un espacio para clasificar los productos
        #que pertenezcan a este tipo de pallet.
        sub_list= []
        fragile_product_list.append(sub_list)
        sub_list2= []
        non_fragile_product_list.append(sub_list2)
        
    
    
    #fragile_product_list stucture:
    #fragile_product_list=[pallet_1_products, ..., pallet_n_products]
    #pallet_1_products=[product_1_info, ..., product_n_info]
    #product_1_info=[weight, quantity, total_volume, unitary_volume]
    
    #non_fragile_product_list stucture:
    #non_fragile_product_list = [pallet_1_products, ..., pallet_n_products]
    #pallet_1_products = [product_1_info, ..., product_n_info]
    #product_1_info = [weight, quantity, unitary_volume]
    
    #Diccionario en donde guardo la respuesta
    cajas = dict()
    contadorCajas=0
    
    #Dividir los productos que conforman el pedido en sus listas correspondientes
    #según sus características de fragilidad y del paquete en el que deben ir asignados
    for key,value in data["products"].items():
        ubicado = False
        for i in range(len(pallet_list)):
            sub_list= []
            if "pallet" in value.keys() and value["pallet"] == pallet_list[i][0] and value["fragile"]==True:
                sub_list.append(value["weight"])
                sub_list.append(value["quantity"])
                sub_list.append(value["length"]*value["width"]*value["height"]*value["quantity"])
                sub_list.append(value["length"]*value["width"]*value["height"])
                fragile_product_list[i].append(sub_list)
                ubicado = True
            elif "pallet" in value.keys() and value["pallet"] == pallet_list[i][0] and value["fragile"]==False:
                sub_list.append(value["weight"])
                sub_list.append(value["quantity"])
                print(value["length"]*value["width"]*value["height"])
                sub_list.append(value["length"]*value["width"]*value["height"])
                non_fragile_product_list[i].append(sub_list)
                ubicado = True
        if ubicado == False:
            cajas[contadorCajas]={"length":value["length"], "width":value["width"], "height":value["height"], "weight":value["weight"], "quantity":value["quantity"], "fragile":value["fragile"], "palletized":False}
            contadorCajas += 1
    
    #Cajas frágiles
    #Resolver como "voy llenando cajas"
    
    #Variables auxiliares
    nfragi= 0
    nfragTot = 0
    
    for i in range(len(fragile_product_list)):
        nfragTot = 0
        nfragi = 0
        for j in range(len(fragile_product_list[i])):
            nfragTot += math.ceil(fragile_product_list[i][j][2]/pallet_list[i][1])
            nAfragi=math.ceil(fragile_product_list[i][j][2]/pallet_list[i][1])
            for cajita in range(1,nAfragi+1):
                if cajita==nAfragi:
                    if fragile_product_list[i][j][2] % pallet_list[i][1] == 0:
                        cajas[contadorCajas]={"weight":math.floor(pallet_list[i][1]/fragile_product_list[i][j][2])*fragile_product_list[i][j][0],"palletized":True,"type":pallet_list[i][0],"fragile":True}
                        contadorCajas += 1
                    else:
                        cajas[contadorCajas]={"weight":math.ceil((fragile_product_list[i][j][2] % pallet_list[i][1])/fragile_product_list[i][j][3])*fragile_product_list[i][j][0],"palletized":True,"type":pallet_list[i][0],"fragile":True}
                        contadorCajas += 1
                else:
                    cajas[contadorCajas]={"weight":math.floor(pallet_list[i][1]/fragile_product_list[i][j][3])*fragile_product_list[i][j][0],"palletized":True,"type":pallet_list[i][0],"fragile":True}
                    contadorCajas += 1
    
    
    #non_fragile_pallet_list stucture:
    #non_fragile_pallet_list = [pallet_1_products, ..., pallet_n_products]
    #pallet_1_products = [product_1_info, ..., product_n_info]
    #product_1_info = [weight, quantity, unitary_volume]
    
    
    #Cajas no frágiles (Algoritmo First Fit)
    for k in range(len(non_fragile_product_list)):    
        #Creación de variables de la cantidad de cajas no frágiles de cada tipo que son 
        #necesarias en el pedido
        nTot = 0
        
        #Cantidad máxima de cajas y su inicialización en listas
        n = 0
        for c in range(len(non_fragile_product_list[k])):
            n += non_fragile_product_list[k][c][1]
            
        volDisp = [0]*n
        pesoCaja = [0]*n
        
        # Algoritmo First Fit
        for c in range(len(non_fragile_product_list[k])):
            for producto in range(1,non_fragile_product_list[k][c][1]+1):
                # Buscar si en alguna de las cajas que ya se abrió cabe el producto
                i = 0
                while( i < nTot):
                    if (volDisp[i] >= non_fragile_product_list[k][c][2]):
                        volDisp[i] -= non_fragile_product_list[k][c][2]
                        pesoCaja[i] += non_fragile_product_list[k][c][0]
                        break
                    i+=1
                     
                # Abrir una nueva caja si el producto no cabe en ninguna de las que ya están abiertas
                if (i == nTot):
                    volDisp[nTot] = pallet_list[k][1] - non_fragile_product_list[k][c][2]
                    pesoCaja[nTot] += non_fragile_product_list[k][c][0]
                    nTot += 1       
        
        #Almacenar respuesta en diccionario
        for j in range(0,len(volDisp)):
            if pesoCaja[j]>0:
                cajas[contadorCajas]={"weight":pesoCaja[j],"palletized":True,"type":pallet_list[k][0],"fragile":False}
                contadorCajas += 1

else:
    for key,value in data["products"].items():
        cajas[contadorCajas]={"length":value["length"], "width":value["width"], "height":value["height"], "weight":value["weight"], "quantity":value["quantity"], "fragile":value["fragile"], "palletized":False}
        contadorCajas += 1

#Imprimir respuesta
dataPGS = dict()
dataPGS = {"products":cajas,"pallets":data["pallets"]}

#Crear archivo .json con los datos
with open('PGS_output.json', 'w', encoding='utf-8') as f:
    json.dump(dataPGS, f, ensure_ascii=False, indent=4)
