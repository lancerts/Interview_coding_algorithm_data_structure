#This script computes the strong connected components(SCC) of a given graph.
import sys
import time
import heapq
#import resource
from itertools import groupby
from collections import defaultdict
import threading







class Tracker(object):
    """Keeps track of the current time, current source, component leader,
    finish time of each node and the explored nodes.

    'self.leader' is informs of {node: leader, ...}."""

    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()
        self.ordered=[]



def dfs(graph_dict, node, tracker):
    """Inner loop explores all nodes in a SCC. Graph represented as a dict,
    {tail: [head_list], ...}. Depth first search runs recursively and keeps
    track of the parameters"""



    stack=[node]
    tracker.explored.add(node)
    tracker.leader[node] = tracker.current_source
    while len(stack) >0:
           node =stack.pop()
           stack.append(node)





#              tracker.finish_time[node] = tracker.current_time
#              tracker.current_time -= 1
           l1=len(stack)
           for head in graph_dict[node]:
               if head not in tracker.explored:
                    tracker.explored.add(head)
                    tracker.leader[head] = tracker.current_source
                    stack.append(head)
                    break

           l2=len(stack)
           if l2==l1:
               node =stack.pop()
               tracker.ordered.append(node)




def dfs_loop(graph_dict, nodes, tracker):
    """Outer loop checks out all SCCs. Current source node changes when one
    SCC inner loop finishes."""

    for node in nodes:
        if node not in tracker.explored:
            tracker.current_source = node
            dfs(graph_dict, node, tracker)



def graph_reverse(graph):
    """Given a directed graph in forms of {tail:[head_list], ...}, compute
    a reversed directed graph, in which every edge changes direction."""

    reversed_graph = defaultdict(list)
    for tail, head_list in graph.items():
        for head in head_list:
            reversed_graph[head].append(tail)
    return reversed_graph


def scc(graph):
    """First runs dfs_loop on reversed graph with nodes in decreasing order,
    then runs dfs_loop on original graph with nodes in decreasing finish
    time order(obtained from first run). Return a dict of {leader: SCC}."""

    out = defaultdict(list)
    tracker1 = Tracker()
    tracker2 = Tracker()

    nodes = set()
    reversed_graph = graph_reverse(graph)
    for tail, head_list in graph.items():
        nodes |= set(head_list)
        nodes.add(tail)



    nodes = sorted(list(nodes), reverse=True)



    dfs_loop(reversed_graph, nodes, tracker1)



    tracker1.ordered.reverse()
#    print tracker1.ordered

#    sorted_nodes = sorted(tracker1.finish_time,
#                          key=tracker1.finish_time.get, reverse=True)



    dfs_loop(graph,  tracker1.ordered, tracker2)
    for lead, vertex in groupby(sorted(tracker2.leader, key=tracker2.leader.get),
                                key=tracker2.leader.get):
        out[lead] = list(vertex)
    return out


def main():
    start = time.time()
    graph = defaultdict(list)

    #with open('scctest.txt') as file_in:
    with open('SCC.txt') as file_in:
        for line in file_in:
            x = line.strip().split()
            x1, x2 = int(x[0]), int(x[1])
            graph[x1].append(x2)

    t1 = time.time() - start
    print t1

    groups = scc(graph)
    t2 = time.time() - start
    print t2
    top_5 = heapq.nlargest(5, groups, key=lambda x: len(groups[x]))
    #sorted_groups = sorted(groups, key=lambda x: len(groups[x]), reverse=True)
    result = []
    for i in range(5):
        try:
            result.append(len(groups[top_5[i]]))
            #result.append(len(groups[sorted_groups[i]]))
        except:
            result.append(0)
    print result


if __name__ == '__main__':
    #set rescursion limit and stack size limit
    #sys.setrecursionlimit(10 ** 6)
    #resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
    #threading.stack_size(2**28-1)
    thread = threading.Thread(target = main)
    thread.start()
