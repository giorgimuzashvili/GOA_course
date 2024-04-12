def my_range(start, end, step = 1):
    numbers = [start]

    counter = start

    if end < start and step >= 0:
        return [start,end]

    for num in numbers:
        counter = counter + step
        if counter == end:
            return numbers
        numbers.append(counter)

print(my_range(10,0))