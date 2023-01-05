s = set()
s.add(4) #no repetition
s.add(7)
s.add(10)
s.add(40)
s.add((6,9,10))
 # s.add({6:8}) cannot add list or dictionary to sets
print(s)
print(len(s)) # print the length of the set

s.remove(4) #remove 4 for set
s.pop() #remove any 1 value
 
print(s)