#1
a={5: 'Hi', 6: 'To', 7: 'Hello', 'A': {1: 'welcome', 2: 'For', 3: 'MANGO'}, 'B': {1: 15, 2: 'car'}}print("before " ,a)
del a['A'][2]
print("after",a)

#2
dict= {'key1': 'Hello', 'key2': 'How are you'}
print("Current Dict is: ", dict)

dict['key3'] = 'Good'
print("Updated Dict is: ", dict)

#3

num=[76.-45,65,14]
print ("numbers in the list:",num)
new_num= list(filter(lambda x: x<0,num))
print ("negative no",new_num)

#4
starts_with= lambda x: True if x.startswith('D') else False
print (starts_with('Aseem'))
starts_with = lambda x:True if x.startswith('D') else False
print(starts_with('Srivastava'))

#5
nums = (1, 2, 3, 4, 5)
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums)
print("\nTriple of said list numbers:")g
print(list(result))

#6
lst1 = [19542209, 4887871, 1420491, 626299, 1805832, 39865590]

lst2 = ["New York", "Alabama", "Hawaii", "Vermont", "West Virginia", "California"]
list_zip=list(zip(lst1,lst2))
print (list_zip)



