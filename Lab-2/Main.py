from CongruentialGenerator import CongruentialGenerator

cg = CongruentialGenerator()
a, b, m = cg.good_abm(10000000)
czx = cg.get_period(a, b, m, 12351)
print(czx)
print(len(czx))
