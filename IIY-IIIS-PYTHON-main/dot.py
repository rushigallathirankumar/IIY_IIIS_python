# n = int(input('enter a rows:'))
# for i in range(0, n+1):
#     for j in range(i):
#         print("1", end=" ")
#     print()

n = int(input('enter number of rows:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()