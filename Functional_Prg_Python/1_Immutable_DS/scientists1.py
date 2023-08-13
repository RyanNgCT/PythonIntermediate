import collections
from pprint import pprint

# define Scientist object
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobelAwarded',
])

print(Scientist)

ada = Scientist(name='Ada Lovelace', field='Math', born=1815, nobelAwarded=False)
emmy = Scientist(name='Emmy Noether', field='Math', born=1882, nobelAwarded=False)
marie = Scientist(name='Marie Curie', field='Physics', born=1867, nobelAwarded=True)
youyou = Scientist(name='Tu Youyou', field='Chemistry', born=1930, nobelAwarded=True)

# storing immutable data structure in mutable ones.
scientistsList = [ada, emmy, marie, youyou]
print(ada.name + "\n")

# ada.name = "ed" # cannot set attribute

pprint(scientistsList)

# can still delete and modify the list
del scientistsList[1]
pprint(scientistsList)
