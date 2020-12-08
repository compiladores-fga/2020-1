#===============================
# Autômato Determinístico Finito
#===============================

# Conjunto de estados válidos
Q = {"A", "B", "C", "e"}

# Alfabeto de entrada
Σ = {"0", "1"}

# Estado inicial
q0 = "A"

# Conjunto de estados finais
F = {"B", "C"}

# Tabela de transição
δ = {
    ("A", "0"): "B",
    ("B", "1"): "C",
    ("C", "0"): "B",
}


def automaton(δ, q0, F, input_string):
    state = q0
    
    for c in input_string:
        old = state
        try:
            state = δ[state, c]
        except KeyError:
            state = None
        print(f"{c}: {old} -> {state}")

    return state in F

st = input("Entrada: ")
print(automaton(δ, q0, F, st))