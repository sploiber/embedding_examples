from minorminer import find_embedding
from dwave.system.samplers import DWaveSampler
from dimod import BinaryQuadraticModel
from dwave.embedding import embed_bqm, broken_chains, unembed_sampleset
import numpy as np

# Graph partitioning as full mesh
gamma = 3
linear = 3 - (3 * gamma)
quad = (2 * gamma) - 2

Q = {(0, 0): linear, (1, 1): linear, (2, 2): linear, (3, 3): linear, (0, 1): quad, (0, 2): quad, (0, 3): quad, (1, 2): quad, (1, 3): quad, (2, 3): quad}

chainstrength = 1.01
numruns = 100

dwave_sampler = DWaveSampler()
A = dwave_sampler.edgelist
Adj = dwave_sampler.adjacency
embedding = find_embedding(Q, A)
print(embedding)

bqm = BinaryQuadraticModel.from_qubo(Q)

# Cannot use a Composite to get the broken chains, so do the embedding
# directly
bqm_embedded = embed_bqm(bqm, embedding, Adj, chain_strength=chainstrength)
response = DWaveSampler().sample(bqm_embedded, num_reads=numruns)

# We need to get the chains directly, as a list
chains = [embedding[v] for v in list(bqm)]

# Obtain the broken chains
broken = broken_chains(response, chains)

# Interpret the results in terms of the embedding. Be sure to 
# tell the method to compute the chain_break_frequency.
print(unembed_sampleset(response, embedding, source_bqm=bqm, chain_break_fraction=True), broken)

# Use NumPy method to obtain the indices of the broken chains
w = np.where(broken == True)
indices = list(zip(*w))
print(indices)
