# Algoritimo de ordenação de array QUICK SORT() - dividir e conquistar


def quick_sort(arr, pos_left, pos_rigth ):
    if pos_left < pos_rigth: 
        print(arr)
        pi = partition(arr, pos_left, pos_rigth)
        quick_sort(arr, pos_left, pi-1)
        quick_sort(arr, pi+1, pos_rigth)


def partition(arr, pos_left, pos_rigth):
    pivot = arr[pos_rigth]
    i = pos_left-1
    
    for j in range(pos_left, pos_rigth):
        #print(f'{arr[j]} <= {pivot}')
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]    
    
    arr[i+1], arr[pos_rigth] = arr[pos_rigth], arr[i+1]
    
    return i+1




arr = [3,1,2,7,2,6,8,9,1,2,0]
quick_sort(arr=arr, pos_left=0, pos_rigth=(len(arr)-1))
print(arr)