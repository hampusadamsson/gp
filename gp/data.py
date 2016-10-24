import random
import math
import operator

p_err = False

ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.div,
       # '^':operator.pow,
       # 'abs':abs,
       # 'asin':math.asin,
       # 'acos':math.acos,
       # 'atan':math.atan,
       # 'sinh':math.sinh,
       # 'cosh':math.cosh,
       # 'tanh':math.tanh,
       'exp':math.exp,
       'sqrt':math.sqrt,
       'log':math.log,
       'sin':math.sin,
       'tan':math.tan,
       'cos':math.cos}

var = {'pi':math.pi}
# var = {}

nr_var = 57

for x in range(1,nr_var+1):
    var['x'+str(x)] = 0


def get_data(s):
    try:
        res = float(s)
        return res
    except:    
        va = var.get(s)
        if va != None:
            return va

        op = ops.get(s)
        if op != None:
            return op

        return False


def get_rnd_op():
    rnd = random.randint(0,len(ops)-1)
    return ops.keys()[rnd]


def get_rnd_var():
    if random.randrange(0,2) == 1:
        rnd = random.randint(0,len(var)-1)
        return var.keys()[rnd]
    else:
        return random.randrange(1,10)
    
        
def nr_inp(o):
    if o == 'pi':
        return math.pi
    try:
        float(o)
        return 0
    except:
        if var.get(o) != None:
            return 0
        
        if o == '+' or  o == '-' or  o == '*' or o == '/' or o == '^':
            return 2
        return 1


def test():
    equation = "1 2 + 3 *"
    answer = 9
    assert  calculate(equation.split(' ')) == answer
        
    equation = "x1 2 *"
    answer = 4
    assert  calculate(equation.split(' ')) == answer

    equation = "x1 2 * x2 *"
    answer = 12
    assert  calculate(equation.split(' ')) == answer

    equation = "1 4 /"
    answer = 0.25
    assert  calculate(equation.split(' ')) == answer

    equation = "1 4 / 4 *"
    answer = 1
    assert  calculate(equation.split(' ')) == answer

    equation = "0 cos"
    answer = 1
    assert  calculate(equation.split(' ')) == answer

    equation = "1 4 / 4 * 1 - cos"
    answer = 1
    assert  calculate(equation.split(' ')) == answer

    print "data.py: Test passed"
    
# test()
