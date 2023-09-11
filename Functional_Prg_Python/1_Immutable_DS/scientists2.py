import collections
from pprint import pprint

# define Scientist factory function (sort of like an object)
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobelAwarded',
])

ada = Scientist(name='Ada Lovelace', field='Math', born=1815, nobelAwarded=False)
emmy = Scientist(name='Emmy Noether', field='Math', born=1882, nobelAwarded=False)
marie = Scientist(name='Marie Curie', field='Physics', born=1867, nobelAwarded=True)
youyou = Scientist(name='Tu Youyou', field='Chemistry', born=1930, nobelAwarded=True)
ada2 = Scientist(name='Ada Lovelace', field='Math', born=1815, nobelAwarded=False)

# storing immutable data structure in mutable ones.
scientistsTpl = (ada, emmy, marie, youyou, ada2) # allows duplicate element as it is not a set.
print(ada.name + "\n")

pprint(scientistsTpl)

# does not work anymore -> 'tuple' object doesn't support item deletion
del scientistsTpl[2]
pprint(scientistsTpl)

# gets rid of duplicate Object
scientistSet = {ada, emmy, marie, youyou, ada2}
pprint(scientistSet)
