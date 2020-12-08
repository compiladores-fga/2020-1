from lark import Lark, InlineTransformer
import math
 
#
# Exercício
#
# Implementar os operadores bitwise |, ^ e &
# 
# - Associatividade a esquerda
# - Operador & possui precedencia maior que | e ^
# - Operadores |, ^ possuem precedência maior que 
#   as operações matemáticas

grammar = Lark(r"""
?start : assign* expr ";"?

assign : NAME "=" expr ";"

?expr  : expr "+" term  -> sum
       | expr "-" term  -> sub
       | term
 
?term  : term "*" pow  -> mul
       | term "/" pow  -> div
       | pow

?pow   : bitor "**" pow  -> exp
       | bitor

?bitor : bitor "^" bitand  -> bitxor
       | bitor "|" bitand  -> bitor
       | bitand

?bitand : bitand "&" atom -> bitand
        | atom

?atom  : NUMBER            -> number
       | NAME "(" expr ")" -> fcall
       | NAME              -> var
       | "(" expr ")"

NUMBER : /-?\d+(\.\d+)?/
NAME   : /[\w_]+/
%ignore /\s+/
""")


class CalcTransformer(InlineTransformer):
    def __init__(self):
        super().__init__()
        self.env = {}
    
    def number(self, token):
        try:
            return int(token)
        except ValueError:
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

    def bitand(self, x, y):
        return x & y

    def bitor(self, x, y):
        return x | y

    def bitxor(self, x, y):
        return x ^ y

    def fcall(self, name, x):
        name = str(name)
        fn = getattr(math, name)
        return fn(x)

    def assign(self, name, value):
        self.env[name] = value

    def var(self, name):
        return self.env[name]

    def start(self, *args):
        return args[-1]


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
    "3**2",
    "2 * 3**2",
    "3**2**3",
    "sqrt(4)",
    "1 + sqrt(25)",
    "1 ^ 2 + 3", # => 0b01 ^ 0b10 = 0b11 = 6
    "3 + 2 ^ 1", # => 6
    "1 | 2 & 3", # => 0b01 | (0b10 & 0b11) = 0b11 = 3
    "1 ^ 2 & 3", # => 0b01 ^ (0b10 & 0b11) = 0b11 = 3
    "x = 20 + 20; y = 2; x + y",
]


for src in exprs:
    print(src)
    
    tree = grammar.parse(src)
    print(tree.pretty())
    
    result = transformer.transform(tree)
    print(result)
    
    print('-' * 40)