import pandas as pd
import numpy as np
import random 
from collections import Counter 

df = pd.read_csv('./ratings.csv')
data = df.sample(frac = 0.002)
data = data.drop('timestamp', 1)
retailer_id = random.choices(range(1,21,1), k=202)
data['retailerId'] = retailer_id
data.to_csv('movieDataset.csv', index=False)





