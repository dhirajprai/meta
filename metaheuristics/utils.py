import math
import numpy as np
import random
import pandas as pd


def greedyselector(p1,new_p1):
    for i in range(len(p1)):
        if p1.loc[i]['f']>new_p1.loc[i]['f']:
            p1.loc[i]=new_p1.loc[i]
    return p1



def initialpopulation(mini,maxi,pop_size):
    
    pop=[]
    
    for i in range(pop_size):
        p=[]
        for a,b in zip(mini,maxi):
            p.append(a + (b-a) * random.random())
        pop.append(p)
    ini_pop=pd.DataFrame(pop)    
    return ini_pop

def jaya(*argv):
    pop_size, Gen, mini, maxi = argv
    lb=np.array(mini)
    ub=np.array(maxi)
    p1=initialpopulation(lb,ub,pop_size)
    p1['f']=myobj(p1)
    dim=len(lb)
    gen=0
    best=[]
    while (gen<Gen):
        new_p1=updatepopulation(p1,dim)
        new_p1=trimr(new_p1,lb,ub)
        new_p1['f']=myobj(new_p1)
        p1=greedyselector(p1,new_p1)
        gen=gen+1
    #     print(gen)
        best=p1['f'].min()
        xbest=p1.loc[p1['f'].idxmin()][0:dim].tolist()
#     print('Best={}'.format(best))
#     print('xbest={}'.format(xbest))
    return best,xbest


def trimr(new_p1,lb,ub):
    col=new_p1.columns.values
    for i in range(len(p1)):
        for j in range(len(col)):
            if new_p1.loc[i][j]>ub[j]:
                new_p1.loc[i][j]=ub[j]
            elif new_p1.loc[i][j]<lb[j]:
                new_p1.loc[i][j]=lb[j]
    return new_p1

def updatepopulation(p1,dim):
    best_x=np.array(p1.loc[p1['f'].idxmin][0:dim])
    worst_x=np.array(p1.loc[p1['f'].idxmax][0:dim])
    new_x=[]
    
    for i in range(len(p1)): 
        old_x=np.array(p1.loc[i][0:dim])
        r1=np.random.random(dim)
        r2=np.random.random(dim)
        new_x.append(old_x+r1*(best_x-abs(old_x))-r2*(worst_x-abs(old_x)))
    new_p1=pd.DataFrame(new_x)
    return new_p1
