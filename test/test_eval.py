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

    def test_only_two_parameted(self): 
        env = Environment()
        expr = parse("(+ 1 1 1)")[0]
        self.assertRaises(TypeError, expr.evaluate, env)


    def test_simple_equality(self):
        env = Environment()
        expr = parse("(eq? 1 1)")[0]
        result = expr.evaluate(env)
        self.assertEqual(result, True)

        env = Environment()
        expr = parse("(eq? 2 1)")[0]
        result = expr.evaluate(env)
        self.assertEqual(result, False)

    def test_quote(self):
        env = Environment()

        expr = parse("(car (quote (1 2)))")[0]
        result = expr.evaluate(env)
        self.assertEqual(result, 1)

        expr = parse("(cdr (quote (1 2)))")[0]
        result = expr.evaluate(env)
        self.assertEqual(result.left.evaluate(env), 2)
        self.assertTrue(result.right.is_nil())

    def test_cons_car_cdr(self):
        env = Environment()
        
        expr = parse("(cons 1 2)")[0]
        result = expr.evaluate(env)
        self.assertEqual(result.left.evaluate(env), 1)
        self.assertEqual(result.right.evaluate(env), 2)

        expr = parse("(car (cons 1 2))")[0]
        result = expr.evaluate(env)
        self.assertEqual(result, 1)

        expr = parse("(cdr (cons 1 2))")[0]
        result = expr.evaluate(env)
        self.assertEqual(result.evaluate(env), 2)