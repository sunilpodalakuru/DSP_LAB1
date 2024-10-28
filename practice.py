# import numpy as np

# x = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# h = [1, -1, 1]

# N = len(x)
# l = 4
# k = [x[i:i + l] for i in range(0, len(x), l)]

# for i in range(len(h) - 1):
#     for j in range(len(k)):
#         k[j].append(0)

# for i in range(len(k[0]) - len(h)):
#     h.append(0)

# def circular_convolution(x, h):
#     N = len(x)
#     result = np.zeros(N)
    
#     for n in range(N):
#         for m in range(N):
#             result[n] += x[m] * h[(n - m) % N]
    
#     return result

# y = []
# for i in range(len(k)):
#     y.append(list(circular_convolution(k[i],h)))
# # y.pop()
# print(y)
# f=[]
# # s=[]
# for i in range(len(y)):
#     # l=0
#     for j in range(len(y[0])):
#         # if(j==5):
#         #     x=y[0][5]+y[0+1][1]
#         #     s.append(x)
#         if(j!=(len(y[0])-1) and j!=(len(y[0])-2)):
#             f.append(y[i][j])
#         elif(j==len(y[0])-2):
#             f.append(y[i][len(y[0])-2]+y[i+1][0])
#             # l=l+1
#         elif(j==len(y[0])-1):
#             f.append(y[i][len(y[0])-1]+y[i+1][1])
#             # l=l+1
        

# print(f)
# # print(s)

# l=[[1,2],[3,4],[5,6]]
# print(l[0][:])
l=[1,2,3]
l2=[3,4,5]
pr=l.extend(l2)
print(pr)