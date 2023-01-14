import math
import re

seed = 937162211    
# Utility function for numerics
def rand(lo,hi):
    if(lo is None):
        lo=0
    if(hi is None):
        hi=1
    seed=(16807*seed)%2147483647
    return lo+(hi-lo)*seed/2147483647

def rint(lo,hi):
    return math.floor(0.5+rand(lo,hi))

def rnd(n,nPlaces):
    if(nPlaces is None):
        nPlaces=3
    mult=math.pow(10,nPlaces)
    return math.floor(n*mult+0.5)/mult

# Utility functions for lists

# map a function fun(v) over list (skip nil results)
def map( t, fun):
    u = []
    for k,v in enumerate(t):
        o = fun(v)
        v,k = o[0], o[1]
        if k != 0:
            u[k] = v
        else:
            u[1+len(u)] = v  
    return u

# map function fun(k,v) over list (skip nil results)
def kap( t, fun):
    u = []
    for k,v in enumerate(t):
        o = fun(k,v)
        v,k = o[0], o[1]
        if k != 0:
            u[k] = v
        else:
            u[1+len(u)] = v  
    return u

# sort the list with given comparator
def sort( t, fun):
    return sorted(t, key = fun)

# return sorted list of keys of given list
def keys( t):
    return sort(kap(t,lambda k,_:k))

# Utility functions for Strings

def o(t,isKeys):
    if type(t)!=list:
        return str(t)
    def fun(k,v):
        if str(k).find('^_') == -1:
            return format(':{} {}', o(k), o(v))

    if (len(t)>0 and not isKeys):
        return '{' + ' '.join(str(item) for item in map(t,o)) + '}'
    else:
        return '{' + ' '.join(str(item) for item in kap(t,fun)) + '}'



def coerce( s):
    def fun(s1):
        if(s1=='true'):
            return True
        elif(s1=='false'):
            return False
        return s1
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return fun(re.search('^\s*(.+?)\s*$'),s).group((1))
    except Exception as e:
        print("Error 101 : corece_file_crashed")


    

def oo(t):
    print(o(t))
    return t
    
