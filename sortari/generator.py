import random
import time
import BubbleSort
import BucketSort
import CountSort
import MergeSort
import QuickSort

def generateBigArray():
    length = random.randint(10, 1000000)
    array = list()
    for i in range(1, length):
        bigNumber = random.randint(10, 1000000)
        array.append(bigNumber)
    return array

bigList = generateBigArray()

start = time.time()
# bigList = BubbleSort.bubbleSort(bigList, len(bigList)) am stat 10 minute si inca nu s-a terminat de sortat
# bigList = BucketSort.bucketSort(bigList)
# bigList = MergeSort.mergeSort(bigList, 0, len(bigList) - 1)
# bigList = QuickSort.quickSort(bigList, 0, len(bigList) - 1)
# bigList = bigList.sort()
print("L-am sortat in %s", (time.time() - start))

# PANA LA 100 DE MII:
"""
attempt-uri bucketSort:
attempt 1: 0.5565476417541504
attempt 2: 0.891913652420044
attempt 3: 0.8103981018066406
attempt 4: 0.20159316062927246
"""

"""
attempt-uri mergeSort:
attempt 1: 0.36303114891052246
attempt 2: 0.2214961051940918
attempt 3: 0.37706828117370605
attempt 4: 0.2001171112060547
"""

"""
attempt-uri quickSort: 
attempt 1: 0.1356372833251953
attempt 2: 0.02094244956970215
attempt 3: 0.2762632369995117
attempt 4: 0.07380223274230957
"""

"""
attempt-uri sortul din Python:
attempt 1: 0.019944429397583008
attempt 2: 0.005984067916870117
attempt 3: 0.004987001419067383
attempt 4: 0.018949270248413086
"""

# PANA LA 10^6
"""
attempt-uri bucketSort:
attempt 1: 37.51306509971619
attempt 2: 2.699028491973877
attempt 3: 0.9694392681121826
attempt 4: 13.899415731430054
"""

"""
attempt-uri mergeSort:
attempt 1: 3.648078680038452
attempt 2: 2.9080657958984375
attempt 3: 1.4156458377838135
attempt 4: 3.3185298442840576
"""

"""
attempt-uri quickSort: 
attempt 1: 1.4552581310272217
attempt 2: 1.4182891845703125
attempt 3: 0.05485272407531738
attempt 4: 2.5264956951141357
"""

"""
attempt-uri sortul din python:
attempt 1: 0.060823678970336914
attempt 2: 0.2562737464904785
attempt 3: 0.21833372116088867
attempt 4: 0.26598453521728516
"""
