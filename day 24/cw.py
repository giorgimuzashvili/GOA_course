def fake_bin(x):
    result = ''
    for digit in x:
        if int(digit) < 5:
            result += '0'
        else:
            result += '1'
    return result

input_string = "123456789"
result = fake_bin(input_string)
print("Resulting string:", result)








# 5 davaleba

# def count_by(x, n):
#      return [x * i for i in range(1, n + 1)]

# # Example usage:
# x_value = 5
# count = 7
# result = count_by(x_value, count)
# print("First", count, "multiples of", x_value, ":", result)