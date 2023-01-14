import sys
import Utils

class Main:

    def cli(self,options):
        vals=options.keys()
        arg=sys.argv
        arg=arg[1:]
        for k in vals:
            v=str(options[k])
            for n,x in enumerate(arg):
                if(x=='-'+ k[0] or x=='--'+k):
                    v= v=="False" and "True" or v=="True" and "False" or arg[n+1]
            options[k]=Utils.coerce(v)

        return options

