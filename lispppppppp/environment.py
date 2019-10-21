from .s_expr import SExpression, Symbol, Atom

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
    return a.evaluate(env).left.evaluate(env)

def cdr(env, b):
    return b.evaluate(env).right


"""
TODO: implement the remainding fxns: 
    * atom?
    * define
    * lambda
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

    def get_bound_value(self, s_expr):
        if not s_expr.is_atom:
            raise AttributeError("Must be an atom")
        atom = s_expr.evaluate(self)
        if isinstance(atom, Symbol):
            return self.env[atom.symbol]
            
        raise AttributeError("Symbol not bound")
