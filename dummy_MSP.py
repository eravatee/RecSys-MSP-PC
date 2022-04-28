
# import gurobi library
from dataclasses import dataclass
from itertools import combinations
from gurobipy import *
import pandas as pd

movie_data = pd.read_csv('./ratings_sample_final.csv')
U = movie_data['userId'].to_list()
Ir = movie_data['movieId'].to_list()
R = movie_data['retailerId'].to_list()
# print("R", R)
# print("U: ", U)
# constants
K = 100000
m = len(set(U))
k = 5
w = 2

# Declare and initialize model
m1 = Model('LUBP1')
m2 = Model('LUBP2')

x_data = list(zip(Ir, U))
y_data = list(zip(R, U))

# print(x_data)
x_matrix = [[0 for _ in range(len(Ir)+1)] for _ in range(len(U)+1)]
y_matrix = [[0 for _ in range(len(R)+1)] for _ in range(len(U)+1)]

# for i in range(len(Ir)):
#     for j in range(len(U)): 
#         print("(Ir[i], U[j])", (Ir[i], U[j]))
#         if (Ir[i], U[j]) in x_data:
#             x_matrix[i][j] = 1
#     break

for i in Ir:
    for j in U:
        if (i, j) in x_data:
            x_matrix[i-1][j-1] = 1

for i in Ir:
    for j in U:
        if (i, j) in x_data:
            y_matrix[i-1][j-1] = 1

# print("x_data: ", x_data)
# print("y_data: ", y_data)

# Create decision variables for the LUBP1 model
x_1 = m1.addVars(x_matrix, vtype=GRB.BINARY, name="x_m1") #c3
m1.update

# create constraints for LUBP1
# c1 = m1.addConstrs((x.prod(i, '*') == k for j in U), 'c1')
# c1 = m1.addConstrs((prod(x) == k for j in U), 'c1')
# c1 = m1.addConstrs(((quicksum(x[i,j] for i in Ir) for r in R) == k) for j in U), 'c1'))

# c1 = m1.addConstrs(((quicksum(x[i,j]) for i in Ir) == k for j in U), 'c1')
c1 = m1.addConstrs((x_1.sum('*',j) == k for j in U), 'c1')
# c3 = m1.addConstrs(0< x < 1)


# Create decision variables for the LUBP2 model
x_2 = m2.addVars(x_matrix, vtype=GRB.BINARY, name="x_m2") #should it be here again?
y_2 = m2.addVars(y_matrix, vtype=GRB.BINARY, name="y_m2")

m2.update

# create constraints for LUBP2
# c4 = m2.addConstrs((x_2.sum('*',j) == k for j in U), 'c4')
# print("x_2: ", x_2)
# print("y_2: ", y_2)
# for r in R:
#     print("r: ",r)
#     for j in U:
#         print("j: ", j)
#         c6 = m2. addConstrs((x_2.sum('*', j) <= K*y_2[r,j]), 'c6')
# c6 = m2.addConstrs((x_1.sum('*', j) <= K*y_2[r, j] for r in R for j in U), 'c6')
# c6 = m2.addConstrs((quicksum(x[i,j]) for i in Ir <= [K*y[r,j] for j in U for r in R ]), 'c6')
# c6 = m2.addConstrs(((quicksum(x[i,j]) for i in Ir) == K for j in U), 'c6')
# c7 = m2.addConstrs((x.sum('*', j) <= (1 - K*(1 - y[r,j])) for r in R for j in U ), 'c7')
# c7 = m2.addConstrs((quicksum(x[i,j]) for i in Ir <= 1 - (K* (1 - y[r,j])) for j in U for r in R), 'c7')
# c8 = m2.addConstrs((y.sum('*', j) >= w for j in U), 'c8')
# c8 = m2.addConstrs(((quicksum(y[r,j]) for r in R)  == w for j in U), 'c8')

# # The objective is to maximize retailer diversity LUPB1
# # obj_func = x.prod(l[r]+u[i,j])- sum(l[r]*a[r]*p[r]*m*k) for i in I for j in U for r in Ir 
# obj_func = [quicksum((l[r]+u[i,j])*x[i,j]) for i in Ir for r in R for j in U - sum(l[r]*a[r]*p[r]*m*k) for r in R]
# m1.setObjective(obj_func, GRB.MAXIMIZE)

# # save model for inspection
# m1.write('LUBP1.lp')
# m2.write('LUBP2.lp')

# # run optimization engine
# m1.optimize()
# m2.optimize()

# c1 = m1.addMConstr(x @ x_1 == k, 'c1')
# c4 = m2.addConstr(x_matrix @ x_2 == k, 'c4')
# c6 = m2.addConstr((x_matrix @ x_2 <= K @ y_matrix), 'c6')
# c7 = m2.addConstr(x_matrix @ x_2 <= 1 - K + K @ y_matrix, 'c7')
# c8 = m2.addConstr(y_matrix @ y_2 >= w , 'c8')