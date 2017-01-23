def sum_to_k(lst, k):

  i = 0 
  j = 1
  
  while i != len(lst) - j:
    if lst[i] + lst[len(lst) - j] > k: 
         j += 1
    elif lst[i] + lst[len(lst) - j] <  k :
        i += 1
        j = 1
    elif lst[i] + lst[len(lst) - j] ==  k:
        return lst[i] + lst[len(lst) - j] == k
        
    i += 1
    j = 1
  
  return False 


