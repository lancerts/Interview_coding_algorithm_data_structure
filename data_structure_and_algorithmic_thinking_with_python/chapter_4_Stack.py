##P-3
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
                             
    def isEmpty(self):
        return (len(self.items)==0)
    
    def __str__(self):
        return str(self.items)
        
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = list(postfixExpr)
    
    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()
    
def doMath(op, op1, op2):
    if op == '*':
        return op1*op2
    elif op == '/':
        return op1/op2
    elif op == '+':
        return op1+op2
    else:
        return op1-op2
        
print(postfixEval('123*5-'))

##P-6
class SmartStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def stack_push(self, x):
        self.stack.append(x)
        if not self.min or x <= self.stack_min():
            self.min.append(x)
            
    def stack_pop(self):
        x = self.stack.pop()
        if x == self.stack_min():
            self.min.pop()
        return x
    
    def stack_min(self):
        return self.min[-1]

minstack = SmartStack()
minstack.stack_push(3)
minstack.stack_push(6)
minstack.stack_push(1)
minstack.stack_push(12)
print(minstack.stack_min())
minstack.stack_pop()   
print(minstack.stack_min())
minstack.stack_pop()   
print(minstack.stack_min())
            

##P-6
class Stack(object):
    def __init__(self, stack=[]):
        self.items = stack

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
                             
    def isEmpty(self):
        return (len(self.items)==0)
    
    def __str__(self):
        return str(self.items)      
        
def reverseStack(stack):
    def reverseStackRecursive(stack, newStack=Stack()):
        if not stack.isEmpty():
            newStack.push(stack.pop())
            reverseStackRecursive(stack,newStack)
        return newStack
    return reverseStackRecursive(stack)
        
stk = Stack(range(10))
print stk
print reverseStack(stk)
        
##P-23
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
                             
    def isEmpty(self):
        return (len(self.items)==0)
    
    def __str__(self):
        return str(self.items)  
        
def findingSpans(A):
    D = Stack()
    S = [None]*len(A)
    for i in range(len(A)):
        while not D.isEmpty() and A[i]>A[D.peek()]:
            D.pop()
        if D.isEmpty():
            P = -1
        else:
            P = D.peek()
        S[i] = i - P
        D.push(i)
    print S

findingSpans(list('63452'))


##P-25
def largestRectangleArea(height):
    stack=[]; i=0; maxArea=0;
    while i<len(height):
        if stack==[] or height[i]>height[stack[len(stack)-1]]:
            stack.append(i)
        else:
            curr=stack.pop()
            width=i if stack==[] else i-stack[len(stack)-1]-1
            maxArea=max(maxArea,width*height[curr])
            i-=1
        i+=1
    while stack!=[]:
        curr=stack.pop()
        width=i if stack==[] else len(height)-stack[len(stack)-1]-1
        maxArea=max(maxArea,width*height[curr])
    return maxArea

largestRectangleArea([1,2,22,22,3,3,3,1,1])