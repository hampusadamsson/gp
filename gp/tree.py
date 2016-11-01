from data import *


class tree:
    parent = None
    left = None
    right = None
    data = None
    
    mut_op_val_rate = 0.75 # 1= value, 0= op

    
    def copy(self, target):
        ntree = tree()
        ntree.data = target.data
        
        if target.left != None:
            ntree.left = ntree.copy(target.left)
            ntree.left.parent = ntree
        if target.right != None:
            ntree.right = ntree.copy(target.right)
            ntree.right.parent = ntree
        return ntree

    
    def depth_ctrl(self, max_d):
        if max_d == 0:
            self.left = None
            self.right = None

            if nr_inp(self.data) != 0:
                self.data = get_rnd_var()
            
        if self.left != None and self.right != None:
            self.left.depth_ctrl(max_d-1)
            self.right.depth_ctrl(max_d-1)
        elif self.left != None:
            self.left.depth_ctrl(max_d-1)
        elif self.right != None:
            self.right.depth_ctrl(max_d-1)

    
    def tree_to_list(self):
        if self.left != None and self.right != None:
            return self.left.tree_to_list() + self.right.tree_to_list() + [self]
        elif self.left != None:
            return self.left.tree_to_list() + [self]
        elif self.right != None:
            return self.right.tree_to_list() + [self]
        return [self]    

    
    def make_list(self):
        if self.left != None and self.right != None:
            return self.left.make_list() + self.right.make_list() + [self.data]
        elif self.left != None:
            return self.left.make_list() + [self.data]
        elif self.right != None:
            return self.right.make_list() + [self.data]
        return [self.data]


    def get_subtree(self, eq):
        stack = []
        i = 1
        while i != 0:
            # print eq
            # print stack
            
            val = eq.pop()
            stack.insert(0, val)
            i += nr_inp(val)
            i -= 1
        return stack

    
    def insert(self, equ):
        self.data = equ.pop()

        if len(equ) != 0:
            ntree = tree()
            ntree.parent = self
            tmp = self.get_subtree(equ)
            if len(equ) == 0:
                self.left = ntree
            else:
                self.right = ntree

            ntree.insert(tmp)
        if len(equ) != 0:
            ntree = tree()
            ntree.parent = self
            self.left = ntree
            tmp = self.get_subtree(equ)
            ntree.insert(tmp)

                
    def equ2tree(self, equ):
        val = equ.split(' ')
        self.insert(val)
        

    def add(self, depth):        
        if depth == 1:
            self.data = get_rnd_var()
            
        elif depth > 1:
            self.data = get_rnd_op()
            ntree = tree()
            ntree.parent = self
            self.left = ntree
            ntree.add(depth-1)
            if nr_inp(self.data) == 2:
                ntree = tree()
                ntree.parent = self
                self.right = ntree
                ntree.add(depth-1)
        

    def get_rnd_node(self):
        ls = self.tree_to_list()
        rnd = random.randrange(0, len(ls))
        node = ls[rnd]
        return node


    def mutate(self):
        node = self
        r = random.uniform(0, 1)

        if r < self.mut_op_val_rate:
            node.data = get_rnd_var()
            node.left = None
            node.right = None
        else:
            node.data = get_rnd_op()

            if nr_inp(node.data) == 1:
                if (node.left != None and node.right != None):
                    node.right = None
                elif (node.left == None and node.right == None):
                    tmp = tree()
                    tmp.parent = node
                    tmp.data = get_rnd_var()
                    node.left = tmp
                
            elif nr_inp(node.data) == 2:
                if node.left == None:
                    tmp = tree()
                    tmp.parent = node
                    tmp.data = get_rnd_var()
                    node.left = tmp

                if node.right == None:
                    tmp = tree()
                    tmp.parent = node
                    tmp.data = get_rnd_var()
                    node.right = tmp


    def create_tree(self, ls):
        val = ls.pop(-1)
        self.data = val
        
        if nr_inp(val) == 2:
            tmp = tree()
            tmp.parent = self
            self.left = tmp
            ls = tmp.create_tree(ls)
            
            tmp1 = tree()
            tmp1.parent = self
            self.right = tmp1
            tmp1.create_tree(ls)
            
        if nr_inp(val) == 1:
            tmp = tree()
            tmp.parent = self
            self.left = tmp
            tmp.create_tree(ls)
            
        return ls
    

    def calc(self, x_var):
        if type(self.data)!=int and self.data[0] == 'x':
            return x_var[int(self.data[1:])-1]
        
        data = get_data(self.data)
        
        if nr_inp(self.data) == 2:
            ans1 = self.right.calc(x_var)
            ans2 = self.left.calc(x_var)
            try:
                ans = data(ans1,ans2)
            except:
                return False
        
        elif nr_inp(self.data) == 1:
            ans1 = self.left.calc(x_var)
            try:
                ans = data(ans1)
            except:
                return False

        else:
            ans = data
        return ans


    # def calc(self, x_var):
    #     if type(self.data)!=int and self.data[0] == 'x':
    #         return x_var[int(self.data[1])-1]
        
    #     data = get_data(self.data)
        
    #     if nr_inp(self.data) == 2:
    #         ans1 = self.left.calc(x_var)
    #         ans2 = self.right.calc(x_var)
    #         try:
    #             ans = data(ans1,ans2)
    #         except:
    #             return False
        
    #     elif nr_inp(self.data) == 1:
    #         ans1 = self.left.calc(x_var)
    #         try:
    #             ans = data(ans1)
    #         except:
    #             return False

    #     else:
    #         ans = data
    #     return ans

    
def init_tree(depth):
    ntree = tree()
    ntree.add(depth)    
    return ntree
