# def numbers_product(start, end, step):
#     numbers = []
#     current = start
#     while current <= end:
#         numbers.append(current)
#         current += step
    
#     filtered_numbers = [num for num in numbers if num % 3 == 0]
    
#     product = 1
#     for num in filtered_numbers:
#         product *= num
    
#     return product




# def hashtag_generator(phrase):
#     words = phrase.split()
#     capitalized_words = [word.capitalize() for word in words]
#     hashtag = '#' + ''.join(capitalized_words)
#     return hashtag


# test_phrase = "abc def ghi"
# print(hashtag_generator(test_phrase)) 




# def num_divisors(number):
#     divisors = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             divisors.append(i)
#     return divisors


# test_number = 20
# print(num_divisors(test_number))  



def manual_split(string, start, end, step):
    result = ""
    for i in range(start, end, step):
        result += string[i]
    return result


test_string = "Hello World!"
start = 2
end = 6
step = 2
print(manual_split(test_string, start, end, step))  
