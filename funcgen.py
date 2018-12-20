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

def gen_csv(x,f,directory):
    temp = []
    arr = sorted(x)
    indexes = range(len(arr))
    for i in indexes:
        temp.append([arr,f(arr[i])])
    df = pd.DataFrame(temp,index = indexes,columns = ['x','fx'])
    df.to_csv(directory)

def get_csvfunc(directory):
    try:
        df = pd.read_csv(directory)
        return np.array(df.x),np.array(df.fx)
    except:
        print("Not valid csv")
        return None,None
    
def get_csvfunc_list(directory):
    try:
        df = pd.read_csv(directory)
        return list(df.x),list(df.fx)
    except:
        print("Not valid csv")
        return None,None 
