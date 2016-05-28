#!/usr/bin/env python
# coding:utf-8

# ---------------------------------------------------------------------------------------------- [OK]
# [OrderedDict][dict subclass that remembers the order entries were added]

from collections import OrderedDict
d1 = {}
d1['a'] = 1
d1['b'] = 2
d1['c'] = 3
print d1
# {'a': 1, 'c': 3, 'b': 2}
d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2
d2['c'] = 3
print d2
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# ---------------------------------------------------------------------------------------------- [OK]
# [Counter][dict subclass for counting hashable objects]

from collections import Counter
l = [1, 2, 3, 'A', 'B', 'C', 1, 2, 3, 4, 5, 6, (1, 2, 3)]
print l
print sorted(l)
# [1, 1, 2, 2, 3, 3, 4, 5, 6, 'A', 'B', 'C', (1, 2, 3)]
print Counter(l)
# Counter({1: 2, 2: 2, 3: 2, 'A': 1, 4: 1, 5: 1, 6: 1, 'C': 1, (1, 2, 3): 1, 'B': 1})
# ---------------------------------------------------------------------------------------------- [OK]
# [deque][list-like container with fast appends and pops on either end]

from collections import deque
deq = deque(range(5))
print deq
# deque([0, 1, 2, 3, 4])

deq.pop()
print deq
# deque([0, 1, 2, 3])

deq.popleft()
print deq
# deque([1, 2, 3])

deq.append(9)
print deq
# deque([1, 2, 3, 9])

deq.appendleft(-1)
print deq
# deque([-1, 1, 2, 3, 9])

deq.rotate(1)
print deq
# deque([9, -1, 1, 2, 3])

deq.rotate(-2)
print deq
# deque([1, 2, 3, 9, -1])
# ---------------------------------------------------------------------------------------------- [OK]
# [defaultdict][dict subclass that calls a factory function to supply missing values]

from collections import defaultdict
s = 'Once opon a time , there was a superhero called batman , and another superhero named superman .'
words = s.split()
print words
# ['Once', 'opon', 'a', 'time', ',', 'there', 'was', 'a', 'superhero', 'called', 'batman', ',', 'and', 'another', 'superhero', 'named', 'superman', '.']

location = defaultdict(list)
print location
# defaultdict(<type 'list'>, {})

for w in enumerate(words):
    print w
    location[w[1]].append(w[0])
print location
# defaultdict(<type 'list'>,
# 	{
# 		'a': [2, 7],
# 		'and': [12],
# 		'opon': [1],
# 		'superhero': [8, 14],
# 		'batman': [10],
# 		'named': [15],
# 		'there': [5],
# 		',': [4, 11],
# 		'.': [17],
# 		'another': [13],
# 		'time': [3],
# 		'superman': [16],
# 		'was': [6],
# 		'called': [9],
# 		'Once': [0]
# 	 }
#  )
# ---------------------------------------------------------------------------------------------- [OK]
