import time

def function(value):
    #start checking execution time
    start = time.time()

    sum = 0
    for i in range(value + 1):
        sum += i
    print(sum)

    #sto checking execution time
    end = time.time()
    print(end - start)

function(500)
