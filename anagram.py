# # Complete the anagram function below.
# def anagram(s):
#     n = len(s)
#     count = 0
#     if n % 2 != 0:
#         return -1
#     else:
#         s1 = s[0:n // 2]
#         s2 = s[n // 2:]
#         for ele in set(s1):
#             if ele in s2 and n > 0:
#                 print(ele)
#                 if s1.count(ele)-s2.count(ele) > 0:
#                     count += s1.count(ele)-s2.count(ele)
#                 n -= abs(s1.count(ele)-s2.count(ele))
#             elif s1.count(ele) > 0 and n > 0:
#                 count += 1
#                 n -= s1.count(ele)
#     return str(count)
#
#
# if __name__ == '__main__':
#
#     q = int(input())
#
#     for q_itr in range(q):
#         s = input()
#
#         result = anagram(s)
#
#         print(result)
