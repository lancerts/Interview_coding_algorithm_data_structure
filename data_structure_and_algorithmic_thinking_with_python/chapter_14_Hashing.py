## P-8
def check_pair(A):
    pair_dict = {}
    pair_sym = []
    for i in range(len(A)):
        if A[i][1] in pair_dict:
            pair_sym.append([(A[i][1],pair_dict.get(A[i][1])),(pair_dict.get(A[i][1]),A[i][1])])
        else:
            pair_dict[A[i][0]] = A[i][1]
    return pair_sym

        
    
    
    
A = [(1,2),(2,1),(3,4),(7,8),(9,100),(4,3)]
check_pair(A)


##P-12
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x]+1, i+1)
            dict[x] = i

num = [1,2,3,4,5,90]
target = 91
sol = Solution()
sol.twoSum(num, 0)
     
#A,B two lists

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num1, num2, target):
        dict = {key:i for (key,i) in zip(num2, xrange(len(num2)))}
        for i in xrange(len(num1)):
            x = num1[i]
            if target-x in dict:
                return (i+1, dict[target-x]+1)


num1 = [1,2,3,4,5,90]
num2 = [90,1,2,3,4,5,11,22,33,44,55]
target = 101
sol = Solution()
sol.twoSum(num1, num2, target)


##P-13
def RemoveChars(str, removeTheseChars):
    table = {key:1 for key in removeTheseChars.lower()}
    temp = []
    index = 0
    for char in str.lower():
        if char not in table:
            temp.append(char)
            index += 1
    return ''.join(temp)
    
print RemoveChars('caswaeraer', 'aw')


##P-16
def firstRepeatedChar(str):
    table ={}
    for char in str.lower():
        if char in table:
            table[char] +=1
            print ('the first repeated char is: %s' % char)
            return char
        elif char !=' ':
            table[char] = 1
    return

print firstRepeatedChar('acdr  rff')


#P-21
class BloomFilter:
    """Bloom Filter"""
    def __init__(self, m, k, hashFun):
        self.m = m   #m bit vector
        self.vector = [0]*m
        self.k = k   #k independent functions 
        self.hashFun = hashFun
        self.data = {}
        self.falsePositive = 0
        
    def insert(self, key, value):
        self.data[key] = value
        for i in xrange(self.k):
            self.vector[self.hashFun(key+str(i)) % self.m] = 1

    def contains(self, key):
        for i in xrange(self.k):
            if self.vector[self.hashFun(key+str(i)) % self.m] == 0:
               return False
        return True
    
    def get(self, key):
        if self.contains(key):
            try:
                return self.data[key]
            except KeyError:
                self.falsePositive += 1
                        
import hashlib
def hashFunction(x):
    h = hashlib.sha256(x)
    return int(h.hexdigest(), base = 16)

print (hashFunction('10'))

b = BloomFilter(100, 10, hashFunction)
b.insert('test key', 'new value')
print b.get('test key2')
print b.get('test key')
print b.contains('test key2')


# HashTable
class HashTable:
    def __init__(self, size):
        self.size = size    
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data    ##update value
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data   ##update value
   
    def hashfunction(self, key, size):
        return key%size
    
    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data
        
    def __getitem__(self, key):
        return self.get(key)
        
    def __setitem__(self, key, data):
        self.put(key,data)

H = HashTable(10)
H[54] = 'abc'
H.get(54)

H[32] = 38
H[12] = 38
H[422] = '38'
H[432] = '38'

print H.slots           
print H.data                

    