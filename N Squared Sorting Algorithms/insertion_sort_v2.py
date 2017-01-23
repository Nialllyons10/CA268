def insertion_sort(lst):
   compares = 0
   moves = 0
   
   for todo in range(1, len(lst)):
       tobeinserted = lst[todo]
       moves += 1
       i = todo
       
       while i > 0 and tobeinserted < lst[i-1]:
          compares += 1
          lst[i] = lst[i-1] # Make space for the item
          moves += 1
          i -= 1
      
       compares += int(i > 0)
       lst[i] = tobeinserted  # Found the place for this item, plonk it in
       moves += 1
  
  return compares, moves
