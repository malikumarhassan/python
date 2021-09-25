from collections import namedtuple

a = namedtuple('courses', 'name ,TechnologyName')
s = a('DCS', 'C++')
print(s)
