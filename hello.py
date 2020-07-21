def fin(n):
    a,b = 0,1
    while(a<=n):
        a,b = b,a+b
        print(a)
print("please write no of digit for fabonacci series:")
fin(int(input()))
print("Completed")