from Queue import Queue

def split(q):
   """ A split function which will split a queue into two.
       The function returns a tuple containing the two queues.
   """
   q1 = Queue()
   q2 = Queue()
   for i in range(len(q)):
      if i % 2:
          q1.enqueue(q.dequeue())
      else:
          q2.enqueue(q.dequeue())
  
  return q1, q2
