import re
from pprint import pprint 
from typing import NamedTuple
NOT_GIVEN = object()


class Token(str):
    kind: str
    value: str
    lineno: int
    column: int

    def __new__(cls, kind, data, lineno=None, column=None, value=NOT_GIVEN):
        new = str.__new__(cls, data)
        new.kind = kind
        new.value = data if value is NOT_GIVEN else value
        new.lineno = lineno
        new.column = column
        return new
    
    def __repr__(self):
        return f'<{self.kind} {self.value!r}>'


class Lexer:
    def __init__(self, token_map, ignore=('IGNORE',), transforms={}):
        groups = (f"(?P<{k}>{v})" for k, v in token_map.items())
        pattern = '|'.join(['(?P<NEWLINE>\n+)', *groups, '(?P<ERROR>.)'])
        
        self._regex = re.compile(pattern)
        self.ignore = set(ignore)
        self.transforms = dict(transforms)

    def lex(self, src):
        """
        Retorna uma sequência de tokens.
        """
        lineno = 0
        column = 0
        ignore = self.ignore
        transforms = self.transforms
        identity = lambda x: x

        for m in self._regex.finditer(src):
            kind = m.lastgroup
            data = m.group()
            
            if kind in ignore:
                continue
            elif kind == 'ERROR':
                raise SyntaxError(f"valor inválido em ({lineno}, {column}): {data}")
            elif kind == 'NEWLINE':
                column = 0
                lineno += 1
                continue
            
            column += len(data)
            value = transforms.get(kind, identity)(data)
            token = Token(kind, data, lineno, column, value=value)
            yield token
        

if __name__ == '__main__':
    lex = Lexer({
        "NUMBER": r"\d+(\.\d+)?",
        "NAME": r"[a-zA-Z_0-9]+",
        "OP": r"[-+*/=]",
        "IGNORE": r"[ \t]+",
    })
    print(list(lex.lex("x = 42 + 1")))

