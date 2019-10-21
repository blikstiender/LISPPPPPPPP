from lispppppppp.parse import parse, tokenize
from lispppppppp.s_expr import SExpression, Atom
import unittest

class TestNormalizing(unittest.TestCase):
    def test_tokenization(self):
        program = '(1 2 3 4)'
        tokens = tokenize(program)
        expected_tokens = ['(', '1', '2', '3', '4', ')']
        self.assertEqual(tokens, expected_tokens)

    def test_parse(self):
        program = "(1 2 (3 4 5 6 7 8 (9 10)))"
        parsed = parse(program)
        s_expr = parsed[0] 
        self.assertTrue(isinstance(s_expr.left, Atom))
        self.assertTrue(isinstance(s_expr.right, SExpression))