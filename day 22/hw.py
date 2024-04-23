# შექმენით ფუნქცია სახელად numbers_product. ფუნქციას გადაეცით სამი არგუმენტი - 
# start, end, step. შემდეგ გამოიყენეთ while ციკლი (for ციკლი არ შეიძლება) 
# და სიაში დაამატეთ რიცხვები - დაიწყეთ start-იდან, 
# იტერაცია მოახდინეთ step-ით და ციკლი ამუშავეთ end-ამდე.
# განიხილეთ ეს სია და მოახდინეთ მასზე ფილტრაცია, კიდევ ახალ სიაში დაამატეთ მარტო
# 3-ის ჯერადი რიცხვები. საბოლოოდ დააბრუნეთ 3-ის ჯერადების სიის ყველა რიცხვის ნამრავლი -
# product.


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


# შექმენით ფუნქცია სახელად hashtag generator.
# მომხმარებელს შეეკითხეთ წინადადება და ის გადაეცით არგუმენტად ფუნქციას.
# მუშაობის წესები: საბოლოო ვერსია იწყება #-თი, სიტყვები შეერთებულია, 
# ყველა სიტყვა იწყება დიდი ასოთი. Test case:
# "abc def ghi" -> "#AbcDefGhi"



# def hashtag_generator(phrase):
#     words = phrase.split()
#     capitalized_words = [word.capitalize() for word in words]
#     hashtag = '#' + ''.join(capitalized_words)
#     return hashtag


# test_phrase = "abc def ghi"
# print(hashtag_generator(test_phrase)) 




# შექმენით ფუნქცია სახელად num_divisors. ამ სიას არგუმენტად გადაეცით მომხმარებლის
# მიერ შემოტანილი მთელი რიცხვი. თქვენი დავალებაა,
# რომ დააბრუნოთ სია, სადაც იქნება ამ რიცხვის ყველა გამყოფი. Test case: 20 -> [1, 2, 4, 5, 10, 20]

# def num_divisors(number):
#     divisors = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             divisors.append(i)
#     return divisors


# test_number = 20
# print(num_divisors(test_number))  







# შექმენით ფუნქცია manual_split. ამ ფუნქციაში უნდა შეიმუშავოთ split-ის
# მსგავსი ალგორითმი, მაგრამ არ გამოიყენოთ თვითონ split. თქვენ ფუნქციას
# არგუმენტად გადაეცით მომხმარებლის მიერ შემოტანილი სიტყვა. ასევე მომხმარებელს შეეკითხეთ 
# start, end, step
# მნიშვნელობები, გადაეცით ფუნქციას და იმუშავეთ სიტყვაზე. Test case:
# "Hello World!", 2, 6, 2 -> "lo".



# def manual_split(string, start, end, step):
#     result = ""
#     for i in range(start, end, step):
#         result += string[i]
#     return result


# test_string = "Hello World!"
# start = 2
# end = 6
# step = 2
# print(manual_split(test_string, start, end, step))  





# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/python

# def solution(number):
#     if number < 0:
#         return 0

#     total = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i

#     return total
  