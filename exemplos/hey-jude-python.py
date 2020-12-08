import random 


def T(st):
    def result():
        return st
    return result

WS = T(" ")
NL = T("\n")


grammar = {
    "start": [
        [T("HEY JUDE"), NL, NL, "heyjude"],
    ],

    "heyjude": [
        [T("hey jude "), "dont", "rememberto", "then", "better", "end"],
    ],

    "end": [
        ["nanana"],
        ["nanana", "heyjude"],
    ],

    "dont": [
        [T("don't"), WS, "dontthing", NL],
    ],

    "dontthing": [ 
        [T("make it bad,\ntake a sad song and make it better")],
        [T("be afraid,\nyou were made to go out and get her")],
        [T("let me down,\nyou have found her, now go and get her"  )],
    ],

    "rememberto": [
        [T("remember to"), WS, "rememberwhat", NL],
    ],
        
    "rememberwhat": [
        [T("let her into your heart")],
        [T("let her under your skin")],
    ],

    "then": [
        [T("then you"), WS, "thenwhat", WS, T("to make it better"), NL],
    ],

    "thenwhat": [
        [T("can start")], 
        [T("begin")],
    ],

    "better": [
        ["starstbetter", T("waaaaa"), NL],
    ],

    "starstbetter": [
        [T("better"), WS],
        [T("better"), WS, "starstbetter"],
    ],

    "nanana": [
        ["startnanana", T("na-na-na-na"), NL, NL],
    ],

    "startnanana": [
        [T("na"), WS],
        [T("na"), WS, "startnanana"],
    ]
}

            
def generate(rule):
    alternatives = grammar[rule]
    symbols = random.choice(alternatives)
    tokens = []

    for symbol in symbols:
        if callable(symbol):
            value = symbol()
            tokens.append(value)
        else:
            list_of_tokens = generate(symbol)
            tokens.extend(list_of_tokens)

    return tokens

print(''.join(generate("start")))
