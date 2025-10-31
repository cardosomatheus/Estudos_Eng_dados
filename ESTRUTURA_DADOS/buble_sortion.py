def buble_sort(mylist):
    size = len(mylist)
    

    for m in mylist:
        is_sorted = True
        for i in range(size-1):
            if mylist[i] > mylist[i+1]:
                is_sorted = False
                mylist[i], mylist[i+1], = mylist[i+1], mylist[i]

        if sorted:
            return mylist
    return mylist


print(buble_sort(mylist=[3,1,2]))