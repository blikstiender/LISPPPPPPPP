from lispppppppp.parse import parse
from lispppppppp.environment import Environment


welcome_string = """
#############################################################################
### Welcome to LISPPPPPPPP, type a common lisp expression to get started! ###
#############################################################################
"""


if __name__ == "__main__":
    env = Environment()
    print(welcome_string)
    while(True): 
        print(">>", end=" ")
        m = input()
        parsed = parse(m)[0]
        print(parsed.evaluate(env))