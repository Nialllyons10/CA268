def get_counts_dict(words):
   dict1 = {}
   for word in words:
       if len(word) not in dict1:
           dict1[len(word)]= 1
       else:
           x = int(dict1[len(word)])
           dict1[len(word)] = x + 1
   return(dict1)    
