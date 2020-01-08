from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Set up the QUBO. Start with the equations from the slides:
# x + y - 2xy -1
# 2yz - y - z
# -2zx + z + x - 1
# QUBO: 2x - 2xy + 2yz - 2zx - 2

chainstrength = 5
numruns = 100
Q = {(0, 0): 2, (0, 1): -2, (0, 2): -2, (1, 2): 2}

response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, chain_strength=chainstrength, num_reads=numruns)

for smpl, energy in response.data(['sample', 'energy']):
    print(smpl, energy)
