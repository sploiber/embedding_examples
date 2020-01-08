import minorminer

# Explore minorminer on a graph problem, without worrying about the
# physical lattice.

# Minorminer: embed a graph minor onto a target graph
# Embed a triangle onto a hexagon
Source = [(0, 1), (0, 2), (1, 2)]
Target = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)]

# Instantiate a miner for Source and Target
E1 = minorminer.miner(Source, Target)

# First, obtain embeddings without any restrictions. Note that there are
# many solutions. There could be one chain of length 3, with one of length
# 2 and one of length 1 (for example); there could be three chains of length
# 2, etc.
for i in range(10):
    print(E1.find_embedding())

print("")

# Now try fixed_chains. These are not allowed to change. For this example,
# we expect them to always be one of the solution nodes. In this case, we
# expect the 1st node to be this chain.
chain_set = {1: [1, 2]}
E2 = minorminer.miner(Source, Target, fixed_chains=chain_set)
for i in range(10):
    print(E2.find_embedding())

print("")

# Now try restrict_chains. These are not allowed to change, in a sense.
# A subset of the restricted chain must be that particular node.
# So we expect that node 1 will be one of [1], [2], or [1, 2].
chain_set = {1: [1, 2]}
E3 = minorminer.miner(Source, Target, restrict_chains=chain_set)
for i in range(10):
    print(E3.find_embedding())
