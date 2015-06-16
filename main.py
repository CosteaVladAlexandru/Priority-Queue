class heap:
    def __init__(self,orig=None,cmp=lambda x,y:x>y):
        '''Initialisarion of the heap.
orig = list on which the heap is built. default: None
cmp = comparation function for heap. default: x>y'''
        self.nodes=[]
        self.comp=cmp
        self.push_many(orig)
        
    def _cmp(self,a,b):
        '''comparation function for 2 values.
Default: x>y'''
        return self.comp(self.nodes[a],self.nodes[b])
        
    def _parent(self,x):
        '''The parent of node x'''
        if x==0:
            return None
        return (x-1)//2
        
    def _left(self,x):
        '''The left child of node x'''
        y=x*2+1
        if y<len(self.nodes):
            return y
        return None
        
    def _right(self,x):
        '''The right child of node x'''
        y=x*2+2
        if y<len(self.nodes):
            return y
        return None
        
    def _redo(self,k):
        '''Rebuilds the heap starting at node k'''
        left=self._left(k)
        right=self._right(k)
        if not(left or right):
            return
        elif not right:
            if self._cmp(left,k):
                self.nodes[left],self.nodes[k]=self.nodes[k],self.nodes[left]
        else:
            if self._cmp(left,k) and self._cmp(left,right):
                self.nodes[left],self.nodes[k]=self.nodes[k],self.nodes[left]
                self._redo(left)
            elif self._cmp(right,k):
                self.nodes[right],self.nodes[k]=self.nodes[k],self.nodes[right]
                self._redo(right)
         
    def push(self,other):
        '''push an element into the heap. O(log n)'''
        self.nodes.append(other)
        k=self._parent(len(self.nodes)-1)
        while k!=None:
            self._redo(k)
            k=self._parent(k)
            
    def push_many(self,other):
        '''push multiple elements into the heap.
Complexity of O(n+k), compared to O(k log(n+k)) when
push() is used multiple times, where n is the number
of elements in the heap and k is the number of
elements added.'''
        if not other:
            return
        self.nodes+=other
        for i in range(len(self.nodes)//2-1,-1,-1):
            self._redo(i)

    def max(self):
        '''returns biggest element in heap. O(1)'''
        return self.nodes[0]
        
    def pop(self):
        '''returns and pops biggest element in heap.
O(log n)'''
        if self.is_empty():
            raise Exception('Heap is empty!')
        x=self.max()
        self.nodes[0]=self.nodes[-1]
        self.nodes.pop()
        self._redo(0)
        return x
        
    def is_empty(self):
        '''returns True if heap is empty, False otherwise'''
        return not self.nodes
        
def sort(lst,cmp=lambda x,y:x<y):
    '''Sorting using a heap (heapsort)
cmp = comparation to be used. Default: x<y'''
    x=heap(lst,cmp)
    return [x.pop() for i in range(len(lst))]


#Testing the heap
print(sort([1,2,3,4,1,2,6,7,2,1,-1]))
print(sort([9,1,2,7,4],lambda x,y:x>y))
x=heap([2,9,7])
print(x.max())
x.push(11)
print(x.max())
x.push_many([13,15])
print(x.max())
print(x.pop(),x.pop(),x.pop(),x.pop())
print(x.pop(),x.pop())
try:
    print(x.pop())
except:
    print('Oh no! Something went wrong!')
