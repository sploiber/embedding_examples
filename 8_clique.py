from minorminer import find_embedding
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import FixedEmbeddingComposite

# Graph partitioning as full mesh
gamma = 3
N = 8
linear = N - 1 - (7 * gamma)
quad = (2 * gamma) - 2

Q = {}
for i in range(N):
    Q[i, i] = linear
    for j in range(i + 1, N):
        Q[i, j] = quad

chainstrength = 5
numruns = 100

dwave_sampler = DWaveSampler()
A = dwave_sampler.edgelist
embedding = find_embedding(Q, A)
print(embedding)
