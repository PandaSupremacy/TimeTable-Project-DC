import time
from initialization import *
from fitness import *
from crossover import *

st = time.time()
generations = 2
gnc = 1
while generations!=0:
    generations -= 1
    # Will make new child population 
    childrenpop = []
    childFit_value = []

    temppop = pop.copy()
    while temppop!=[]:
        childrens = crossoverIW(temppop)
        if childrens!=[]:
            o1,o2 = childrens[0],childrens[1]
            childrenpop.append(o1)
            childFit_value.append(fitnessFunction(o1))
            childrenpop.append(o2)
            childFit_value.append(fitnessFunction(o2))


    pop += childrenpop
    Fit_values += childFit_value
    spop = [val for (_, val) in sorted(zip(Fit_values, pop), key=lambda x: x[0],reverse=True)]
    pop = spop.copy()
    pop = pop[:popz]
    Fit_values.clear()
    for i in pop:
        Fit_values.append(fitnessFunction(i))
    

    print("Generation ",gnc)
    gnc+=1
    # import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)



                 
    

et = time.time()
print("time : ",et-st)
print("Max fitness achived : ",max(Fit_values))

y1 , y2 , y3 , y4 = separateChromosome(pop[0])
print("\n\n\n\nFirst year\n")
for k , v in y1.items():
    print(k,v)
print("\nSecond year\n")
for k , v in y2.items():
    print(k,v)
print("\nthird year\n")
for k , v in y3.items():
    print(k,v)
print("\nfourth year\n")
for k , v in y4.items():
    print(k,v)
print(fitnessFunction(pop[0]))
