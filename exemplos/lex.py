import re
from pprint import pprint 
from typing import NamedTuple

code = open('exemplo.js').read()
exprs = {
    "NAME": r"[a-zA-Z]\w*",
    "NUMBER": r"\d+(\.\d+)?",
    "OP": r"==|<=|>=|[-+*/<>]",
    "SYMB": r"[(){}[\];]",
    "NEWLINE": r"\n",
    "IGNORE": r"[ \t]+",
    "ERROR": r".",
}

groups = (f"(?P<{k}>{v})" for k, v in exprs.items())
regex = re.compile('|'.join(groups))


class Token(NamedTuple):
    kind: str
    value: str
    lineno: int = None
    column: int = None


def lex(code):
    lineno = 0
    column = 0
    tokens = []

    for m in regex.finditer(code):
        kind = m.lastgroup
        value = m.group()
        
        if kind == 'IGNORE':
            continue
        elif kind == 'ERROR':
            raise SyntaxError(f"valor inválido em ({lineno}, {column}): {value}")
        elif kind == 'NEWLINE':
            column = 0
            lineno += 1
            continue
        
        column += len(value)
        token = Token(kind, value, lineno, column)
        tokens.append(token)
    
    return tokens

pprint(lex(code))