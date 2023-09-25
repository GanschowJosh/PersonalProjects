from itertools import permutations
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
eq = input()
evaluation = eval(eq)
#bracketCount = eq.count("(") + eq.count(")")
bracketIndices = find(eq, "(")
bracketIndices2 = (find(eq, ")"))
bracketIndices = bracketIndices+bracketIndices2
bracketIndices = list(permutations(bracketIndices)) + list(powerset(bracketIndices))
#print (bracketIndices)

for ind in bracketIndices:
    try:
        print(eval(eq[:ind]+eq[ind+1:]))
        print("here")
    except:
        continue
    print(eq[:ind]+eq[ind+1:])
