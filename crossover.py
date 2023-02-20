from initialization import*
from fitness import *
from math import *
# Crossover 
# Define the crossover probability
crossProb = 0.8
# Define mutation probablity
mutateProb = 0

Fit_values = []
for chromosome in pop:
    Fit_values.append(fitnessFunction(chromosome))
# We use random or non-random multipoint crossover here 
# Random multipoint : two parents are chosen to crossover by roullete wheel selection , then a random value N (no. of points 
# of crossover) ranging from 1 to 119 is chosen. Following which the multipoint crossover is done. 

# Non-Random multipoint : We can fix the no. of points of crossover to suitable value


def crossoverIW(pop):

    # assume the population is a list of individuals with corresponding fitness values
    population = [(indiv, fitness) for indiv, fitness in zip(pop, Fit_values)]

    # select the first parent
    parent1 = random.choice(population)[0]
    # select the second parent
    while True:
        parent2 = random.choice(population)[0]
        if parent2 != parent1:
            break
        
    pop.remove(parent1)
    pop.remove(parent2)

    parent1 = weektosubs(parent1)
    parent2 = weektosubs(parent2)


    # Check if crossover should be performed
    if random.random() <= crossProb:
    # Perform crossover
    # N Multipoint crossover 
        N = 10
        cpoints = sorted(random.sample(range(1, 120), N-1))

        # Add the endpoints of the chromosome to the list of crossover points
        cpoints = [0] + cpoints + [120]
        
        # Extract segments from parents and create offspring
        offspring1 = []
        offspring2 = []
        for i in range(len(cpoints)-1):
            if i % 2 == 0:
                seg_length = cpoints[i+1] - cpoints[i]
                if len(offspring1) + seg_length <= 120:
                    offspring1 += parent1[cpoints[i]:cpoints[i+1]]
                else:
                    offspring1 += parent1[cpoints[i]:cpoints[i]+(120-len(offspring1))]
                seg_length = cpoints[i+1] - cpoints[i]
                if len(offspring2) + seg_length <= 120:
                    offspring2 += parent2[cpoints[i]:cpoints[i+1]]
                else:
                    offspring2 += parent2[cpoints[i]:cpoints[i]+(120-len(offspring2))]
            else:
                seg_length = cpoints[i+1] - cpoints[i]
                if len(offspring1) + seg_length <= 120:
                    offspring1 += parent2[cpoints[i]:cpoints[i+1]]
                else:
                    offspring1 += parent2[cpoints[i]:cpoints[i]+(120-len(offspring1))]
                seg_length = cpoints[i+1] - cpoints[i]
                if len(offspring2) + seg_length <= 120:
                    offspring2 += parent1[cpoints[i]:cpoints[i+1]]
                else:
                    offspring2 += parent1[cpoints[i]:cpoints[i]+(120-len(offspring2))]
               
        offspring1 = substoweek(offspring1)
        offspring2 = substoweek(offspring2)
        parent1 = substoweek(parent1)
        parent2 = substoweek(parent2)

        offspring1 , offspring2 = fix(offspring1,offspring2,parent1,parent2)

        return [offspring1,offspring2]
    
    else:
        return []

#---------------------------#--------------------------------------------#    

def crossoverSW(pop):

    # assume the population is a list of individuals with corresponding fitness values
    population = [(indiv, fitness) for indiv, fitness in zip(pop, Fit_values)]

    # select the first parent
    parent1 = random.choice(population)[0]
    # select the second parent
    parent2 = random.choice(population)[0]

    if parent1==parent2:
        pop.remove(parent1)
    else:
        pop.remove(parent1)
        pop.remove(parent2)

    parent1 = weektoslots(parent1)
    parent2 = weektoslots(parent2)

    # Check if crossover should be performed
    if random.random() <= crossProb:
        N = 5
        cpoints = sorted(random.sample(range(1, 30), N-1))

        # Add the endpoints of the chromosome to the list of crossover points
        cpoints = [0] + cpoints + [30]
        
        # Extract segments from parents and create offspring
        offspring1 = []
        offspring2 = []

        for i in range(0,len(cpoints)-1):
            if (i%2)==0:
                for j in range(cpoints[i],cpoints[i+1]):
                    offspring1.append(parent1[j])
            else:
                for j in range(cpoints[i],cpoints[i+1]):
                    offspring1.append(parent2[j])

        for i in range(0,len(cpoints)-1):
            if (i%2)==0:
                for j in range(cpoints[i],cpoints[i+1]):
                    offspring2.append(parent2[j])
            else:
                for j in range(cpoints[i],cpoints[i+1]):
                    offspring2.append(parent1[j])

        offspring1 = slotstoweek(offspring1)
        offspring2 = slotstoweek(offspring2)

        return [offspring1,offspring2]
    else:
        return []

#-------------------------------#-----------------------------------------#

def uniformCrossover(pop):
    # assume the population is a list of individuals with corresponding fitness values
    population = [(indiv, fitness) for indiv, fitness in zip(pop, Fit_values)]

    # select the first parent
    parent1 = random.choice(population)[0]
    # select the second parent
    while True:
        parent2 = random.choice(population)[0]
        if parent2 != parent1:
            break
        
    pop.remove(parent1)
    pop.remove(parent2)

    parent1 = weektosubs(parent1)
    parent2 = weektosubs(parent2)

    crossProb = 0.8

    # Check if crossover should be performed
    if random.random() <= crossProb:
        offspring1 = []
        offspring2 = []

        for i in range(120):
            rn = random.random()
            if rn<=0.5:
                offspring1.append(parent1[i])
                offspring2.append(parent2[i])
            else:
                offspring1.append(parent2[i])
                offspring2.append(parent1[i])

        offspring1 = substoweek(offspring1)
        offspring2 = substoweek(offspring2)

        fix(offspring1, offspring2, parent1,parent2)
        return [offspring1,offspring2]
        # rn = random.random()
        # if rn<=mutateProb:
        #     return mutationDay(offspring1,offspring2) 
        # else:
        #     return [offspring1,offspring2]
    
    else:
        return []




