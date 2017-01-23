def detect_loop(lst):
# Floyd's cycle-finding algorithm, aka. the hare and tortoise algorithm
 if not lst.head or not lst.head.next:
     return False

 tort = lst.head
 hare = lst.head.next
 while hare != tort:
     if not (hare.next and hare.next.next):
        return False
    tort = tort.next
    hare = hare.next.next
return True
