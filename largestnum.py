my_list=list(input().split())
print(my_list)
max=my_list[0]
for i in range(len(my_list)):
    if my_list[i]>max:
        max=my_list[i]
        
print(max)
    