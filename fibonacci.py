# printing n-th number of fibonacci series
# def Fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#         # First Fibonacci number is 0
#     elif n == 0:
#         return 0
#     # Second Fibonacci number is 1
#     elif n == 1:
#         return 1
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)
#
#
# print(Fibonacci(9))


# def fibo(n):
#     if n <= 0:
#         print('Please enter positive number')
#         return
#     a, b = 0, 1
#     for index in range(n):
#         if index < 2:
#             print(index, end=" ")
#         else:
#             a, b = b, a + b
#             print(b, end=" ")
#
#
# fibo(4)

# def fibo(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         if i < 2:
#             yield i
#         else:
#             yield a+b
#             a, b = b, a+b
#
# gen = fibo(0)
# print(list(gen))


# res = 0
# def fib(num):
#      global res
#      a = 0
#      b  = 1
#      if num < 0:
#          return
#      else:
#           for i in range(num):
#                  if i == 0:
#                      yield a
#                  if i == 1:
#                      yield b
#                  else:
#                       res = a+b
#                       a = b
#                       b = res
#                       yield res
#
# result = fib(7)
# print(list(result))