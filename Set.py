#set always carrys the unique values
s = set()
print(type(s))
s_from_list = set([2,3,4,5,6])
print(s_from_list)
print(type(s_from_list))
#functions in set
#fuction to add element in set
s.add(1)
s.add(3)
s.add(4)
s1 = s.union({1,3,4,4,5})
s2 = s.intersection({1,3,4,4,5})
s3 = s.isdisjoint({1,3,4,4,5})
s4  = s.difference({1,3,4,4,5})
s5 = s.symmetric_difference({1,3,4,4,5})
print(s,s1)
print(s2,s3,s4,s5)
print(len(s))
print(min(s))
print(max(s))
s.remove(4)
print(s)
print(len(s))
#we can also show the ven diagram of the sets using python



