#第一题
num_list = [6,4,-3,5,-2,-1,0,1,-9]
def quicksort(arr):
    if len(arr) < 2:
        return arr
    mid = arr[len(arr)//2]
    left, right = [], []
    arr.remove(mid)
    for i in arr:
        if i >= mid:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left) + [mid] + quicksort(right)

print(quicksort(num_list))




#第二题
d={'A': 1, 'B.A': 2, 'B.B': 3, 'CC.D.E': 4, 'CC.D.F': 5}
new_d = {}
for key in d:
    if "." not in key:
        new_d[key] = d[key]
    else:
        lst = key.split(".")
        l = len(lst)
        now_d = new_d
        for i in range(l-1):
           try:
                now_d[lst[i]]
           except:
                now_d[lst[i]] = {}
                now_d = now_d[lst[i]]
                now_d[lst[-1]] = d[key]
print(new_d)













