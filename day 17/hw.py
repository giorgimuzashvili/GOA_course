# მომხმარებელს შემოატანინეთ ხუთი რიცხვი და ყველა შეიტანეთ სიაში. თქვენი დავალებაა,
# რომ დაბეჭდოთ ამ სიის ჯამი, არ გამოიყენოთ sum მეთოდი.
# numbers = []
# for i in range(5):
#     number = int(input("enter number: "))
#     numbers.append(number)


# total = 0
# for num in numbers:
#     total += num

# print( total)




# სიაში შეიტანეთ თქვენთვის სასურველი 10 რიცხვი. დაბეჭდეთ ამ სიაში არსებული ყველაზე დიდი რიცხვი,
# მინიშნება: გამოიყენეთ for ციკლი. არ გამოიყენოთ max მეთოდი.

# შეყვანილი რიცხვების წამოღება
# numbers = []
# for i in range(10):
#     number = int(input("enter number: "))
#     numbers.append(number)


# max_number = numbers[0]
# for num in numbers:
#     if num > max_number:
#         max_number = num

# print( max_number)



# სიაში შეიტანეთ 30-იდან 50-ის ჩათვლით არსებული ყველა რიცხვი.
# შემდეგ დაითვალეთ ამ სიაში არსებული კენტი რიცხვები და დაბეჭდეთ მათი რაოდენობა.



# count_odd = 0
# for num in range(30, 51):
#     if num % 2 != 0:
#         count_odd += 1


# print( count_odd)


# სიაში შეიტანეთ 10-იდან 50-ის ჩათვლით არსებული 4-ის ჯერადი რიცხვები.
# შემდეგ შეაბრუნეთ ეს სია და დაბეჭდეთ ის, test case: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]


# numbers = []
# for num in range(10, 50 +1):
#     if num % 4 == 0:
#         numbers.append(num)


# print( numbers)


# reversed_numbers = numbers[::-1]
# print( reversed_numbers)


# თქვენი დავალებაა, რომ სიაში შეიტანოთ 50-იდან 100-მდე არსებული ყველა რიცხვი.
# შემდეგ გამოიყენეთ for ციკლი და 
# დაბეჭდეთ ყველა ლუწი რიცხვი  მათი ინდექსებით. test case: ["50 - 0", "52 - 3", "54 - 5", "56 - 7"]




numbers = list(range(50, 100 + 1))
for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        print(f"{numbers[index]} - {index}")


