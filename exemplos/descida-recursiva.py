import re

REGEX_MAP = {
    "STRING"  : r'"[^"\n]*"', 
    "NUMBER"  : r'-?\d+(\.\d+)?', 
    "LITERAL" : r'true|false|null',
    "OP"      : r'[{}[\],:]',
    "WS"      : r'\s+',
    "ERROR"   : r'.',
}



class Token(str):
    kind : str

    def __new__(cls, value, kind):
        tk = str.__new__(cls, value)
        tk.kind = kind
        return tk

    def __repr__(self):
        value = super().__repr__()
        return f'Token({value}, {self.kind})'


class JsonParser:
    REGEX = re.compile('|'.join(
        f'(?P<{k}>{v})' for k, v in REGEX_MAP.items()
    ))

    def lex(self, src) -> list:
        tokens = []
        for m in self.REGEX.finditer(src):
            kind = m.lastgroup
            value = src[m.start():m.end()]
            tk = Token(value, kind)
            if kind == 'WS':
                continue
            elif kind == 'ERROR':
                raise SyntaxError(r'bad token: {tk}')
            else:
                tokens.append(tk)
        
        return tokens

    def peek(self, tokens):
        if tokens:
            return tokens[0]
        return Token('<EOF>', 'EOF')

    def read(self, tokens):
        if tokens:
            return tokens.pop(0)
        return Token('<EOF>', 'EOF')

    def expect(self, value, tokens):
        tk = self.peek(tokens)
        if tk != value:
            raise SyntaxError(r'bad token: {tk}')
        return self.read(tokens)
        
    def parse(self, src):
        tokens = self.lex(src)
        return self.start(tokens)

    def start(self, tokens):
        """
        start  : (object | array) EOF
        """
        if self.peek(tokens) == '{':
            value = self.object(tokens)
        else:
            value = self.array(tokens) 
        
        if self.read(tokens).kind != "EOF":
            raise SyntaxError('expected EOF')
        return value

    def object(self, tokens):
        """
        object : "{" [pair ("," pair)*] "}"
        """
        self.expect("{", tokens)
        
        if self.peek(tokens) == "}":
            self.expect("}", tokens)
            return []

        pairs = [self.pair(tokens)]
        
        tk = self.read(tokens)
        while tk == ',':
            pairs.append(self.pair(tokens))
            tk = self.read(tokens)
        if tk != "}":
            raise SyntaxError(f'bad token: {tk}')
        
        return dict(pairs)

    def array(self, tokens):
        """
        array  : "[" [value ("," value)*] "]"
        """
        self.expect("[", tokens)
        
        if self.peek(tokens) == "]":
            self.expect("]", tokens)
            return []

        values = [self.value(tokens)]
        
        tk = self.read(tokens)
        while tk == ',':
            values.append(self.value(tokens))
            tk = self.read(tokens)
        if tk != "]":
            raise SyntaxError(f'bad token: {tk}')
        
        return values

    def pair(self, tokens):
        """
        pair   : STRING ":" value
        """
        tk = self.read(tokens)
        if tk.kind != "STRING":
            raise SyntaxError(f'bad token: {tk}')
        left = eval(tk)
        self.expect(":", tokens)
        right = self.value(tokens) 

        return (left, right)

    def value(self, tokens):
        """
        value  : object
            | array 
            | STRING
            | NUMBER
            | LITERAL
        """
        tk = self.peek(tokens)
        if tk == "{":
            return self.object(tokens)
        elif tk == "[":
            return self.array(tokens)
        
        tk = self.read(tokens)
        if tk.kind == "STRING":
            return eval(tk)
        elif tk.kind == "NUMBER":
            return float(tk)
        elif tk == "true":
            return True
        elif tk == "false":
            return False
        elif tk == "null":
            return None


def parse(src):
    parser = JsonParser()
    return parser.parse(src)

src = r"""
{
    "name": "Fábio",
    "age": 38,
    "langs": ["Python", "Js", "C"],
    "data": [
        [true, false, null],
        {"data": {}},
        [[]]
    ]
}
"""
print(parse(src))
