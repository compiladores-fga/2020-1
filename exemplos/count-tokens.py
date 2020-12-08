import sys
import tokenize


path = sys.argv[-1]
n = len(list(tokenize.generate_tokens(open(path).readline)))
print(f"O arquivo {path} possui {n} tokens!")