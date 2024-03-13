#declaring firs place values of books
#book names can be changed in future
book1_first_price = 10
book2_first_price  = 20
book3_first_price  = 30
book4_first_price = 40
book5_first_price = 50
book6_first_price  = 60
book7_first_price = 80
book9_first_price = 100
#declaring values of discounts

small_discount = 10
large_discount = 20

#declaring value of books after discount
#declaring small discount
book_small_discount1 = book1_first_price * small_discount/100
book_small_discount2 = book2_first_price * small_discount/100
book_small_discount3 = book3_first_price * small_discount/100
book_small_discount4 = book4_first_price * small_discount/100
book_small_discount5 = book5_first_price * small_discount/100

#declaring values of large discount

book_large_discount1 = book1_first_price * large_discount/100
book_large_discount2 = book2_first_price * large_discount/100
book_large_discount3 = book3_first_price * large_discount/100
book_large_discount4 = book4_first_price * large_discount/100
book_large_discount5 = book5_first_price * large_discount/100
#displaying last prices of books with small discount
print("book1'sfirst price is" ,book_small_discount1, "book2's first price is",book_small_discount2,
"book3's first price is" ,book_small_discount3, "book4's first price is" ,book_small_discount4,
"book5's first price is" ,book_small_discount5,)
#displaying last prices of with large discount
print("book1 costs" ,book_large_discount1, "book2 costs" ,book_large_discount2,
"book3 costs" ,book_large_discount3, "book4 costs" ,book_large_discount3,
"book4 costs" ,book_large_discount4, "book5 costs ",book_large_discount5,)






