#!/usr/bin/python

from random import seed
from random import random

seed(7)
for _ in range(5):
	print(random())
print('Reseeded')
seed(7)
for _ in range(5):
	print(random())
