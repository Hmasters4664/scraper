# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 20:38:20 2018

@author: Olivier
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

d_regdet = pd.read_csv('artCTP.csv')
d_regdet =d_regdet.drop(columns=['more_info','more_info-href','web-scraper-order', 'web-scraper-start-url', 'email','web'])

d_regdet.to_csv('artCTP.csv', index_label=None,index=False)
d_regdet.to_json(orient='records')




cred =credentials.Certificate('fir-listview-b8972-firebase-adminsdk-mq7nm-4035b338d5.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
x=d_regdet.iat[0,0]
data = {
    u'venue':  d_regdet.iat[0,1],
    u'info': d_regdet.iat[0,2],
    u'date': d_regdet.iat[0,3]
}

db.collection(u'Cape Town').document(u'Art').collection(d_regdet.iat[0,0]).document(d_regdet.iat[0,0]).set(data)

p=d_regdet.iat[7,3]
for i in range(0,15):
        title=d_regdet.iat[i,0]
        venue=d_regdet.iat[i,1]
        info=d_regdet.iat[i,2]
        date=d_regdet.iat[i,3]
        
        if (title == p):
            title =''
        if (venue == p):
            venue =''
        if (info == p):
            info =''
        if (date == p):
            date =''
            
        data = {
                u'title':  title,
                u'venue': venue,
                u'info': info,
                u'date': date
                }

        db.collection(u'Cape Town').document(u'Art').collection(title).document(title).set(data)