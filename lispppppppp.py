from lispppppppp.parse import parse
from lispppppppp.environment import Environment
if __name__ == "__main__":
    env = Environment()
    print("""
#############################################################################
### Welcome to LISPPPPPPPP, type a common lisp expression to get started! ###
#############################################################################
""")
    while(True): 
        print(">>", end=" ")
        m = input()
        parsed = parse(m)[0]
        print(parsed.evaluate(env))