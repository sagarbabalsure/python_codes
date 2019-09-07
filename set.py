set1={1,3,5,253,354}
set2={2,3,5,768,56}

print(set1)
print(set2)
#set3=set1.union(set2)
print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set1.issubset(set2))
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))

set2.add(33)
set2.update([23,3544,453])
print(set1)
print(set2)

set1.remove(5)
set2.discard(234)
print(set1)
print(set2)
set1.clear()
print(set1)
print(set2)
del set2
print(set1)
#print(set2)