# array[1,3,2,5,4]
def bubble_sort(arr):
    k= len(arr)
    for i in range(k):
        for j in range(i+1,k):
            if arr[i] > arr[j]:
                tam = arr[i]
                arr[i] = arr[j]
                arr[j] = tam

arr=[]
n= int(input())
for i in range(n):
    num= int(input(f"Nhap {n} so"))
    arr.append(num)
bubble_sort(arr)
print("mang sau khi sap xep", arr)








