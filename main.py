import random


def create_chromosomes(length):     #randomly creating chromosomes
    c=''
    for i in range(length):
        c=c+alpha[random.randint(0,51)]
    return c

def fitness(a,b):       #Calculating fitness
    fit=0
    for i in range(len(a)):
        if(a[i]!=b[i]):
            fit+=1

    return fit

def crossover(a,b):     #random cross over point chosen
    length=len(a)
    random_split=random.randint(1,length//2)
    random_val=random.randint(0,2)
    if(random_val==0):
        c=b[0:random_split]+a[random_split:]
    else:
        c = a[0:random_split] + b[random_split:]
    return c

def selection(og,c1,c2,c3,c4):      #Used to find the values with least fitness score
    fitness1 = fitness(og, c1)
    fitness2 = fitness(og, c2)
    fitness3 = fitness(og, c3)
    fitness4 = fitness(og, c4)
    rank = [fitness1, fitness2, fitness3, fitness4]
    # print(rank)
    min1=rank.index(min(rank))
    rank[min1]=999999999
    min2=rank.index(min(rank))

    return min1,min2

def mutation(c1):
    value = random.random()
    c=''
    for i in range(len(c1)):
        value = random.random()
        if value > 0.90:
            c=c+alpha[random.randint(0,51)]
        else:
            c=c+c1[i]

    return c


if __name__=="__main__":
    alpha='Aa Bb cC dD eE fF gG hH iI jJ kK lL mM nN oO pP qQ rR sS tT uU vV wW xX yY zZ 1 2 3 4 5 6 7 8 9 0 . , - ; : ( ) * & ^ % $ # @ ! < > [ ] { } | / ? _ + ='
    a=input('Enter word to match: ')
    print('')
    length=len(a)
    c1 = create_chromosomes(length)
    c2 = create_chromosomes(length)
    c3 = create_chromosomes(length)
    c4 = create_chromosomes(length)

    # print('Initial values: ',c1,c2,c3,c4)

    i=1
    while(c1!=a):



        max1,max2=selection(a,c1,c2,c3,c4)


        if(max1==0):
            c1 = crossover(a, c1)
        elif (max1 == 1):
            c1 = crossover(a, c2)
        elif (max1 == 2):
            c1 = crossover(a, c3)
        elif (max1 == 3):
            c1 = crossover(a, c4)

        if (max2 == 0):
            c2 = crossover(a, c1)
        elif (max2 == 1):
            c2 = crossover(a, c2)
        elif (max2 == 2):
            c2 = crossover(a, c3)
        elif (max2 == 3):
            c2 = crossover(a, c4)

        # print(fitness(a, c1))
        # print(c1+" || || "+c2)

        c1 = mutation(c1)
        c2 = mutation(c2)
        c3 = mutation(c3)
        c4 = mutation(c4)


        print(f"Generation {i}: {c1}")

        i+=1





