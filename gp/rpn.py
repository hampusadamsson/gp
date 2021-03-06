import math
import operator


ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.div,
       '^':operator.pow,
       'abs':abs,
       'asin':math.asin,
       'acos':math.acos,
       'atan':math.atan,
       'sinh':math.sinh,
       'cosh':math.cosh,
       'tanh':math.tanh,
       'exp':math.exp,
       'sqrt':math.sqrt,
       'log':math.log,
       'sin':math.sin,
       'tan':math.tan,
       'cos':math.cos}

def nr_inp(o):
    if o == 'pi':
        return 0
    try:
        float(o)
        return 0
    except:
        if o == '+' or  o == '-' or  o == '*' or o == '/' or o == '^':
            return 2
        return 1

def data(x):
    if x=='pi':
        return math.pi
    return float(x)


def solve(equ):
    stack = []
        
    for x in equ.split(' '):
        if nr_inp(x) == 0:
            stack.insert(0,data(x))
            
        elif nr_inp(x) == 1:
            ans = ops.get(x)(stack.pop(0))
            stack.insert(0,ans)
            
        elif nr_inp(x) == 2:
            ans = ops.get(x)(stack.pop(1),stack.pop(0))
            stack.insert(0,ans)

    assert len(stack) == 1
    return stack.pop()



#
#   TEST SUITE
#
def test():
    assert solve("1 1 +") == 2
    assert solve("3 2 *") == 6
    assert solve("1 2 /") == 0.5
    assert solve("2 1 /") == 2
    assert solve("9 sqrt") == 3
    assert solve("2 3 3 * +") == 11
    assert solve("4 5 -") == -1
    assert solve("1 2 + 3 / 1 -") == 0
    assert solve("1 2 + 3 / 2 - -1 *") == 1
    assert solve("1 2 / pi * sin") == 1
    assert solve("0 cos") == 1
    assert solve("pi cos") == -1
    assert solve("-1 pi * cos") == -1
    assert solve("18 3 3 -1 pi * cos * * + sqrt 2 ^") == 9
    assert solve("-1 abs") == 1
    # print solve("x24 2 ^ 2 ~ x3 ∗ sin −")
    print "All tests passed"
test()








