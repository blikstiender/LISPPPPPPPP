from .s_expr import SExpression, Atom, Lambda

def add(env, a, b):
    return a.evaluate(env) + b.evaluate(env)

def subtract(env, a, b):
    return a.evaluate(env) - b.evaluate(env)

def multiply(env, a, b):
    return a.evaluate(env) * b.evaluate(env)

def divide(env, a, b): 
    return a.evaluate(env) / b.evaluate(env)

def check_eq(env, a, b):
    return a.evaluate(env) == b.evaluate(env)

def quote(env, *args):
    return args[0]

def cons(env, a, b):
    return SExpression(a, b)

def car(env, a):
    return a.evaluate(env).left

def cdr(env, a):
    return a.evaluate(env).right

def is_atom(env, a): 
    return isinstance(a, Atom)

def define(env, a, b):
    env.bind_value(a.symbol, b.evaluate(env))
    return Atom()

def lambda_def(env, *args): 
    symbols = args[0].get_list()
    proc = args[1]
    return Lambda(symbols, proc)

"""
TODO: implement the remainding fxns: 
    * cond
"""


class Environment: 
    env = {}
    def __init__(self):
        self.env["+"] = add
        self.env["-"] = subtract
        self.env["*"] = multiply
        self.env["/"] = divide
        self.env["eq?"] = check_eq
        self.env["quote"] = quote
        self.env["cons"] = cons
        self.env["car"] = car
        self.env["cdr"] = cdr
        self.env["atom?"] = is_atom
        self.env["define"] = define
        self.env["lambda"] = lambda_def

    def get_bound_value(self, symbol):
        return self.env[symbol]

    def bind_value(self, symbol, s_expr):        
        self.env[symbol] = s_expr

    def replicate(self): 
        new_env = Environment()
        for key in self.env: 
            new_env.bind_value(key, self.get_bound_value(key)) 
        return new_env
