#program to display elements from list
#do not display if number is even
list3 = [1,13,14,17,19,18,20,25]
for item in list3:
    if(item %2==0):
        continue
    print(item)
