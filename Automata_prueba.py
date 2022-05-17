from cgitb import text
import tkinter
from anyio import open_file
from automata.fa.dfa import DFA
from isort import file
from sympy import false
from visual_automata.fa.dfa import VisualDFA
from tkinter import *
dfa=DFA(
states={"q0","q1","q2","q3","q4"},
input_symbols = {"a","b"},
transitions={
"q0":{"a":"q1","b":"q4"},
"q1":{"b":"q2","a":"q4"},
"q2":{"a":"q1","b":"q3"},
"q3":{"a":"q1","b":"q4"},
"q4":{"a":"q1","b":"q4"}
},
initial_state="q0",
final_states={"q1"}
)
root = Tk()  
root.geometry("550x750") 
dfa = VisualDFA(dfa)
dfa.show_diagram()
dfa.show_diagram(view=True)
palabra = input("ingrese palabra:")
print(dfa.input_check(palabra))

root.mainloop() 
