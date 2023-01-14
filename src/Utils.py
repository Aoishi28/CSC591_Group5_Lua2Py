import math
import re
class Utils:
    def __init__(self) -> None:
        self.seed = 937162211
    
    # Utility function for numerics
    def rand(self,lo,hi):
        if(lo is None):
            lo=0
        if(hi is None):
            hi=1
        self.seed=(16807*self.seed)%2147483647
        return lo+(hi-lo)*self.seed/2147483647

    def rint(self,lo,hi):
        return math.floor(0.5+self.rand(lo,hi))

    def rnd(self,n,nPlaces):
        if(nPlaces is None):
            nPlaces=3
        mult=math.pow(10,nPlaces)
        return math.floor(n*mult+0.5)/mult

    # Utility functions for lists

    # map a function fun(v) over list (skip nil results)
    def map(self, t, fun):
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
    def kap(self, t, fun):
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
    def sort(self, t, fun):
        return sorted(t, key = fun)
    
    # return sorted list of keys of given list
    def keys(self, t):
        return self.sort(self.kap(t,lambda k,_:k))

    # Utility functions for Strings

    def o(self,t,isKeys):
        if type(t)!=list:
            return str(t)
        def fun(k,v):
            if str(k).find('^_') == -1:
                return format(':{} {}', self.o(k), self.o(v))

        if (len(t)>0 and not isKeys):
            return '{' + ' '.join(str(item) for item in self.map(t,self.o)) + '}'
        else:
            return '{' + ' '.join(str(item) for item in self.kap(t,fun)) + '}'



    def coerce(self,s):
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


        
    
    def oo(self,t):
        print(self.o(t))
        return t
    
