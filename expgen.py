
import numpy as np
import pandas as pd

def step_gen_csv(start,step,step_count,f,directory):
    temp = []
    indexes = range(step_count)
    sofar = 0
    for i in indexes:
        temp.append([sofar,f(sofar)])
        sofar+=step
    df = pd.DataFrame(temp,index = indexes,columns = ['x','fx'])
    df.to_csv(directory)



f = lambda x: np.exp(x+2) - 8

step_gen_csv(1, 0.5, 10 , f, 'exp.csv');
