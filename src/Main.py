import sys
from Utils import coerce
import re



def cli(options):
    vals=options.keys()
    arg=sys.argv
    arg=arg[1:]
    for k in vals:
        v=str(options[k])
        for n,x in enumerate(arg):
            if(x=='-'+ k[0] or x=='--'+k):
                v= v=="False" and "True" or v=="True" and "False" or arg[n+1]
        options[k] = coerce(v)

    return options

def settings(help):
    try:
        return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", help))
    except Exception as e:
        print("Error occurred while parsing the help string:\n", e)

def main(options,help,funs):
    
    saved = dict()
    fails = 0
    for k,v in cli(settings(help)).items():
        options[k] = v
        saved[k] = v
    
    if options['help']:
        print(help)
    else:
        for what, fun in funs.items():
            if options['go'] == 'all' or what == options['go']:
                for k,v in saved.items():
                    options[k] = v
                Seed = options['seed']
                if funs[what]() == False:
                    fails += 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)
            


