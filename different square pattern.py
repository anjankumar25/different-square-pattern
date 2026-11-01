def row(a):
    for i in range(1,a):
        for j in range(1,a):
            if i != 1 and i !=a-1:
                if j !=1 and j !=a-1:
                    print("-",end=" ")
                else:
                    print("*",end=" ")
            else:
                print("*",end=" ")
        print( )
row(6)