friends = ["Rolf", "John", "Charlie", "Mani"]
#counter = 0
#for name in friends:
#    print(counter)
#    print(name)
#    counter = counter + 1
    
for counter, name in enumerate(friends, start =1):
    print(counter,name)  
    
print(list(enumerate(friends)))
print(list(zip([0,1,2], friends)))

print(dict(enumerate(friends, start =1)))
