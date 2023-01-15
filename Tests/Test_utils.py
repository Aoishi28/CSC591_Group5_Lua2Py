import sys
sys.path.append("./src")
import Utils

# testing coerce
s1 = Utils.coerce('true')
print(s1, type(s1))

s2 = Utils.coerce('false')
print(s2, type(s2))

s3 = Utils.coerce('normal_string')
print(s3, type(s3))

s4 = Utils.coerce('1')
print(s4, type(s4))

s5 = Utils.coerce('2.5')
print(s5, type(s5))

s6 = Utils.coerce('0s')
print(s6, type(s6))
