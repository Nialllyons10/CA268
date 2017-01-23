def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    swaps = 0
    compares = 0
    
    for todo in range(1, len(lst)):
         # Find correct position for lst[todo].
         i = todo
         while i > 0 and lst[i] < lst[i-1]:
            compares += 1
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            swaps += 1
            i -= 1
        
        compares += int(i > 0)
    
    return compares, swaps
