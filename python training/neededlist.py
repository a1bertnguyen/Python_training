if __name__ == '__main__':
    arr=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
 
    arr=sorted(arr, key = lambda x: (x[1], x[2]))

print(arr)
    
        
        