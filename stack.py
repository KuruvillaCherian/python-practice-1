class _StackNode :
	def __init__( self, item, link ) :
		self.item = item
		self.next = link

class Stack :
	def __init__( self ):
		self._top = None
		self._size = 0	
		
	def peek( self ):
		assert not self.is_empty(), "Cannot peek at an empty stack"
		return (self._top.item)
	
	def push( self, item ):
		''' Method to push an item to the top of a Stack
		'''
		new_node = _StackNode(item, self._top)
		self._top = new_node
		self._size += 1

	def is_empty(self):
		''' Used to tell us whether the Stack is empty (returns a True or False)
		'''
		return self._size == 0

	def __len__(self):
		''' Overrides the Python len() method for Stack objects
		'''
		return self._size

	def pop(self):
		''' Method to pop an item from the top of a Stack
		'''
		assert not self.is_empty(), "Cannot peek at an empty stack"
		popped = self._top.item #pop top of stack
		self._top = self._top.next #next up after previous top of stack becomes new top
		self._size -= 1
		return popped

    
	     
