#Student name: Becky Tseng
#Student ID: 2038591

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers)-1):
        max_index = i
        for j in range(i+1, len(numbers)):
            if numbers[max_index] < numbers[j]:
                max_index = j
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
        for value in numbers:
            print(value, end=" ")
        print()
    return numbers

if __name__ == "__main__":
    numbers = []
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)