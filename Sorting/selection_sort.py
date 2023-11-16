
def countSwaps(n,a):
    for i in range(0,n):
        min_val=i
        for j in range(i+1,n):
            if a[min_val]>a[j]:
                min_val=j
            
        temp = a[i] 
        a[i]=a[min_val]
        a[min_val] = temp

    print("Sorted Array", a)


if __name__ == '__main__':
    n = 8
    # a = [8,4,6,2,1,3,7,5]
    a = [8,7,6,5,4,3,2,8]
    countSwaps(n,a)

# ref : https://www.youtube.com/watch?v=5KjapFQNxUo&t=220s