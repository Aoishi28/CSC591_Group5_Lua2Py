class Utils:
    def __init__(self) -> None:
        self.seed = 937162211
    
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
    
