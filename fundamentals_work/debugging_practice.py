# def multiply(num_list, num):
#     print(num_list, num)
#     for x in num_list:
#         print(x)
#         x *= num
#         print(num_list)
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

def multiply(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)