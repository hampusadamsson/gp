# import matplotlib.pyplot as plt
import copy
from root import *
import random



def plot(vals):
    # plt.plot(vals)
    # plt.ylabel('MSE')    
    # plt.show()
    return 0
    
class ga:
    iterations = 1000000
    pop_size = 1000
    pop = []

    elit = 200
    mut_rate = 0.9
    cross_rate = 0.9
    
    result = []
    train_set = [[3,2,7,8,2,6],[2,2,9,7,2,4],[1,2,3,9,9,81]]

    def load_data(self):
        self.train_set = []
        fname = 'coursework2-training.csv'
        with open(fname) as f:
            content = f.readlines()
        content.pop(0)
        for x in content:
            var = x.split(',')

            tmp = []
            for y in var:
                tmp.append(float(y))
            self.train_set.append(tmp)

    def init(self):        
        for x in range(0, self.pop_size):
            ind = init_root()
            self.pop.append(ind)
        self.pop[0] = in_b()

            
    def evaluate(self):
        for ind in self.pop:
            ind.mse(self.train_set)

    def depth_ctrl(self):
        for ind in self.pop:
            ind.depth_ctrl()

            
    def sort(self):
        self.pop.sort(key=lambda ind: ind.fit, reverse=False)


    def rand_select(self):
        r = random.randrange(0, len(self.pop)-1)
        return self.pop[r]

        
    def rank_select(self):
        total = sum(range(0, len(self.pop) + 1))
        r = random.uniform(0, total)
        tot = 0
        for c in range(0, len(self.pop)+1):
            if tot + c >= r:
                return self.pop[c-1]
            tot += c

            
    def select(self):
        # return self.rank_select()
        return self.rand_select()
        

    def crossover(self):
        p1 = self.select()
        p2 = self.select()
        while(p1==p2):
            p2 = self.select()

        # UPDATE THE TREE DEPTH ALSO *
        child = p1.copy()
        replace_node = child.tree.get_rnd_node()
        p2_node = p2.tree.get_rnd_node()        
        insert_node = p2_node.copy(p2_node)
        insert_node.parent = replace_node.parent

        if replace_node.parent != None:
            if replace_node.parent.left == replace_node:
                replace_node.parent.left = insert_node
            if replace_node.parent.right == replace_node:
                replace_node.parent.right = insert_node
                
        replace_node = insert_node

        return child
                                

    def run(self):
        for i in range(0, self.iterations):
            new_pop = []
            self.depth_ctrl()
            self.evaluate()
            self.sort()
            self.result.append(self.pop[0].fit)


            print "---------------------"
            print i
            print self.pop[0].fit
            print self.pop[0].tree.make_list()

            
            # NODE COUNTING
            tot = 0
            for x in self.pop:
                tot += len(x.tree.tree_to_list())
            print "amount of tree nodes: " + str(tot)

            
            # CROSSOVER
            for x in range(0, int((self.pop_size-self.elit)*self.cross_rate)):
                new_pop.append(self.crossover())
        

            # FILL POP
            while(len(new_pop)!=(self.pop_size-self.elit)):
                new_pop.append(self.pop.pop(random.randrange(self.elit, len(self.pop))))

                
            # MUTATION
            for ind in new_pop:
                val = random.uniform(0, 1)
                if val < self.mut_rate:
                    ind.mutate() # implement mutation in tree

                    
            # ELITISM
            for x in range(0, self.elit):
                new_pop.append(self.pop.pop(0))


                
            self.pop = new_pop
            
        # END CHECK
        self.evaluate()
        self.sort()

        return self.pop[0]

    
def batch():
    gan = ga()
    gan.load_data()
    gan.init()

    best = gan.run()
    
    print "---"
    print best.tree.make_list()
    print "MSE: " + str(best.fit)
    print "---"

    #plotting
    plot(gan.result)

    
batch()
    
