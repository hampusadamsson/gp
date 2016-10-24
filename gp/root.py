import copy
from tree import *

class root:
    tree = None
    fit = None
    depth = 3
    max_depth = 7
    
    def init(self):
        self.tree = init_tree(self.depth)

    def depth_ctrl(self):
        self.tree.depth_ctrl(self.max_depth)
    
    def mutate(self):
        node = self.tree.get_rnd_node()
        node.mutate()

        
    def copy(self):
        ind = root()
        ind.tree = tree()
        ind.tree = ind.tree.copy(self.tree)
        return ind

    
    def mse(self, train_set):
        mse = 0

        for xset in train_set:
            target = xset[-1]
            inp = xset[:-1]
            ans = self.tree.calc(inp)
            try:
                mse += (ans-target)**2
            except:
                self.fit = float('inf')
                return float('inf')
                        
        mse /= len(train_set)
        self.fit = mse
        return mse

def in_b():
    ind = root()
    tr = tree()
    ind.tree = tr
    eq = "x45 x9 + 3 x17 - sin - sqrt x9 x1 x3 - - sqrt x8 x9 + x6 + sin + + 1 5 * x6 cos + x54 x53 log + cos + x8 x9 + x5 - cos cos + + sqrt"

    tr.equ2tree(eq)
    # print eq.split(' ')
    # print tr.make_list()
    # print  eq.split(' ') == tr.make_list()
    return ind

    

    
def init_root():
    ind = root()
    ind.init()
    return ind


in_b()
