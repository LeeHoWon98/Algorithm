import sys

n = int(sys.stdin.readline())

for i in range(n):
    weeping = list(sys.stdin.readline().rstrip().split())
    
    while True:
        animal_weep = sys.stdin.readline().rstrip()
        if animal_weep == 'what does the fox say?':
            break
        else:
            animal_weep = animal_weep.split()
            while animal_weep[2] in weeping:
                weeping.remove(animal_weep[2])

    print(" ".join(weeping))