import sys
import tokenize

KEYWORDS = {
    "função": "def",
    "retorna": "return",
    "se": "if",
    "senão": "else",
    "sesenão": "elif",
    "classe": "class",
    "e": "and",
    "ou": "or",
    # ...
}
FUNCTIONS = {
    "entrada": input,
    "imprime": print,
    # ...
}


def run(path):
    fd = open(path)
    py_toks = []
    for tok in tokenize.generate_tokens(fd.readline):
        kind, string, *_ = tok
        if kind == tokenize.NAME:
            string = KEYWORDS.get(string, string)
        py_toks.append((kind, string))

    py_src = tokenize.untokenize(py_toks)
    exec(py_src, FUNCTIONS)


if __name__ == '__main__':
    run(sys.argv[-1])