import copy
from tree import *


class root:
    tree = None
    fit = None
    depth = 7
    
    
    def init(self):
        self.tree = init_tree(self.depth)

        
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
                        
        self.fit = mse
        return mse

    
def init_root():
    ind = root()
    ind.init()
    # print ind.tree.make_list()
    return ind

