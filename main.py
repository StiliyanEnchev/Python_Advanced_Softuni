def bubble_sort(numbers):
    is_sorted = False

    i = 0

    while not is_sorted:
        is_sorted = True

        for j in range(1, len(numbers) - i):

            if numbers[j - 1] > numbers[j]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
                while
                is_sorted = False

        i += 1

a = 6
numbers = [int(x) for x in input().split()]
bubble_sort(numbers)
print(*numbers)