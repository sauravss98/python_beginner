# # M
# #
# for i in range(0,5):
#     for j in range(0,5):
#         if((j==0 or j==4) or (i==1 and (j==1 or j==3)) or (i==2 and j==2)):
#             print('*',end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# # N
#
# for i in range(0,5):
#     for j in range(0,5):
#         if((j==0 or j==4)or(i==j)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# # Diamond
# for i in range(0,5):
#     for j in range(0,5):
#         if((i==2 and (j==0 or j==4)) or (i==1 and (j==1 or j==3)) or (i==3 and (j==1 or j==3)) or (j==2 and (i==0 or i==4))):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# # G
# for i in range(0,7):
#     for j in range(0,6):
#         if((i!=0 and j==0) or (i==0 and (j==1 or j==2 or j==3 or j==4)) or (i==6 and (j==1 or j==2 or j==3 or j==4)) or (i==3 and (j==2 or j==3 or j==4)) or (j==5 and (i==3 or i==4 or i==5))):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# # V
# for i in range(4):
#     for j in range(7):
#         if((i==0 and(j==0 or j==6)) or (i==1 and(j==1 or j==5)) or (i==2 and(j==2 or j==4)) or (i==3 and j==3)):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# # K
#
# for i in range(7):
#     for j in range(5):
#         if((j==0) or (i==0 and j==4) or (i==1 and j==3) or (i==2 and j==2) or (i==3 and j==1) or (i==4 and j==2) or (i==5 and j==3) or (i==6 and j==4)):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# # Pattern random
# for i in range(9):
#     for j in range(11):
#         if((i==0) or (i==8) or (j==0) or (j==10) or (j!=5 and (i==1 or i==7)) or ((i==2 or i==6)  and (j==0 or j==1 or j==2 or j==3 or j==7 or j==8 or j==9 or j==10)) or((i==3 or i==5) and (j==0 or j==1 or j==2 or j==8 or j==9 or j==10)) or (i==4 and (j==1 or j==9))):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()

# HourGlass
# for i in range(9):
#     for j in range(9):
#         if((i==0 or i==8) or ((i==1 or i==7) and (j==1 or j==2 or j==3 or j==4 or j==5 or j==6 or j==7 )) or ((i==2 or i==6) and (j==2 or j==3 or j==4 or j==5 or j==6)) or ((i==3 or i==5) and ( j==3 or j==4 or j==5 )) or (i==4 and j==4)):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()

# Butterfly

# for i in range(4):
#     for j in range(4):
#         if((i==1 or i==2) or (j==0 or j==3)):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()

# Asterik
# for i in range(7):
#     for j in range(7):
#         if((j==3)or((j==2 or j==4)and(i==2 or i==4))or((j==1 or j==5)and(i==1 or i==5))or((j==0 or j==6)and(i==0 or i==6))):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()

#Pant
for i in range(5):
    for j in range(10):
        if((i==0)or(i==1 and (j!=4 and j!=5))or(i==2 and (j!=3 and j!=4 and j!=5 and j!=6))or (i==3 and (j==0 or j==1 or j==8 or j==9))or(i==4 and (j==0  or j==9))):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print()