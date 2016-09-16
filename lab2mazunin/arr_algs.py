def min(arr):
    min = arr[0]
    for n in arr:
        if n < min:
            min = n
    print("Минимальное значение в массиве: ", min)

def sred(arr):
    sum = 0
    for n in arr:
        sum = sum + n
    answer = sum / len(arr)
    print("Среднее арифметическое в массиве: ", answer)

print("Добро пожаловать в мою программу!")
print()
arr1 = [6, 8, 4, 12, 5]
min(arr1)
sred(arr1)
