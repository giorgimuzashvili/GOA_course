#  შექმენით რიცხვთა დიაპაზონი სადაც გექნებით ლუწი რიცხვები.

# numbers_range = range(0,10 +1,2)

# for i in numbers_range :
#     print (i)


# ექმენით სია სადაც გექნებათ 1-დან 10 ის ჩათვლით რიცხვები და SLICE ინგის გამოყენებით შექმენით 
# ახალი სია სადაც გექნებათ მხოილოდ ის მნიშვნელობები შეტანილი, რომლის ინდექსბიც არის ლუწი

# numbers = [1,2,3,4,5,6,7,8,9,10]

# print (numbers [0:10:2])








# lists = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14]
# list0 = []
# for i in lists:
#     if i % 2 == 0:
#         list0.append(i)
        
# print(list0)



# დავალება: შექმენით პროგრამაც, სადაც გექნებათ ორი სია. პირველში 1-იდან 10-ის
# ჩათვლით დაამატეთ ლუწი რიცხვები, ხოლო მეორეში კენტები.
# გამოიყენეთ for ციკლი და append ფუნქცია


# even_numbers = []
# odd_numbers = []

# for i in range(1, 25):
#     if i % 2 == 0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)

# print( even_numbers)
# print( odd_numbers)





# შექმენით პროგრამა სადაც გექნებათ ორი სია. პირველ სიაში 10-იდან 20-ის 
# ჩათვლით ლუწი რიცხვები, ხოლო მეორეში კენტები დაამატეთ.
# საბოლოოდ გამოიტანეთ ამ სიების სხვაობა


# def main():
  
#     even_numbers = [num for num in range(10, 21) if num % 2 == 0]

    
#     odd_numbers = [num for num in range(10, 21) if num % 2 != 0]

#     print( even_numbers)
#     print( odd_numbers)

  
#     difference = sum(even_numbers) - sum(odd_numbers)
#     print( difference)

# if __name__ == "__main__":
#     main()


def main():
    even_numbers = []
    odd_numbers = []

    for i in range(5):
        num = int(input("შეიყვანეთ რიცხვი: "))
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    print("ლუწები:", even_numbers)
    print("კენტები:", odd_numbers)

if __name__ == "__main__":
    main()

