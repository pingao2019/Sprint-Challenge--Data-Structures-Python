#  reference:http://code.activestate.com/recipes/68429-ring-buffer/  
#  https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html



class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.index = 0
    self.storage = [None]*capacity
  
  #append an element at the end of the buffer
  def append(self, item):
    self.storage[self.index] = item
    if self.index == self.capacity -1:
      self.index = 0
    else:
      self.index += 1
  
  #return a list of elements from the oldest to the newest
  def get(self):
    return [i for i in self.storage if i != None]