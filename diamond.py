#this is a code for hollow diamond
i=0
j=0
k=0
for i in range(10,0,-1):
    k=k+1

    for j in range(10,0,-1):
        if j==k:
            print("*", end="")
        else:
            print("  ", end="")
    for j in range(11):
        if j==k:
            print("*", end="")
        else:
            print("  ", end="")
    print()
for i in range(10):
    k=k+1
    for j in range(10):
        if j==i:
            print("*", end="")
        else:
            print("  ", end="")
    for j in range(10,0,-1):
        if j==i:
            print("*", end="")
        else:
            print("  ", end="")
    print()
