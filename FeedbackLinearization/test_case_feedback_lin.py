import sympy as sym
from feedback_linearization import FeedbackLinearization

x1, x2, x3, x4 = sym.symbols('x1, x2, x3, x4')
k, I, J, M, g, L = sym.symbols('k, I, J, M, g, L')

f = sym.Matrix([x2, -(M*g*L/I)*sym.sin(x1) - (k/I)*(x1-x3), x4, (k/J)*(x1-x3)])

g = sym.Matrix([0, 0, 0, 1/J])

states = sym.Matrix([x1, x2, x3, x4])

n = 4

input_linearizer = FeedbackLinearization(f, g, n, states)
# lie_bracket = input_linearizer.liebracket(1)
# print(lie_bracket)

linearizable_bool = input_linearizer.input_state_linearizable_check()
print(linearizable_bool)

# see Slotine Pg. 239 for double checking of vector fields & controllability result


