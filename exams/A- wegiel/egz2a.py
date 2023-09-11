from egz2atesty import runtests
from collections import deque
from math import log2,ceil

# akceptowalna złożoność 
def coal( A, T ):
    n = len(A)
    M = [T for _ in range(n)]
    inx = None
    for i in range(n):
        for j in range(n):
            if M[j] - A[i] >= 0:
                M[j] -= A[i]
                inx = j
                break
    return inx

#wzorcowa złożoność
class Node:
    def __init__(self):
        self.level=0
        self.parents=None
        self.left=None
        self.right=None
        self.max=None
        self.id=None #tylko dla lisci
        self.actuall_coal=0 #tylko dla lisci

def create_tree(A,T): #O(n)
    n=len(A) #liczba lisci
    number_of_all_nodes=2**(ceil(log2(n))+1)-1
    number_of_level_end=ceil(log2(n))
    number_of_act_nodes=1
    root=Node()
    root.max=T
    Q=deque()
    Q.append(root)
    while number_of_act_nodes!=number_of_all_nodes: #O(2*n)
        father=Q.popleft()
        left_son=Node()
        left_son.parents=father
        left_son.level=left_son.parents.level+1
        left_son.max=T
        right_son=Node()
        right_son.parents=father
        right_son.level=right_son.parents.level+1
        right_son.max=T
        father.left=left_son
        father.right=right_son
        Q.append(left_son)
        Q.append(right_son)
        number_of_act_nodes+=2
    Q.clear()
    Q.append(root)
    act_id=0
    while len(Q)>0: #O(2*n)
        v=Q.popleft()
        if v.level==number_of_level_end: #mam do czynienia z moimi koncowymi lisciami
            v.id=act_id
            act_id+=1
        if v.left!=None:
            Q.append(v.left)
        if v.right!=None:
            Q.append(v.right)
    return root

def search_in_tree(root,elements): #funkcja aktualizuje stan jednego z magazynow o konkretna dostawe wegla O(logn) bo jest to drzewo binarne czyli h=logn
    node=root
    while node!=None:
        if node.left==None and node.right==None: #to znaczy ze mam do czynienia z elementem mojej tablicy
            node.actuall_coal+=elements
            node.max-=elements #atrybut pozwalajcy okreslic ile jeszcze moge zmiescic elementow
            return node
        if node.left!=None and node.left.max>=elements: node=node.left #ide, tam gdzie aktualnie znajduje sie wiekszy osiagalny magazyn oraz plnuje zalozenia ze, id musi byc jednoczesnie jak najmniejsze
        else: node=node.right

def update_max(node): #funkcja aktualiazucja max #O(logn)
    element=node.parents
    while element!=None:
        element.max=max(element.left.max,element.right.max)
        element=element.parents

def coal2( A, T ):
    n=len(A)
    root=create_tree(A,T)
    last_transport=0
    for i in range(n): #O(nlogn)
        act_coal=A[i]
        act_node=search_in_tree(root,act_coal)
        update_max(act_node)
        last_transport=act_node.id
    return last_transport

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True)
