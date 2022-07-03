import array as arr 

a = arr.array('i',[1,1,2,3])
                # 0 1 2 
print("Given array : ",end=" ")


for i in range(0,3):
    print(a[i],end=" ")
print()



a.insert(1,4)
a.append(5)


#import array as arr 
print("after", end=" ")


for i in range(0,5):
    print(a[i],end=" ")

print() 


