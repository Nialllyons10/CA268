def get_counts(words):
  counts = [0]* 10
  l = 0
  
  for i in words:
    if len(i) <= 9:
      l = len(i)
      x = int(counts[l])
      counts[l] = x + 1
  
  return counts        
