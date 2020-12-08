from lark import Lark

# Instale o hypothesis com 
#   python3 -m pip install hypothesis --user
from hypothesis.extra.lark import from_lark

# GRAMÁTICA LIVRE DE CONTEXTO
#  - Inclui símbolos terminais (tokens) e não-terminais
#  - Símbolos não-terminais representam padrões 
#    formados a partir de sequências de outros símbolos.
#  - Símbolos não-terminais são compostos por alternativas 
#    de sequências de símbolos.

grammar = Lark(r"""
start   : "HEY JUDE" NL NL heyjude

heyjude : "hey jude " dont rememberto then better end

end     : nanana
        | nanana heyjude

dont        : "don't" WS dontthing NL
dontthing   : "make it bad,\ntake a sad song and make it better"
            | "be afraid,\nyou were made to go out and get her"
            | "let me down,\nyou have found her, now go and get her"  

rememberto  : "remember to" WS rememberwhat NL
rememberwhat: "let her into your heart"
            | "let her under your skin"      

then        : "then you" WS thenwhat WS "to make it better" NL
thenwhat    : "can start" 
            | "begin"

better      : starstbetter "waaaaa" NL

starstbetter: "better" WS
            | "better" WS starstbetter

nanana      : beginnanana "na-na-na-na" NL NL

startnanana : "na" WS
            | "na" WS startnanana
            
WS : " "
NL : "\n"
""")


generator = from_lark(grammar)

ex = generator.example()

print()
print("=" * 50)
print(ex)