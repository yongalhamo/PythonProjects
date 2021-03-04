def naive_search (arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            print (f'{target} found at location {i}')




def binary_search( arr, x):
    lowerBound = 0
    upperBound = len(arr)-1
    found = False

    while not found :
        if upperBound < lowerBound:
            print (f'{x} does not exist!')
            exit()

        midPoint = (lowerBound + (upperBound - lowerBound)// 2)

        if arr[midPoint]==x :
            print (f'{x} found at location {midPoint}')
            found = True

        elif arr[midPoint] < x:
            lowerBound = midPoint +1

        elif arr[midPoint] > x:
            upperBound = midPoint - 1





if __name__=='__main__':

    import random
    import time

    i =1
    arr = []
    while i <1000:
        arr.append(random.randint(1,5000))
        i+=1
    sorted_arr = sorted(arr)
    print(sorted_arr)

    start = time.time()
    for target in sorted_arr:
        naive_search(sorted_arr, target)
    end = time.time()
    Naive = (end - start)

    start = time.time()
    for target in sorted_arr:
        binary_search(sorted_arr, target)
    end = time.time()
    Binary = (end - start)

    print (f'Naive search time : {Naive}')
    print (f'Binary search time : {Binary}')





