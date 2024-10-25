numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

for i, value in enumerate(numbers):
    if value is None:
        index = i
        numbers[i] = 0
        break
average = sum(numbers) / len(numbers)
numbers[index] = average
# TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:", numbers)
