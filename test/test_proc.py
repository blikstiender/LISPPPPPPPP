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

    def test_cond(self): 
        env = Environment()
        
        exprs = parse("""
        (define a 3)
        (cond ((eq? a 1) 2)
              ((eq? a 2) 4)
              ((eq? a 3) (+ 3 5))
              (else 16))
        """)
        exprs[0].evaluate(env)
        result = exprs[1].evaluate(env)
        self.assertEqual(result, 8)

        exprs = parse("""
        (define check_b (
            lambda (b)
                (cond ((eq? b 1) 2)
                    ((eq? b 2) 4)
                    ((eq? b 3) (+ 3 5))
                    (else 16))))
        (check_b 1)
        (check_b 7)
        """)
        exprs[0].evaluate(env)
        result_a = exprs[1].evaluate(env)
        result_b = exprs[2].evaluate(env)
        self.assertEqual(result_a, 2)
        self.assertEqual(result_b, 16)
