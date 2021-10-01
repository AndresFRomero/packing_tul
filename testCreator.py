# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:16:49 2021

@author: NECSOFT
"""

import pandas as pd
import json

routes = pd.read_excel('./tests/trueRoutes.xlsx', index_col='route_id')
routes_ids = set(routes.index)

trucks = pd.read_excel('./db/db.xlsx', sheet_name='vehicle_types', index_col = 'name').to_dict(orient='index')

count = 1
for i in routes_ids:
    if count<10:
        indRoute = routes[routes.index.isin([i])].set_index('product_id')
        truckName = list(indRoute['truck'])[0]
        dTruck =  trucks[truckName]
        dTruck['name'] = truckName
        indRoute = indRoute.drop(columns = ['truck'])
        products = indRoute.to_dict(orient = 'index')
        
        with open('test' + str(i) +'.json', 'w') as fp:
            json.dump( {'truck': dTruck, 'products':products }, fp)
        
        count += 1
    else:
        break
