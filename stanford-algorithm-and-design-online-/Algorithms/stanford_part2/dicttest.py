#This script computes the strong connected components(SCC) of a given graph.
import sys
import time
import heapq
#import resource
from itertools import groupby
from collections import defaultdict
import threading

def main1():
    start = time.time()
    graph = defaultdict(list)
    
    #with open('scctest.txt') as file_in:
    with open('SCC.txt') as file_in:
        for line in file_in:
            x = line.strip().split()
            x1, x2 = int(x[0]), int(x[1])
            graph[x1].append(x2)
            
    
    print time.time() - start
    graph
    print time.time() - start
    
def main2():
    start = time.time()
    
    graph2={}
    #with open('scctest.txt') as file_in:
    with open('SCC.txt') as file_in:
        for line in file_in:
            x = line.strip().split()
            x1, x2 = int(x[0]), int(x[1])
            
            graph2[x1]=x2
            
    print time.time() - start
    graph2
    print time.time() - start
    
if __name__ == '__main__':
    #set rescursion limit and stack size limit
    sys.setrecursionlimit(10 ** 6)
    #resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
    threading.stack_size(2**28-1)
    thread = threading.Thread(target = main2)
    thread.start()