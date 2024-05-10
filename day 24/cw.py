#valeba
# def litres(time):
    
#     return int(time * 0.5)







# 2 davaleba
# def paperwork(n, m):
   
#     if n < 0 or m < 0:
#         return 0
#     else:
#         return n * m

# 3 davaleba
# def grow(numbers_list):
#     result = 1
    
#     for number in numbers_list:
#         result = result * number
    
#     return result








# 4 davaleba
# def fake_bin(x):
#     result = ""
    
#     for char in x:
#         if int(char) < 5:
#             result = result + "0"
#         else:
#             result = result + "1"
    
#     return result










# 5 davaleba

# def count_by(x, n):
#      return [x * i for i in range(1, n + 1)]






# 7kyu 1 davaleba
# def to_jaden_case(string):
#      return ' '.join(word.capitalize() for word in string.split())


# quote = "how can mirrors be real if our eyes aren't real"
# jaden_case_quote = to_jaden_case(quote)
# print(jaden_case_quote)
  

# 7kyu 2 davaleba
# def accum(st):
#     return '-'.join((c.upper() + c.lower() * i) for i, c in enumerate(st))
# result = accum("abcd")
# print(result)  








# 7kyu 3 davaleba 
# def remove_smallest(numbers):
#     if not numbers:
#         return []
#     min_index = numbers.index(min(numbers))
    
#     return numbers[:min_index] + numbers[min_index + 1:]
# numbers = [4, 3, 1, 2, 5]
# result = remove_smallest(numbers)
# print("Ratings after removing the smallest exhibit:", result)


# 6kyu 4 davaleba

# def solution(number):
#     if number < 0:
#         return 0
#     else:
#         return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0)

# # Example usage:
# number = 10
# result = solution(number)
# print("Sum of multiples of 3 or 5 below", number, ":", result)
 