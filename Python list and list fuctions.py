grocery = ["Chawal", "Aatta", "Doodh", "Dahi", "Ghee", 32,
           23, 45]
print(grocery)
number = [3,5,2,7,989,12,8787]
print(number)
number.sort()
print(number)
number.reverse()
print(number)
print(number[2])
#slicing in lists
print(number[:3])
print(number[:])
#extended slicing in lists
print(number[::])
print(number[::1])
print(number[::2])
print(number[::3])
print(number[::-1])
print(number[::-2])
#functions
print(len(number))
print(max(number))
print(min(number))
#append function
number.append(34)
number.append(34)
print(number)
number.insert(1,23)
print(number)
number.remove(23)
print(number)
#pop to remove the last element
number.pop()
print(number)
number[1] = 23
print(number)
#tuples in python
#muteable - can change
#immutable - cannot change
#tuples are immutable means its values are not changeable
#tp[3] = 23 'this is wrong in tuple'
tp = (2,4,4,4,3)
print(tp)
print(list(tp))
#can take on value with comma
cp = (1,)
print(cp)


#if you want to alternate the value
a= 1
b =3
a,b=b,a
print(a,b)



