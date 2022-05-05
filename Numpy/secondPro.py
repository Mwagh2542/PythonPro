import numpy as np

a = np.array([(1,2,3,13),(4,5,6,14),(7,8,9,15), (10,11,12,16)])
print ('1. First Row and Second coloum displayed = ', a,)
print ('2. Here 0 Index and position 2 start from 0 = ', a[0,2],'\n')
print ('3. Here All Index and position 2 start from 0 = ', a[0:,2],'\n')
print ('4. Till 2 Index and position 3 after 0 use : Coln = ', a[0:2,3],'\n')

a = a.reshape(2,8)
print ('5. number of elements represent = ', a, '\n')

a = np.linspace(1,3,5)
print ('6 Here All Index and position 2 after 0 use : Coln = \n', a)