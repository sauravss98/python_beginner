#pattern 1
'''
    *
    * *
    * * *
    * * * *
'''

# n=int(input(" Enter the number of rows"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print('*',end=' ')
#     print()

#pattern 2
'''
 * * * *
 * * * 
 * * 
 *
'''

# n=int(input(" Enter the number of rows"))
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print('*', end=" ")
#     print()

#pattern 3
'''
1
1 2 
1 2 3
1 2 3 4
'''
# n=int(input("Enter the number or rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#pattern 4
'''
1
2 2
3 3 3
4 4 4 4
'''
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#      for j in range(1,i+1):
#          print(i,end=" ")
#      print()

#pattern 5
'''
A
A B 
A B C
A B C D
'''
# n=int(input(" Enter the number of rows"))
# for i in range(65,65+n):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()

#pattern 6
'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1
'''

# n=int(input(" Enter the number of rows"))
# for i in range(n,1,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#pattern 7
'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''

# n=int(input(" Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i-j+1,end=" ")
#     print()

#pattern 8
'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1 
1
'''
# n=int(input(" Enter the number of rows"))
# for i in range(n+1,1,-1):
#     for j in range(1,i):
#         print((i-j),end=" ")
#     print()

#PATTERn 9
'''
1 1 1 1
2 2 2
3 3
4
'''
# n=int(input(" Enter the number of rows"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(n-i+1,end=" ")
#     print()

#Pattern 10
'''
0
0 1
0 2 4 
0 3 6 9
'''

# n=int(input(" Enter the number of rows"))
# for i in range(0,n+1):
#     for j in range(0,i+1):
#         print(j*i,end=" ")
#     print()

# Pattern 11
'''
1
1 0
1 0 1
1 0 1 0
'''

# n=int(input(" Enter the number of rows"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         if(j==0 or j%2==0):
#             print('1',end=" ")
#         else:
#             print('0',end=" ")
#     print()

# Pattern 12
'''
1
2 3 
4 5 6
7 8 9 10
'''

# n=int(input(" Enter the number of rows"))
# a=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(a,end=" ")
#         a+=1
#
#     print()

#Pattern 13
'''
A
B C
D E F
G H I J
'''
# n=int(input(" Enter the number of rows"))
# a=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(a),end=" ")
#         a+=1
#     print()

#Pattern 14
'''
      A
    B A
  C B A
D C B A
'''

# n = int(input(" Enter the number of rows: "))
# a=65
# for i in range(1, n+1):
#     for j in range(1, (n-i)+1):
#         print(" ",end=" ")
#
#     for j in range(1,i+1):
#         print(chr(a+(i-j)), end=" ")
#     print( )


#Pattern 15
'''
A B C D
A B C
A B
A
'''
# n=int(input(" Enter the number of rows"))
# for i in range(65+n,65,-1):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()

#Pattern 16
'''
A
B A
C B A
D C B A
'''
# a=65
# n=int(input(" Enter the number of rows"))
# for i in range(0,n):
#     for j in range(0,i+1):
#
#         print(chr(a+(i-j)), end=" ")
#     print()

# Problem 21
'''
      * 
    * * *
  * * * * *
* * * * * * *
'''
# n=int(input(" Enter the number of rows"))
# k=n-1
# for i in range(0,n):
#     for j in range(0,k):
#         print(end=" ")
#     k=k-1
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# Problem 22
'''
* * * * * * *
  * * * * *
    * * *
      *
'''
# n=int(input(" Enter the number of rows"))
# k=2*n-2
# for i in range(n,-1,-1):
#     for j in range(k,0,-1):
#         print(end=" ")
#     k=k+1
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# Problem 19
'''
    A
   A B
  A B C
 A B C D
'''
# n=int(input(" Enter the number of rows"))
# k=n-1
# a=65
# for i in range(0,n):
#     for j in range(0,k):
#         print(end=" ")
#     k=k-1
#     for j in range(0,i+1):
#         a=65+j
#         print(chr(a),end=" ")
#     print()

# Problem 23

# n = int(input(" Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, (n-i)+1):
#         print(" ",end=" ")
#
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print( )

'''
    a
  a b a
c b a b a
'''
n=int(input("enter the number"))
k=2*n-2

for i in range(65,65+n):
    for j in range(0,k):
        print(end=' ')
    k=k-2
    for l in range(65,i+1):
        print(chr(l),end=' ')
    for r in range(i-1,64,-1):
        print(chr(r),end=' ')
    print()

n=int(input(" Enter the number of rows"))
k=n-1
a=65
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        a=65+j
        print(chr(a),end=" ")
    print()
for i in range(n,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0,i+1):
        a=65+j
        print(chr(a),end=" ")
    print()


