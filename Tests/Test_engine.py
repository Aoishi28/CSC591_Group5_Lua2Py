import sys
sys.path.append("./src")
from NUM import NUM
from SYM import SYM
import Utils
import Main
from Egs import Egs


help = '''   
script.lua : an example script with help text and a test suite
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
'''

the = Main.cli(Main.settings(help))

tester = Egs(help)


def test1():
    Utils.oo(the)

def test2():
    num1, num2 = NUM(), NUM()
    
    Utils.seed = the['seed']
    for i in range(1, 1001):
        num1.add(Utils.rand(0,1))
    
    Utils.seed = the['seed']
    for i in range(1, 1001):
        num2.add(Utils.rand(0,1))
    
    m1, m2 = Utils.rnd(num1.mid(), 10), Utils.rnd(num2.mid(), 10) 
    
    return m1 == m2 and 0.5 == Utils.rnd(m1,1)

def test3():
    sym =SYM()
    l = ['a','a','a','a','b','b','c']
    for i in l:
        sym.add(i)
    return "a" == sym.mid() and 1.379 == Utils.rnd(sym.div(), None)
    

def test4():
    num = NUM()
    l = [1,1,1,1,2,2,3]
    for n in l:
        num.add(n)
    return 11/7 == num.mid() and 0.787 == Utils.rnd(num.div(), None)

tester.eg("the", "show settings", test1)
tester.eg("rand", "generate, reset, regenerate same", test2)
tester.eg("sym", "check syms", test3)
tester.eg("num", "check nums", test4)


Main.main(the, tester.help, tester.egs)






