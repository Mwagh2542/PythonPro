import numpy as np
a = np.array([(1,2,3), (3,5,6)])
b = np.array([(1,2,3), (3,5,6)])
print(np.hstack((a,b)),'\n')

print(np.vstack((a,b)))
print(a.ravel())
'''
print (a.sum(axis = 0))
print (a.sum(axis = 1))
print ("adddition", a + b)
print (a * b)
print (a / b)
'''
