from minorminer import find_embedding
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import FixedEmbeddingComposite

# Graph partitioning as full mesh
gamma = 3
linear = 3 - (3 * gamma)
quad = (2 * gamma) - 2

Q = {(0, 0): linear, (1, 1): linear, (2, 2): linear, (3, 3): linear, (0, 1): quad, (0, 2): quad, (0, 3): quad, (1, 2): quad, (1, 3): quad, (2, 3): quad}

chainstrength = 5
numruns = 100

dwave_sampler = DWaveSampler()
A = dwave_sampler.edgelist
embedding = find_embedding(Q, A)
print(embedding)
