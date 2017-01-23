#
#  Just a class to store the item and the next pointer
#
class Node:
  def __init__(self, item, next):
  self.item = item
  self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
  def __init__(self):
    self.head = None

  def add(self, item):
    self.head = Node(item, self.head)

  def remove(self):
    if self.is_empty():
      return None
    else:
      item = self.head.item
      self.head = self.head.next    # remove the item by moving the head pointer
    return item

  def is_empty(self):
    return self.head == None

  def count(self):
    return self.recursive_count(self.head)

  def largest(self):
    return self.check(self.head)
    
  def check(self,ptr):
    if ptr == None:
	    return
    elif ptr.next == None:
	    return ptr.item
    else:
	    maxi = self.check(ptr.next)
	
    if maxi > ptr.item:
	    return maxi
    else:
	    return ptr.item
