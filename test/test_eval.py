import unittest
from lispppppppp.environment import Environment
from lispppppppp.parse import parse

class TestBasicOperations(unittest.TestCase):
    def test_arithmetic(self):
        env = Environment()
        
        # Evaluate add
        expr = parse("(+ 1 2)")[0]
        result = expr.evaluate(env)
        self.assertEqual(result, 3)

        # Evaluate subtract
        expr = parse("(- 4 2)")[0]
        result = expr.evaluate(env)
        self.assertEqual(result, 2)

        # Evaluate multiply
        expr = parse("(* 4 2)")[0]
        result = expr.evaluate(env)
        self.assertEqual(result, 8)

        # Evaluate divide
        expr = parse("(/ 3 2)")[0]
        result = expr.evaluate(env)
        self.assertEqual(result, 1.5) # NOTE: this would be wrong in python 2 but I'm 
                                      # gonna go ahead and assume python 3. 

        # Evaluate compounded expressions
        expr = parse("(+ (- 7 1) (* 2 4))")[0]
        result = expr.evaluate(env)
        self.assertEqual(result, 14)

    