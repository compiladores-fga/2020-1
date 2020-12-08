#===================================
# Autômato Não-Determinístico Finito
#===================================

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
    ("A", "0"): {"B", "C"},
    ("B", "1"): {"C"},
    ("C", "0"): {"B"},
}


def automaton(δ, q0, F, input_string):
    states = {q0}
    
    for c in input_string:
        old = states
        states = set()
        for state in old:
            new_states = δ.get((state, c), set())
            states.update(new_states)

        print(f"{c}: {old} -> {states}")

    return bool(states.intersection(F))


st = input("Entrada: ")
print(automaton(δ, q0, F, st))