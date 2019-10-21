from .s_expr import SExpression, Atom

def nest_tokenized_expression(tokens):
    if ")" not in tokens and "(" not in tokens: 
        return tokens

    expressions = []
    current_expr_start_index = 0
    current_expression_open = False
    open_bracket_count = 0
    for i in range(len(tokens)):
        token = tokens[i]
        if current_expression_open == False:
            if token == "(":
                current_expression_open = True
                open_bracket_count += 1
            else: # we have an atom
                expressions.append(token)
                current_expr_start_index = i + 1
            continue
        
        if token == ")":
            open_bracket_count -= 1
        elif token == "(":
            open_bracket_count += 1
        
        if open_bracket_count == 0:
            expr_tokens = tokens[current_expr_start_index+1:i]            
            expressions.append(nest_tokenized_expression(expr_tokens))
            current_expr_start_index = i + 1
            current_expression_open = False
    
    if open_bracket_count > 0:
        raise SyntaxError("Malformed program")
    
    return expressions

def form_ast_from_nested_expr(nested_expr):
    if isinstance(nested_expr, list):
        if len(nested_expr) == 0:
            return Atom() # nil atom
        return SExpression(form_ast_from_nested_expr(nested_expr[0]), form_ast_from_nested_expr(nested_expr[1:]))
    
    return Atom(nested_expr)



def tokenize(program):
    return program.replace(")", " )").replace("(", "( ").split()

def parse(program):
    """
    Parse the complete program into a list of expressions and produce the corresponding abstract 
    syntax trees. The first line of this method is drawn from Peter Norvig's lis.py. I've tried 
    avoiding looking at that particular reference implementation more than once (feels like looking
    at the solutions to a homeword assignment) but a couple of the "tricks" he uses stuck with me
    """
    tokens = tokenize(program)
    nested_expressions = nest_tokenized_expression(tokens)
    trees = list(map(lambda t: form_ast_from_nested_expr(t), nested_expressions))
    return trees