# sum_greater_than_75 = 0
# for num in range (50,100):
#     if num > 75:
#         sum_greater_than_75 += num
#         print("sum of numbers greater than 75: ",sum_greater_than_75)
# """
# რიცხვების შემოწმება: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს. სანამ ეს რიცხვი არ იქნება ლუწი, შეეკითხეთ მომხმარებელს თავიდან.

# 1) როგორ შემოვატანინოთ მომხმარებელს რიცხვი
#     ა) გამოვიყენოთ input() ახსნა: ეს ფუნქცია გვაძლევს იმის საშუალებას რომ ტერმინალიდან შევიტანოთ მნიშვნელობა პროგრამაში,ეს მნიშვნელობა კი ყოველტვის იქნება სტრინნგი
    
#     ბ) ზემოთ მოცემულის გათვალისწინებით თუ input() ფუნქცია ყოველთვის გვიბრუნებს სტრინგს, ჩვენ გვიწევს რომ ის გარდავქმნათ ნამდვილ რიცხვად, მიზეზი არის ის რომ მიწევს კონკრეტული მნიშვნელობის შემოწმება, არის თუ არა ის ლუწი რიცხვი, იმისთვის რომ კონკრეტული მნიშვნელობა გარდავქმნა რიცხვად ვიყენებ int() ფუნქციას

# 2) როგორ გავაკეთოთ ისეთი ინსტრუქცია რომელიც ამოწმებს არის თუ არა რიცხვი ლუწი და იქამდე შემოვატანინოთ მომხმარებელს თავიდან მნიშვნელობა სანამ არ დაემთხვევა პირობას
#     ა) გამოვიყენოთ ციკლი სახელად while რადგან ამ ციკლის გამოყენებიტ შემიძლია შევამოწმო პირობა, მარტივად ეს ციკლი იმუშავებს პირობაზე დაყრდნობით
    
#     ბ) while ციკლს გადავცემ პირობას რომელიც ამოწმებს არის თუ არა რიცხვი ლუწი ანუ იქამდე შემოვატანინოთ მომხმარებელს რიცხვი სანამ ლუწი არ იქნდება ესეიგი სანამ number % 2 != 0
# """

# number = int(input("Please enter number: "))

# while number % 2 != 0:
#     number = int(input("Please enter number: "))
    # ori toloba aris shedarebis operatori xolo 1 toloba aris minichebistvis gamoyenebuli
# sum = 0

# for i in range(50, 100 + 1):
#     if i % 2 != 0:
#         print(i)
#     if i > 75:
#         sum = sum + i

# print(sum)


number = int(input("Please enter number: "))

number_after_addition = number + 20

while number < number_after_addition:
    print(number)
    number = number + 1