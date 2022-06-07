

l = []  
  
num_list = int(input("Enter number of elements in list: "))  
  
for i in range(1, num_list + 1):  
    l2 = int(input("Enter the elements: "))  
    l.append(l2)  
  
  
l3=[]
for i in l:
    if i not in l3:
        l3.append(i)
l3.sort()
a=l3[-2]
print("Second largest element is : ",a)
print("Position of Second largest element is : ",l.index(a))