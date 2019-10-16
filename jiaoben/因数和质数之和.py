#!/usr/bin/python3
# -*- coding: utf-8 -*-
import python
# def ys():
    #ys()

    # # 因数之和 :所有能被数整除的数
    # def ys():
    #     sum = 0
    #     for i in range(1, 10):
    #         for j in range(1, i + 1):
    #             if i % j == 0:
    #                 sum = sum + j
    #
    #     print(sum)
    #
    # ys()


#质数之和
# sum = 0
# for i in range(3,10):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         sum += i
# print(sum)

def zhishu():
    sum=0
    for i in range(3,10):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            sum=sum+i
            print(i)
zhishu()


