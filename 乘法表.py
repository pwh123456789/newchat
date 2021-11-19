#for i in range(1, 10):
#        for j in range(1, i + 1):
#           print('{}x{}={}\t'.format(j, i, i * j), end='')
#        print()
x=1
while x <= 9:
    y=1
    while y <= x:
        print('%d*%d=%d\t'  %(y,x,x*y),end='')
        y += 1
    print('')
    x += 1
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}x{}={}\t".format(j,i,i*j),end='')
#     print()
# x = 1
# while x<=9:
#     y=1
#     while y <=x:
#         print('*',end="")
#         y +=1
#     print()
#     x += 1