#----------------------------------------------------------------#

# Mutation 

def mutationSlot(chromosome1,chromosome2):

    chromosome1 = weektoslots(chromosome1)
    chromosome2 = weektoslots(chromosome2)
    n = len(chromosome1)

    rn1 = random.randint(0,n-1)
    rn2 = random.randint(0,n-1)
    while rn1==rn2:
        rn2 = random.randint(0,n-1)
    chromosome1[rn1],chromosome1[rn2] = chromosome1[rn2],chromosome1[rn1]

    rn1 = random.randint(0,n-1)
    rn2 = random.randint(0,n-1)
    while rn1==rn2:
        rn2 = random.randint(0,n-1)
    chromosome2[rn1],chromosome2[rn2] = chromosome2[rn2],chromosome2[rn1]

    return [slotstoweek(chromosome1),slotstoweek(chromosome2)]

#---------------------------------------------------#
def mutationDay(chromosome1,chromosome2):
    n = len(chromosome1)

    rn1 = random.randint(0,n//2)
    rn2 = random.randint(n//2,n-1)
    chromosome1[rn1],chromosome1[rn2] = chromosome1[rn2],chromosome1[rn1]

    rn1 = random.randint(0,n//2)
    rn2 = random.randint(n//2,n-1)
    chromosome2[rn1],chromosome2[rn2] = chromosome2[rn2],chromosome2[rn1]

    return [chromosome1,chromosome2]


def fix(child1,child2,parent1,parent2):

    courseCredStore = dict(zip(cp['Course_Code'], cp['NOCW']))
    #print(courseCred, "\n\n\n\nMAin")
    def remaining(chromosome,coursecred):
        print(coursecred)
        for day in chromosome:
            for slot in day:
                for sub in slot:
                    if sub!='' and sub in coursecred:
                        coursecred[sub]-=1
                        if coursecred[sub] == 0:
                            print(sub,coursecred[sub])
                            del coursecred[sub]
                    elif sub!='' and sub not in coursecred:
                        slot[slot.index(sub)] = ''
        return chromosome,coursecred
    
    def change(chromosome):

        chromosome , courseCred = remaining(chromosome,courseCredStore)

        missing_class_batch = {1:[],2:[], 3:[], 4:[]}
        for sub in courseCred.keys():
            missing_class_batch[subject_batch_ind_dict[sub]//2].append(sub)
        
        missing_slot = {1:[],2:[],3:[],4:[]}
        chromosome = weektoslots(chromosome)
        for slotNo , slot in enumerate(chromosome):
            for i, sub in enumerate(slot):
                if not sub:
                    missing_slot[i+1].append(slotNo)           

        chromosome = slotstoweek(chromosome)
        
        for i , slots in missing_slot.items():
            while missing_class_batch[i]:
                if not slots:
                    break
                j = random.choice(slots)
                missing_slot[i].remove(j)
                day = ceil(j/6)
                slot = j%6
                if slot == 0:
                    slot = 6
                
                
                if parent1[day-1][slot-1][i-1] in missing_class_batch[i]:
                    sub = parent1[day-1][slot-1][i-1] 
                    courseCred[sub]-=1                
                    if courseCred[sub] == 0:
                        missing_class_batch[i].remove(sub)
                    chromosome[day-1][slot-1][i-1] = sub
                
                elif parent2[day-1][slot-1][i-1] in missing_class_batch[i]:
                    
                    sub = parent2[day-1][slot-1][i-1] 
                    courseCred[sub]-=1                
                    if courseCred[sub] == 0:
                        missing_class_batch[i].remove(sub)
                    chromosome[day-1][slot-1][i-1] = sub
        
        return chromosome

    child1  = change(child1)
    child2 = change(child2)
    print(f"\n\n{parent1}\n\n{parent2}\n\n{child1}\n\n{child2}")

    return child1, child2

    
    
    # Create a dictionary of missing classes for each batch
    
    
        # if subject_batch_ind_dict[sub] not in missing_class_batch:
        #     missing_class_batch[subject_batch_ind_dict[sub]] = [sub]
        # else:
        #     missing_class_batch[subject_batch_ind_dict[sub]].append(sub)
    

    # Storing empty slots of each batch
    
        
        
            


    # # Assign missing classes to empty slots
    # for day in chromosome:
    #     for slot in day:
    #         for i, sub in enumerate(slot):
    #             if not sub:
    #                 if ((i*2)+2) in missing_class_batch:
    #                     sb = random.choice(missing_class_batch[(i*2)+2])
    #                     slot[i] = sb
    #                     courseCred[sb] -= 1
    #                     if courseCred[sb] == 0:
    #                         del courseCred[sb]
    #                         missing_class_batch[((i*2)+2)].remove(sb)
    #                         if not missing_class_batch[(i*2)+2]:
    #                             del missing_class_batch[(i*2)+2]