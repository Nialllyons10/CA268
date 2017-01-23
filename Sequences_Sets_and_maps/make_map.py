def make_map():
   n = input()
   student={}
   while n != '' :
       x = n.split(' ')
       student[x[0]]=x[1]
       n = input()
   return student    
