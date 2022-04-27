from gurobipy import *
import pandas as pd
import numpy as np
import random
#load data
movie_data = pd.read_csv('./ratings_sample_final.csv')
U = movie_data['userId'].to_list()
Ir = movie_data['movieId'].to_list()
R = movie_data['retailerId'].to_list()

# constants
K = 100000
m = len(set(U))
k = 2
w = 2

# Declare and initialize models
m1 = Model('LUBP1')
m2 = Model('LUBP2')

x_data = dict(zip(Ir, U))
y_data = dict(zip(R, U))

u = [[0 for _ in range(len(Ir)+1)] for _ in range(len(U)+1)]

for i in Ir:
    for j in U:
        item = i-1
        user = j-1
        if (item, user) in x_data:
            u[item][user] = 1
        else:
            u[item][user] = random.randint(0,1)

u_matrix = np.array(u)

# Create decision variables for the LUBP1 model
x_1 = m1.addMVar((501, 501), vtype=GRB.BINARY, name="x_m1") #c3
m1.update
# Create constraints for LUBP1
c1 = m1.addConstrs((x_1[:, j].sum() == k for j in U), 'c1')

# Create decision variables for the LUBP2 model
x_2 = m2.addMVar((501, 501), vtype=GRB.BINARY, name="x_m2") #c9
y_2 = m2.addMVar((501, 501), vtype=GRB.BINARY, name="y_m2") #c10
m2.update

# create constraints for LUBP2python3 
c4 = m2.addConstrs((x_2[:, j].sum() == k for j in U), 'c4')
c6 = m2.addConstrs((x_2[:, j].sum() <= K*y_2[r,j] for r in R for j in U), 'c6')
c7 = m2.addConstrs((x_2[:, j].sum() <= (1 - K*(1 - y_2[r,j])) for r in R for j in U ), 'c7')
c8 = m2.addConstrs((y_2[:, j].sum() >= w for j in U), 'c8')

# The objective is to maximize retailer diversity LUPB1
init_obj_func_m1 = m1.setMObjective(((u_matrix[i,j]) * x_1[i,j] for i in Ir for j in U), None, None, GRB.MAXIMIZE) # l[r] = 0 initially.
init_obj_func_m2 = m2.setMObjective(((u_matrix[i,j]) * x_2[i,j] for i in Ir for j in U), None, None, GRB.MAXIMIZE)

# save model for inspection
m1.write('LUBP1.lp')
m2.write('LUBP2.lp')

# run optimization engine
m1.optimize()
m2.optimize()

obj_1 = m1.getObjective()
print(obj_1.getValue())

obj_2 = m2.getObjective()
print(obj_2.getValue())

# def subGradientOptimization() :
#     l = 0
#     pi = 0.1
    
#     return l