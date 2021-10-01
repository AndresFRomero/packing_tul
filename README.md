# packing_tul

Algoritmo de packing para TUL. Se tienen 3 servicios distintos:

1. Pre Processing (Diego)
    -  1. Pallet Generation Service
    Se encarga de agrupar en pallets estándar los productos que están dentro de un paquete.
    -  2. Min Viable Truck Service
    Se encarga de evaluar cada uno de los paquetes y decidir cuál es el vehículo mas pequeño en el que se podría empacar. Asumiendo que dicho vehículo solo va a llevar ese paquete.
    -  3. Lower Bound Packing Service
    Se encarga de evaluar un conjunto de paquetes (ruta) y decidir, mediante reglas fijas, si caben en un camión dado por parámetro o no. Adicional, este servicio decide si la ruta vale la pena verificarla con alguno de los algoritmos de packing.

2. Light Packing Service (Daniel)
Algoritmo de packing que evalúa si un conjunto de productos/pallets caben en un camión dado por parámetro. No hay restricciones de fragilidad, ni de multidrop o rotaciones. Tampoco es necesario retornar la ubicación de los paquetes en el vehículo, solo es necesario decir si es posible o no.

3. Robust Packing Service (Natalia)
Algoritmo de packing que evalúa si un conjunto de productos/pallets caben en un camión dado por parámetro. Tenemos restricciones de fragilidad y apilamiento.