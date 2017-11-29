import random
import itertools

names, constraints;
curr_max = random.shuffle(names)

while(notMet(curr_max,constraints)):
    name1,name2 = random.sample(range(names.length),2);
    new_max = curr_max[:]
    new_max[name1],new_max[name2] = curr_max[name2],curr_max[name1]
    if(notMet(new_max)<notMet(curr_max)):
        curr_max = new_max

def notMet(names,constraints):
    total = 0
    for constraint in constraints:
        if(not satisfied(names,constraint)):
            total += 1
    return total
def satisfied(names, constraint):
    name1 = names.index(constraint[0])
    name2 = names.index(constraint[1])
    name3 = names.index(constraint[2])
    if((name1 < name3 and name2 < name3) or (name1>name3 and name2>name3)):
        return True
    return False
