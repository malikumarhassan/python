# Data Types Test
# Numbers int
import cmath
from builtins import print
from collections import deque
from collections import namedtuple
from collections import ChainMap
from collections import  Counter
i = 0
print(i)
print(type(i))

# Numbers float
i = 4.5
print(i)
print(type(i))

# Numbers bool
i = True
print(i)
print(type(i));

# Numbers complex x + (iota)y
x = -1
y = 1
#j = 2
c = complex(x, y)
print(c)
print(c.real)
print(c.imag)
print(cmath.phase(c))
print(type(c))


# strings
i = "malik umar hassan"
print(i)
print(type(i))


# Lists or array (mutable)
fruitsList = ['apple', 'banana', 'mango']
fruitsList[0] = 'mango'
print(fruitsList)
print(fruitsList[0])
print(type(fruitsList))

# Dictionary indexed with key value (mutable)
fruitsDictionary = {'1': 'cherry', '2': 'banana', '3': 'mango'}
print(fruitsDictionary)
print(fruitsDictionary['1'])
print((type(fruitsDictionary)))

# Tuple ordered, cannot change(immutable) , duplicate NOT entries present
fruitsTupple = ('1','2','3', 'malik', 'umar', 'hassan', 'hassan')
print(fruitsTupple)
print(type(fruitsTupple))




# set unordered , immutable, duplicate entries not present
fruitsSet = {'1','2','3', 'mango', 'banana', 'apple', 'apple'}

print(fruitsSet)
print(type(fruitsSet))

#namedtuple immutable
a = namedtuple('courses','name, technology, dept')
'''s = a.make(['arti','python'])
print(s)/'''
s= a('Arti', 'python', 'science')
print(s)

fruitsNamedTuple = namedtuple('ListOfFruits', 'Name, Quality')
fnt = fruitsNamedTuple('Mango', 'A+')
print((fnt))

a = namedtuple('x', 'y, z')
s = a('L','M')
print(s)

# deque (deck) optimized list
a = ['a','b', 'c', 'd']
d = deque(a)
print(d)
d.append(('e'))
print(d)

# chainmap dictionary like class single view of multiple mapping – merge two dictionary

d1 = {'1': 'a', '2' : 'b' }
d2 = {'1' : 'c', '2': 'd'}
d3 = ChainMap(d1,d2)
print(d3)

#Counter count hashable object
a = ['1','1','2']
count = Counter(a)
print(count)

# ORderDict
from collections import  OrderedDict
a = OrderedDict()
a[1] = '0'
a[2]= '1'
print(a)

# Default Dict
from collections import  defaultdict
a = {1: 'Pak', 2: 'Uae'}
#print(a[3]) throw error because key value not exists if not defaultdic

d = defaultdict(int)
d[1] = 'Pak'
d[2] = 'UAE'
print(d[2])
print(d[3])


# Array mutable
from array import*
a = array('b', [1,2,3,4,5,6])
print(a)

print(len(a))

a.append(7) #append at last
print(a)
a.extend([8,9,10]) #append at Last with multiple values
print(a)
a.insert(2,16) # insert at particular index
print(a)


''''
Removing element from array
1. pop() - remove from last with return value
2. pop(2) - reomve from 2 index
3. remove(6) - remove the value 
'''

a.pop()
print(a)

a.pop(0)
print(a)
a.remove(6)
print(a)
# Concatenate array
a = array('d', [1,2,3,4,5,6])
b = array('d',[2.1, 5.6 ,8.9])
c = array('d')



c = a +b
print(c)

#slicing array searching of values
a = array('d', [1,2,3,4,5,6])
print(a[0:1])
