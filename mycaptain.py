n = int(input("enter number of terms :"))
    first = 0
    second = 1
    print(first,second,end=" ")
    for i in range(n - 2):
        third = first + second
        print(third,end=" ")
        first = second
        second = third    
