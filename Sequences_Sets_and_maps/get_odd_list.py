def get_odd_list():
  num = int(input())
  lst = []
  while num != -1:
     if num % 2 == 1:
         lst.append(num)
  
     num = int(input()) 
  
  return lst    
