from root import *
from tree import *
import sys

train_set = [[]]


# eq = sys.argv[1] 
# fname = sys.argv[2] 
eq = "x24 2 ^ 2 ~ x3 * sin -"
fname = 'coursework2-training.csv'

train_set = []
with open(fname) as f:
    content = f.readlines()
content.pop(0)
for x in content:
    var = x.split(',')
    tmp = []
    for y in var:
        tmp.append(float(y))
    train_set.append(tmp)


ind = root()
tr = tree()
ind.tree = tr

tr.equ2tree(eq)
# print eq
# print tr.make_list()


print ind.mse(train_set)
# print ind.mse([[3,6,9,1]])

