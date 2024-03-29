"""
We use the recursive S-Expression definition which is: an S-Expression is either: 
    1. An Atom.
    2. An S-Expression of the form (A.B) where A and B are both S-Expressions
"""

class Atom:
    symbol = None
    def __init__(self, symbol=None):
        self.symbol = symbol

    def is_nil(self):
        return self.symbol == None 

    def evaluate(self, env):
        if self.is_nil():
            return None

        s = self.symbol
        if isinstance(s, int) or isinstance(s, float) or isinstance(s, bool):
            return s
        try:
            return int(self.symbol)
        except ValueError: 
            try:
                return float(self.symbol)
            except ValueError:
                return env.get_bound_value(self.symbol)

    def __repr__(self):
        if self.is_nil():
            return "nil"
        return self.symbol

class Lambda:
    symbols = []
    procedure = Atom()
    def __init__(self, symbols, procedure):
        self.symbols = symbols
        self.procedure = procedure
    
    def call(self, env, *args): 
        new_env = env.replicate()
        args_l = len(args)
        symb_l = len(self.symbols)
        if args_l != symb_l:
            raise TypeError("Lambda takes {} arguments, {} provided".format(symb_l, args_l))

        for i in range(symb_l):
            symbol_atom = self.symbols[i]
            arg = args[i]
            new_env.bind_value(symbol_atom.symbol, arg.evaluate(new_env))

        return self.procedure.evaluate(new_env)

class SExpression:
    left = None
    right = None
    def __init__(self, *args):
        arg_list = list(args)
        self.left = arg_list[0]
        self.right = arg_list[1]

    def evaluate(self, env):
        bound_value = self.left.evaluate(env)
        args = self.right.get_list()
        eval_val = Atom()
        if isinstance(bound_value, Lambda):
            eval_val = bound_value.call(env, *args)
        else: 
            eval_val = bound_value(env, *args)
        return eval_val

    def get_list(self):
        members = []
        s_expr = self
        while not s_expr.is_nil():
            members.append(s_expr.left)
            s_expr = s_expr.right
        return members

    def is_nil(self): 
        return False

    def __repr__(self):
        """
        As the original paper notes, I do wonder what will happen here once we get hit 
        with some recursion.
        """
        return "({} {})".format(self.left, self.right)
