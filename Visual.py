from cProfile import label
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
import tkinter as tk
dfa = DFA(
    states={"q0", "q1", "q2", "q3", "q4"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": "q3", "1": "q1"},
        "q1": {"0": "q3", "1": "q2"},
        "q2": {"0": "q3", "1": "q2"},
        "q3": {"0": "q4", "1": "q1"},
        "q4": {"0": "q4", "1": "q1"},
    },
    initial_state="q0",
    final_states={"q2", "q4"},
)
dfa = VisualDFA(dfa)
print(dfa.table)
dfa.show_diagram()


new_dfa = VisualDFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)
new_dfa = VisualDFA(new_dfa)
minimal_dfa = VisualDFA.minify(new_dfa)
minimal_dfa.show_diagram()
print (new_dfa.input_check("1001"))
new_dfa.show_diagram(view=True)
new_dfa.mostrar_diagrama ( "1001" )
