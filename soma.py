def sum(a, arr):
    if a == 0:
        return arr[a]
    else:
        return arr[a] + sum(a-1, arr)

arr =  [1,2,3,4,5]
print(sum(len(arr)-1,arr))