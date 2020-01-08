import dimod

# use the exact solver to find energies for all states. This is only
# realistic for very small problems.
exactsolver = dimod.ExactSolver()

# Set up the QUBO. Start with the equations from the slides. These have the
# embedding explicitly expressed, with a variable for chainstrength.
chainstrength = 3

# -1 + q_0 + q_4 - 2 q_0 q_4
# 2 q_1 q_4 - q_4 - 0.5 (q_1 + q_5)
# -1 + q_0 + 0.5 (q_1 + q_5) - 2 q_0 q_5
# c (-1 + q_1 + q_5 - 2q_1 q_5)

Q = {(0, 0): 2, (1, 1): chainstrength, (5, 5): chainstrength, (0, 4): -2, (1, 4): 2, (0, 5): -2, (1, 5): -2 * chainstrength}

# There's no need for a constant, so we can use exactsolver directly.
results = exactsolver.sample_qubo(Q)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
