# 使用分支结构实现1~100之间的偶数求和
# 不使用分支结构实现1~100之间的偶数求和

sum1 = 0
sum2 = 0
for i in range(1,101):
    #对i进行取余，余数为0则是偶数
    if i%2 == 0:
        sum1 = sum1+i
    elif i%2 == 1:
        sum2 = sum2+i
    print(f"偶数之和为：{sum1}")
    print(f"基数之和为：{sum2}")







# sum1 = 0
# for i in range(1,101):
#     if i % 2 != 0:
#         sum1 = sum1 +i
#     #i += 1
#     i = i+1
# print(f"1-100之間奇數的和是：{sum1}")
