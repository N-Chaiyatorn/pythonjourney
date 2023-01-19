import random

gr_list = ["GR", "RRR", "RR", "R", "C"]

for gr in range(1):
    gr_list.append("GR")

for rrr in range(10):
    gr_list.append("RRR")

for rr in range(20):
    gr_list.append("RR")

for r in range(28):
    gr_list.append("R")

for c in range(40):
    gr_list.append("C")


random.sample(gr_list, k=10)


