from .s_expr import SExpression, Atom, Lambda

def evaluate_atom_result(fxn):
    def run(env, *args):
        result = fxn(env, *args)
        if isinstance(result, Atom): 
            return result.evaluate(env)
        return result
    return run

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

def quote(env, a):
    return a

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

def cond(env, *args): 
    for i in range(len(args)):
        arg = args[i]
        if i == len(args) - 1 and isinstance(arg.left, Atom) and arg.left.symbol == "else":
            return arg.right.left.evaluate(env)
        if (arg.left.evaluate(env)): 
            return arg.right.left.evaluate(env)

    return Atom()

class Environment: 
    env = {}
    def __init__(self):
        self.env["+"] = evaluate_atom_result(add)
        self.env["-"] = evaluate_atom_result(subtract)
        self.env["*"] = evaluate_atom_result(multiply)
        self.env["/"] = evaluate_atom_result(divide)
        self.env["eq?"] = evaluate_atom_result(check_eq)
        self.env["quote"] = quote
        self.env["cons"] = evaluate_atom_result(cons)
        self.env["car"] = evaluate_atom_result(car)
        self.env["cdr"] = evaluate_atom_result(cdr)
        self.env["atom?"] = evaluate_atom_result(is_atom)
        self.env["define"] = define
        self.env["lambda"] = lambda_def
        self.env["cond"] = cond

    def get_bound_value(self, symbol):
        return self.env[symbol]

    def bind_value(self, symbol, s_expr):        
        self.env[symbol] = s_expr

    def replicate(self): 
        new_env = Environment()
        for key in self.env: 
            new_env.bind_value(key, self.get_bound_value(key)) 
        return new_env
