#to search for "cherry" in the given list
#if found,stop iteration and display index value
list2 = ["apple","oats","grapes","cherry","mangos","coconut"]
c = 0
for item in list2:
    if(item == "cherry"):
        print("Element found")
        print("At index",c)
    c = c + 1
