import math
class SYM:
    def __init__(self) -> None:
        self.n = 0
        self.has = dict()
        self.most = 0
        self.mode = None

    def add(self, x) -> None:
        if x != '?':
            self.n += 1
            if x in self.has:
                self.has[x] += 1
            else:
                self.has[x] = 1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x
            

    def mid(self) -> str:
        return self.mode

    def div(self) -> float:
        
        def fun(p):
            return p*math.log(p,2)
        
        e = 0
        for _, n in self.has.items():
            e += fun(n/self.n)
            
        return -e