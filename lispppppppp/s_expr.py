"""
We use the recursive S-Expression definition which is: an S-Expression is either: 
    1. An Atom.
    2. An S-Expression of the form (A.B) where A and B are both S-Expressions
"""

class Symbol: 
    symbol = None
    def __init__(self, symbol):
        self.symbol = symbol


class Atom:
    is_atom = True
    symbol = None
    def __init__(self, symbol=None):
        self.symbol = symbol

    def is_nil(self):
        return self.symbol == None 

    def evaluate(self, environment):
        try:
            return int(self.symbol)
        except ValueError: 
            try:
                return float(self.symbol)
            except ValueError:
                return Symbol(self.symbol)

    def __repr__(self):
        if self.is_nil():
            return "nil"
        return self.symbol

class SExpression:
    is_atom = False
    left = None
    right = None
    def __init__(self, *args):
        arg_list = list(args)
        if len(arg_list) == 1:
            self.is_atom = True
            self.left = arg_list[0]
        else:
            self.left = arg_list[0]
            self.right = arg_list[1]

    def is_nil(self):
        return self.is_atom and self.left.is_nil()

    def evaluate(self, environment):
        if self.is_atom:
            return self.left.evaluate(environment)
        
        bound_value = environment.get_bound_value(self.left)
        args = self.right.get_list()
        evaled_args = list(map(lambda a: a.evaluate(environment), args))
        return bound_value(environment, *evaled_args)

    def get_list(self):
        members = []
        s_expr = self
        while not s_expr.is_nil():
            members.append(s_expr.left)
            s_expr = s_expr.right
        return members



    def __repr__(self):
        """
        As the original paper notes, I do wonder what will happen here once we get hit 
        with some recursion.
        """
        if self.is_atom:
            return self.left.__repr__()
        return "({} {})".format(self.left, self.right)