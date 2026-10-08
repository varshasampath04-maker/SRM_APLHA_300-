def duplicate_zero(arr):

    i = len(arr)-1

    while i >=0:
        if arr[i] ==0:

            arr.insert(i,0)
            arr.pop()

        i = -1

    return arr 
