def ternarySearch(arr,low,high):
    import sys
    c1 = (2*low +   high)//3
    c2 = (  low + 2*high)//3
    if low == c1 or c1 == c2 or c2 == high:
        m = sys.maxsize
        for i in range(low,high+1):
            m = min(m,arr[i])
        return m
    if arr[c1] <= arr[c2]:
        return ternarySearch(arr,low,c2)
    else:
        return ternarySearch(arr,c1,high)