from .s_expr import SExpression, Symbol, Atom

def add(env, *args):
    return args[0] + args[1]

def subtract(env, *args):
    return args[0] - args[1]

def multiply(env, *args):
    return args[0] * args[1]

def divide(env, *args): 
    return args[0] / args[1]

class Environment: 
    env = {}
    def __init__(self):
        self.env["+"] = add
        self.env["-"] = subtract
        self.env["*"] = multiply
        self.env["/"] = divide

    def get_bound_value(self, s_expr):
        if not s_expr.is_atom:
            raise AttributeError("Must be an atom")
        atom = s_expr.evaluate(self)
        if isinstance(atom, Symbol):
            return self.env[atom.symbol]
            
        raise AttributeError("Symbol not bound")
