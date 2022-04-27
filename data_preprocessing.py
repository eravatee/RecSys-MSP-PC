import pandas as pd
import numpy as np
import random 
from collections import Counter , OrderedDict

data = pd.read_csv('./ratings_sample.csv')

# userId = df['userId'].to_list()
# counts = Counter(userId)
# sorted_counts = OrderedDict(sorted(counts.items()))
# print(sorted_counts)

max_users = 200,

# data = df[:500]
# data = data.drop('timestamp', 1)
# retailer_id = random.choices(range(1,21,1), k=500)
# data['retailerId'] = retailer_id
# data.to_csv('movieDataset.csv', index=False)
# movieId = data['movieId']

retailerId = [-1 for _ in range(501)]
movieId = random.choices(range(1,151,1), k=501)
df = pd.DataFrame(movieId, columns=['movieId'])
df.to_csv('movieId.csv', index=False)

# counts = Counter(movieId)
# print(counts)
# i = 0
# for movie in movieId:
#     i = i+1
#     if movie in range(0, 3):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 1
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(3, 9):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 2
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(9, 23):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 3
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(23, 27):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 4
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(27, 33):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 5
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(33, 37):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 6
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(37, 49):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 7
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(49, 56):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 8
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(56, 66):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 9
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(66, 68):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 10
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(68, 89):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 11
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(89, 94):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 12
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(94, 99):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 13
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(99, 109):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 14
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(109, 124):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 15
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(124, 131):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 16
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(131, 137):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 17
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(138, 142):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 18
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(142, 145):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 19
#         print("retailerId[movie]", retailerId[movie])
#     if movie in range(145, 150):
#         print("i", i)
#         print(movie)
#         retailerId[movie-1] = 20
#         print("retailerId[movie]", retailerId[movie])

# print("retailerId: ", retailerId)

# df = pd.read_excel('./mapping.xlsx')

# begin = df['begin'].to_list()
# end = df['end'].to_list()

# begin = [b-1 for b in begin]

# ranges = list(zip(begin, end))
# print(ranges)

# i = 0
# j = 1

# for movie in movieId:
#     for r in ranges:
#         x, y = r
#         print(x, y)
#         for movie in range(x, y):
# print(movie)            
# retailerId[movie] = j
#             i = i+1
#         j=j+1

# print(retailerId)
