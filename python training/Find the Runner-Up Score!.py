if __name__ == '__main__':
    n = int(input())
arr = map(int, input().split())
arrRmDup = []
for num in arr: 
    if num not in arrRmDup:
        arrRmDup.append(num)
            
arrRmDup.sort(reverse = True)
print(arrRmDup[1])