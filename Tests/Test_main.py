import sys
sys.path.append("./src")
import Main


help = '''script.lua : an example script with help text and a test suite
        (c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
        USAGE:   script.lua  [OPTIONS] [-g ACTION]
        OPTIONS:
        -d  --dump  on crash, dump stack = false
        -g  --go    start-up action      = data
        -h  --help  show help            = false
        -s  --seed  random number seed   = 937162211
        ACTIONS:'''
d = Main.settings(help)

print("Fetched options after running settings function: ", d)

options = Main.cli(d)

print("Fetched options after running cli functions: ",options)

