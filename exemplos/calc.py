from lark import Lark, InlineTransformer
import math
 
grammar = Lark(r"""
?start : expr

?expr  : expr "+" term  -> sum
       | expr "-" term  -> sub
       | term
 
?term  : term "*" pow  -> mul
       | term "/" pow  -> div
       | pow

?pow   : atom "^" pow  -> exp
       | atom

?atom  : NUMBER            -> number
       | NAME "(" expr ")" -> fcall
       | "(" expr ")"

NUMBER : /-?\d+(\.\d+)?/
NAME   : /\w+/
%ignore /\s+/
""")


class CalcTransformer(InlineTransformer):
    def number(self, token):
        return float(token)

    def sum(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    
    def mul(self, x, y):
        return x * y
    
    def div(self, x, y):
        return x / y

    def exp(self, x, y):
        return x ** y

    def fcall(self, name, x):
        name = str(name)
        fn = getattr(math, name)
        return fn(x)

transformer = CalcTransformer()


exprs = [
    "42",
    "3.14",
    "-10",
    "40 + 2",
    "21 * 2",
    "80 - 38",
    "84 / 2",
    "1 + 1 + 1",
    "1 + 1 - 1",
    "2 * 2 * 2 / 8",
    "20 * 2 + 2",
    "2 + 20 * 2",
    "32 / 4 / 2",
    "10 - 2 - 3",
    "(2 + 20) * 2",
    "(2 + (10 + 10) / 4) * 2",
    "3^2",
    "2 * 3^2",
    "3^2^3",
    "sqrt(4)",
    "1 + sqrt(25)",
]


for src in exprs:
    print(src)
    
    tree = grammar.parse(src)
    print(tree.pretty())
    
    result = transformer.transform(tree)
    print(result)
    
    print('-' * 40)