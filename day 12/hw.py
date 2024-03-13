
choose_number = int(input(" (Choose a number from 1 to 9): "))

print( {choose_number} up to 50:")
for i in range(1, 51):
    if i % choose_number == 0:
        print(i)
    


