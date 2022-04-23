
# import gurobi library
from gurobipy import *
import pandas as pd

movie_data = pd.read_csv('./movieDataset.csv')
U = movie_data['userId']
Ir = movie_data['movieId']
R = movie_data['retailerId']
print(type(R))


'''
# Declare and initialize model
m1 = gp.Model('LUBP1')
m2 = gp.Model('LUBP2')

# Create decision variables for the LUBP1 model
x = m1.addVars(vtype=GRB.BINARY, name="recommend1")
m1.update

# create constraints for LUBP1
# c1 = m1.addConstrs((x.prod(i, '*') == k for j in U), 'c1')
# c1 = m1.addConstrs((prod(x) == k for j in U), 'c1')
c1 = m1.addConstrs(((quicksum(x[i,j]) for i in Ir for r in R ) == k for j in U), 'c1')
# c3 = m1.addConstrs(0<= x[i,j] <=1)


# Create decision variables for the LUBP2 model
x = m2.addVars(vtype=GRB.BINARY, name="recommend2") #should it be here again?
y = m2.addVars(vtype=GRB.BINARY, name="recommend3")
m2.update

# create constraints for LUBP2
c4 = m2.addConstrs(((quicksum(x[i,j]) for i in Ir for r in R ) == k for j in U), 'c4')
# c6 = m2.addConstrs((x.sum('*', j) <= K*y[r,j] for j in U), 'c6')
c6 = m2.addConstrs((quicksum(x[i,j]) for i in Ir <= K*y[r,j] for j in U for r in R), 'c6')
# c7 = m2.addConstrs((x.sum('*', j) <= 1 - K(*1 - y[r,j]) for j in U), 'c7')
c7 = m2.addConstrs((quicksum(x[i,j]) for i in Ir <= 1 - K*(1 - y[r,j]) for j in U for r in R), 'c7')
# c8 = m2.addConstrs((y.sum('*', j) >= w for j in U), 'c8')
c8 = m2.addConstrs((quicksum(y[r,j]) for r in R  >= w for j in U), 'c8')

# The objective is to maximize retailer diversity LUPB1
# obj_func = x.prod(l[r]+u[i,j])- sum(l[r]*a[r]*p[r]*m*k) for i in I for j in U for r in Ir 
obj_func = quicksum((l[r]+u[i,j])*x[i,j]) for i in Ir for r in R for j in U - sum(l[r]*a[r]*p[r]*m*k) for r in R
m1.setObjective(obj_func, GRB.MAXIMIZE)

# save model for inspection
m1.write('LUBP1.lp')
m2.write('LUBP2.lp')

# run optimization engine
m1.optimize()
m2.optimize()
'''