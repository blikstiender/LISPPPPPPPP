import unittest
from lispppppppp.parse import parse
from lispppppppp.environment import Environment

class TestProcedure(unittest.TestCase):
    def test_lambda(self):
        env = Environment()
        expr = parse("(define multip (lambda (x y z) (* x (* y z))))")[0]
        expr.evaluate(env)

        use_lambda = parse("(multip 2 3 4)")[0]
        result = use_lambda.evaluate(env)
        self.assertEqual(result, 24)

        exprs = parse("""
        (define add (lambda (x y) (+ x y)))
        (add (+ 1 2) 3)
        """)
        exprs[0].evaluate(env)
        result = exprs[1].evaluate(env)
        self.assertEqual(result, 6)

    # TODO: do some testing with bound value collisions