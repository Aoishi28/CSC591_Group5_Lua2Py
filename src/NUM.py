import math

class NUM:
    '''
    Summarizes a stream of numbers
    '''

    def __init__(self):
        self.n=0
        self.mu=0
        self.m2=0
        self.lo=math.inf
        self.hi=-math.inf


    def add(self,n):
        '''
        Add 'n', update lo,hi and stuff needed for standard deviation
        '''
        if(n!='?'):
            self.n=self.n+1
            d=n-self.mu
            self.mu=self.mu+d/self.n
            self.m2=self.m2+d*(n-self.mu)
            self.lo=math.min(n,self.lo)
            self.hi=math.max(n,self.hi)
        

    def mid(self):
        '''
        Return mean
        '''
        return self.mu

    def div(self):
        '''
        Return standard deviation using Welford's algorithm http://t.ly/nn_W
        '''
        if(self.m2<0 or self.n<2):
            return 0
        else:
            return math.pow((self.m2/(self.n-1)),0.5)
        
