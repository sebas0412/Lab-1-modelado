from CongruentialGenerator import CongruentialGenerator
import random

randomInit = random.randint(10000000,11000000)
cg = CongruentialGenerator(0,0,0)
a,b,m = cg.good_abm(randomInit)
seed = cg.seed(cg.generateTime())
generated = cg.buildGenerator(a,b,m,seed)
print(m)
print(len(generated))