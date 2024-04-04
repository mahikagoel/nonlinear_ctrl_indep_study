# CLASS TO DETERMINE IF SYSTEM IS INPUT STATE LINEARIZABLE
import sympy as sym

class FeedbackLinearization:

    def __init__(self, f, g, n, state):
        self.f = f # f dynamics matrix
        self.g = g # g input matrix
        self.n = n # number of states
        self.states = state
        self.vfield = sym.Matrix.zeros(n, n)
        pass

    def liebracket(self, f_v, g_v, i):

        if i == 0:
            return g_v
        elif i == 1:
            return g_v.jacobian(self.states) @ f_v - f_v.jacobian(self.states) @ g_v
        else:
            bracket = self.liebracket(f_v, g_v, i-1)
            return self.liebracket(f_v, bracket, 1)

    def vector_field(self):
        for i in range(self.n):
            lb = self.liebracket(self.f, self.g, i)
            self.vfield[:, i] = lb
        return self.vfield

    def input_state_linearizable_check(self):
        controllability_bool = False
        involutive_bool = False

        # print(self.vector_field())

        vfield = sym.Matrix(self.vfield)
        rank = vfield.rank()

        if (rank == self.n):
            controllability_bool = True

        # return controllability_bool and involutive_bool
        return controllability_bool
    



